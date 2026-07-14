#!/usr/bin/python
"""Contains certificate generation for vin."""

import logging
import os
import pathlib
import shutil
import sys
from pathlib import Path

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
from cryptography.hazmat.primitives.serialization.pkcs12 import load_key_and_certificates

from . import cert_config

work_dir = os.path.dirname(os.path.abspath(__file__))

logger = logging.getLogger(__name__)


def move_file(vin):
    """Move keystore file to temporary directory.

    :param str vin: VIN to generate certificates for by keystore file.
    :return: 1 if moving file worked correctly, 0 if moving failed
    :rtype: int
    """
    scr_dir_abs = pathlib.Path(__file__).parent / cert_config.SCR_DIR
    scr_dir_abs = os.path.join(scr_dir_abs, vin, vin + ".keystore.p12")
    dst_dir_abs = os.path.join(work_dir, work_dir + "\\" + cert_config.TMP_DIR_REL, vin + ".keystore.p12")
    try:
        shutil.copy(scr_dir_abs, dst_dir_abs)
        return 1
    except IOError:
        logger.error(f"Error: Cannot find keystore.p12 for vin {vin}")
        return 0


def extract_certificate(vin):
    """Extract certificates for VIN by keystore file.

    :param str vin: VIN to generate certificates for by keystore file.
    """
    os.chdir(work_dir + "\\" + cert_config.TMP_DIR_REL)
    p12_absolute = os.path.join(work_dir, work_dir + "\\" + cert_config.TMP_DIR_REL, vin + ".keystore.p12")
    backend = default_backend()
    with open(p12_absolute, "rb") as pkcs12_file:
        pkcs12_data = pkcs12_file.read()
    pkcs12_password_bytes = vin.encode("utf8")
    pyca_p12 = load_key_and_certificates(pkcs12_data, pkcs12_password_bytes, backend)
    cert_bytes = pyca_p12[1].public_bytes(Encoding.PEM)
    pk_bytes = pyca_p12[0].private_bytes(Encoding.PEM, PrivateFormat.PKCS8, NoEncryption())

    with open(work_dir + "/tempVinCa/vin.crt", "wb") as pem_file:
        pem_file.write(cert_bytes)

    with open(work_dir + "/tempVinCa/vin.key", "wb") as key_file:
        key_file.write(pk_bytes)


def clear_old_vins():
    """Delete old keystore files from temporary directory."""

    tmpdir = os.path.join(work_dir, work_dir + "\\" + cert_config.TMP_DIR_REL)
    logger.debug(f"Directory: {tmpdir}")
    listdir = os.listdir(tmpdir)
    for item in listdir:
        if item.endswith(".keystore.p12"):
            os.remove(os.path.join(tmpdir, item))


def change_vin(vin):
    """Generate crt and key files for vin by .keystore file.

    :param str vin: VIN to generate certificates for by keystore file.
    :return: Path to Files
    :rtype: str
    """
    if not cert_config.SCR_DIR:
        logger.error("Missing Config")
        sys.exit()
    Path(work_dir + "\\" + cert_config.TMP_DIR_REL).mkdir(parents=True, exist_ok=True)
    clear_old_vins()
    if move_file(vin):
        extract_certificate(vin)

    return work_dir + "\\" + cert_config.TMP_DIR_REL
