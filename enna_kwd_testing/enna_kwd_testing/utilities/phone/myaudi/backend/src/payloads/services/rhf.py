# -*- coding: utf-8 -*-
"""Created on 07.02.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Contains payload for rhf service.
"""

from .. import interface


class Payload(interface.Payload):
    """Remote Honk and flash (RHF) payload."""

    def __init__(self):
        """Initialize payload object for rhf service."""

        super().__init__()

        self.flash_state = interface.RHFFlashState.FLASH_OFF.value
        self.honk_state = interface.RHFHonkState.HONK_OFF.value

        self.prepare_payload()
        self.payload = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n" \
                       f"<honkAndFlash:honkAndFlashState \r\n" \
                       f"xmlns:honkAndFlash=\"http://www.vw.com/mbb/honkAndFlash\" \r\n" \
                       f"xmlns:p=\"http://www.vw.com/mbb/jobMechanism\" \r\n" \
                       f"xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" \r\n" \
                       f"xsi:schemaLocation=\"http://www.vw.com/mbb/honkAndFlash ../../XSD_mbb/2017.1/XSD_RHF/honkAndFlash_v1_0_0.xsd \">\r\n" \
                       f"  <honkAndFlash:flashState>{self.flash_state}</honkAndFlash:flashState>\r\n" \
                       f"  <honkAndFlash:honkState>{self.honk_state}</honkAndFlash:honkState>\r\n" \
                       f"</honkAndFlash:honkAndFlashState>"

        self.get_payload()

    def get_payload(self):
        """Get payload for rhf service.

        :rtype: str.
        :returns: Payload.
        """
        return self.payload
