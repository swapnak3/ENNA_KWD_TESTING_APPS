# -*- coding: utf-8 -*-
"""Created on 10.05.2022.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.
Contains payload for RPT (Remote Profile and Timer Programming) service
"""
import datetime

from .. import interface


class Payload(interface.Payload):
    """ RPT (Remote Profile and Timer Programming) payload """

    def __init__(self, **kwargs):
        """Initialize payload object for RPT service.

        :param kwargs: Arbitrary keyword arguments.
        """

        super().__init__()

        self.utc = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%S")
        self.timestamp_instrument_cluster = self.utc

        self.timer1_state = interface.RPTTimerState.DEACTIVATED.value
        self.timer2_state = interface.RPTTimerState.DEACTIVATED.value
        self.timer3_state = interface.RPTTimerState.DEACTIVATED.value
        self.timer4_state = interface.RPTTimerState.DEACTIVATED.value
        self.timer5_state = interface.RPTTimerState.DEACTIVATED.value
        self.timer6_state = interface.RPTTimerState.DEACTIVATED.value
        self.timer7_state = interface.RPTTimerState.DEACTIVATED.value

        self.prepare_payload(**kwargs)
        self.payload = f"<rptTimerStateReport:rptTimerStateReport xmlns:rptCommonTypes=\"http://www.vw.com/mbb/rptCommonTypes\" \r\n" \
                       f"xmlns:rptTimerStateReport=\"http://www.vw.com/mbb/rptTimerStateReport\" \r\n" \
                       f"xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" \r\n" \
                       f"xsi:schemaLocation=\"http://www.vw.com/mbb/rptTimerStateReport ../../XSD_mbb/2018.1/XSD_RPT/rptTimerStateReport_v1_0_0.xsd \">\r\n" \
                       f"\r\n" \
                       f" <!-- Lade-Serientimer 1 -->\r\n" \
                       f" <rptCommonTypes:timer>\r\n" \
                       f"   <rptCommonTypes:cycle>true</rptCommonTypes:cycle>\r\n" \
                       f"   <rptCommonTypes:hour>15</rptCommonTypes:hour>\r\n" \
                       f"   <rptCommonTypes:instrumentClusterTime>{self.timestamp_instrument_cluster}</rptCommonTypes:instrumentClusterTime>\r\n" \
                       f"   <rptCommonTypes:minute>30</rptCommonTypes:minute>\r\n" \
                       f"   <rptCommonTypes:timerActivationState>{self.timer1_state}</rptCommonTypes:timerActivationState>\r\n" \
                       f"   <rptCommonTypes:timerChargeOption>enabled</rptCommonTypes:timerChargeOption>\r\n" \
                       f"   <rptCommonTypes:timerClimaOption>disabled</rptCommonTypes:timerClimaOption>\r\n" \
                       f"   <rptCommonTypes:timerID>1</rptCommonTypes:timerID>\r\n" \
                       f"   <rptCommonTypes:weekdayBitmask>127</rptCommonTypes:weekdayBitmask>\r\n" \
                       f" </rptCommonTypes:timer>\r\n" \
                       f"\r\n" \
                       f" <!-- Lade-Serientimer 2 -->\r\n" \
                       f" <rptCommonTypes:timer>\r\n" \
                       f"   <rptCommonTypes:cycle>true</rptCommonTypes:cycle>\r\n" \
                       f"   <rptCommonTypes:hour>2</rptCommonTypes:hour>\r\n" \
                       f"   <rptCommonTypes:instrumentClusterTime>{self.timestamp_instrument_cluster}</rptCommonTypes:instrumentClusterTime>\r\n" \
                       f"   <rptCommonTypes:minute>20</rptCommonTypes:minute>\r\n" \
                       f"   <rptCommonTypes:timerActivationState>{self.timer2_state}</rptCommonTypes:timerActivationState>\r\n" \
                       f"   <rptCommonTypes:timerChargeOption>enabled</rptCommonTypes:timerChargeOption>\r\n" \
                       f"   <rptCommonTypes:timerClimaOption>disabled</rptCommonTypes:timerClimaOption>\r\n" \
                       f"   <rptCommonTypes:timerID>2</rptCommonTypes:timerID>\r\n" \
                       f"   <rptCommonTypes:weekdayBitmask>23</rptCommonTypes:weekdayBitmask>\r\n" \
                       f" </rptCommonTypes:timer>\r\n" \
                       f"\r\n" \
                       f" <!-- Lade-Serientimer 3 -->\r\n" \
                       f" <rptCommonTypes:timer>\r\n" \
                       f"   <rptCommonTypes:cycle>true</rptCommonTypes:cycle>\r\n" \
                       f"   <rptCommonTypes:hour>3</rptCommonTypes:hour>\r\n" \
                       f"   <rptCommonTypes:instrumentClusterTime>{self.timestamp_instrument_cluster}</rptCommonTypes:instrumentClusterTime>\r\n" \
                       f"   <rptCommonTypes:minute>30</rptCommonTypes:minute>\r\n" \
                       f"   <rptCommonTypes:timerActivationState>{self.timer3_state}</rptCommonTypes:timerActivationState>\r\n" \
                       f"   <rptCommonTypes:timerChargeOption>enabled</rptCommonTypes:timerChargeOption>\r\n" \
                       f"   <rptCommonTypes:timerClimaOption>disabled</rptCommonTypes:timerClimaOption>\r\n" \
                       f"   <rptCommonTypes:timerID>3</rptCommonTypes:timerID>\r\n" \
                       f"   <rptCommonTypes:weekdayBitmask>14</rptCommonTypes:weekdayBitmask>\r\n" \
                       f" </rptCommonTypes:timer>\r\n" \
                       f"\r\n" \
                       f" <!-- Lade-Serientimer 4 -->\r\n" \
                       f" <rptCommonTypes:timer>\r\n" \
                       f"   <rptCommonTypes:cycle>true</rptCommonTypes:cycle>\r\n" \
                       f"   <rptCommonTypes:hour>04</rptCommonTypes:hour>\r\n" \
                       f"   <rptCommonTypes:instrumentClusterTime>{self.timestamp_instrument_cluster}</rptCommonTypes:instrumentClusterTime>\r\n" \
                       f"   <rptCommonTypes:minute>40</rptCommonTypes:minute>\r\n" \
                       f"   <rptCommonTypes:timerActivationState>{self.timer4_state}</rptCommonTypes:timerActivationState>\r\n" \
                       f"   <rptCommonTypes:timerChargeOption>enabled</rptCommonTypes:timerChargeOption>\r\n" \
                       f"   <rptCommonTypes:timerClimaOption>disabled</rptCommonTypes:timerClimaOption>\r\n" \
                       f"   <rptCommonTypes:timerID>4</rptCommonTypes:timerID>\r\n" \
                       f"   <rptCommonTypes:weekdayBitmask>46</rptCommonTypes:weekdayBitmask>\r\n" \
                       f" </rptCommonTypes:timer>\r\n" \
                       f"\r\n" \
                       f" <!-- Lade-Serientimer 5 -->\r\n" \
                       f" <rptCommonTypes:timer>\r\n" \
                       f"   <rptCommonTypes:cycle>true</rptCommonTypes:cycle>\r\n" \
                       f"   <rptCommonTypes:hour>05</rptCommonTypes:hour>\r\n" \
                       f"   <rptCommonTypes:instrumentClusterTime>{self.timestamp_instrument_cluster}</rptCommonTypes:instrumentClusterTime>\r\n" \
                       f"   <rptCommonTypes:minute>50</rptCommonTypes:minute>\r\n" \
                       f"   <rptCommonTypes:timerActivationState>{self.timer5_state}</rptCommonTypes:timerActivationState>\r\n" \
                       f"   <rptCommonTypes:timerChargeOption>enabled</rptCommonTypes:timerChargeOption>\r\n" \
                       f"   <rptCommonTypes:timerClimaOption>disabled</rptCommonTypes:timerClimaOption>\r\n" \
                       f"   <rptCommonTypes:timerID>5</rptCommonTypes:timerID>\r\n" \
                       f"   <rptCommonTypes:weekdayBitmask>33</rptCommonTypes:weekdayBitmask>\r\n" \
                       f" </rptCommonTypes:timer>\r\n" \
                       f"\r\n" \
                       f" <!-- Klimatimer 6: Einzeltimer -->\r\n" \
                       f" <rptCommonTypes:timer>\r\n" \
                       f"   <!-- ElementSettings werden bei TimerID 6 mitgesendet und gelten allg. fuer alle Klimatimer -->\r\n" \
                       f"   <rptCommonTypes:cycle>false</rptCommonTypes:cycle>\r\n" \
                       f"   <rptCommonTypes:hour>16</rptCommonTypes:hour>\r\n" \
                       f"   <rptCommonTypes:instrumentClusterTime>{self.timestamp_instrument_cluster}</rptCommonTypes:instrumentClusterTime>\r\n" \
                       f"   <rptCommonTypes:minute>30</rptCommonTypes:minute>\r\n" \
                       f"   <rptCommonTypes:timerActivationState>{self.timer6_state}</rptCommonTypes:timerActivationState>\r\n" \
                       f"   <rptCommonTypes:timerChargeOption>disabled</rptCommonTypes:timerChargeOption>\r\n" \
                       f"   <rptCommonTypes:timerClimaOption>enabled</rptCommonTypes:timerClimaOption>\r\n" \
                       f"   <rptCommonTypes:timerDate>\r\n" \
                       f"     <rptCommonTypes:day></rptCommonTypes:day>\r\n" \
                       f"     <rptCommonTypes:month></rptCommonTypes:month>\r\n" \
                       f"     <rptCommonTypes:year></rptCommonTypes:year>\r\n" \
                       f"   </rptCommonTypes:timerDate>\r\n" \
                       f"   <rptCommonTypes:timerID>6</rptCommonTypes:timerID>\r\n" \
                       f"   <rptCommonTypes:timerTargetSOC>0</rptCommonTypes:timerTargetSOC>\r\n" \
                       f"   <rptCommonTypes:weekdayBitmask>96</rptCommonTypes:weekdayBitmask>\r\n" \
                       f" </rptCommonTypes:timer>\r\n" \
                       f"\r\n" \
                       f" <!-- Klimatimer 7: Einzeltimer   -->\r\n" \
                       f" <rptCommonTypes:timer>\r\n" \
                       f"   <rptCommonTypes:cycle>false</rptCommonTypes:cycle>\r\n" \
                       f"   <rptCommonTypes:hour>8</rptCommonTypes:hour>\r\n" \
                       f"   <rptCommonTypes:instrumentClusterTime>{self.timestamp_instrument_cluster}</rptCommonTypes:instrumentClusterTime>\r\n" \
                       f"   <rptCommonTypes:minute>00</rptCommonTypes:minute>\r\n" \
                       f"   <rptCommonTypes:timerActivationState>{self.timer7_state}</rptCommonTypes:timerActivationState>\r\n" \
                       f"   <rptCommonTypes:timerChargeOption>disabled</rptCommonTypes:timerChargeOption>\r\n" \
                       f"   <rptCommonTypes:timerClimaOption>enabled</rptCommonTypes:timerClimaOption>\r\n" \
                       f"   <rptCommonTypes:timerDate>\r\n" \
                       f"     <rptCommonTypes:day></rptCommonTypes:day>\r\n" \
                       f"     <rptCommonTypes:month></rptCommonTypes:month>\r\n" \
                       f"     <rptCommonTypes:year></rptCommonTypes:year>\r\n" \
                       f"   </rptCommonTypes:timerDate>\r\n" \
                       f"   <rptCommonTypes:timerID>7</rptCommonTypes:timerID>\r\n" \
                       f"   <rptCommonTypes:weekdayBitmask>96</rptCommonTypes:weekdayBitmask>\r\n" \
                       f" </rptCommonTypes:timer>\r\n" \
                       f"</rptTimerStateReport:rptTimerStateReport>"

        self.get_payload()

    def get_payload(self):
        """Get payload for RPT service.

        :rtype: str.
        :returns: Payload.
        """
        return self.payload
