# -*- coding: utf-8 -*-
"""Created on 10.05.2022.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.
Contains payload for RPT (Remote Profile and Timer Programming) service
"""
import datetime

from .. import interface


class Payload(interface.Payload):
    """ RPT (Remote Profile and Timer Programming) payload. """

    def __init__(self, **kwargs):
        """Initialize payload object for RPT service.

        :param kwargs: Arbitrary keyword arguments.
        """

        super().__init__()

        self.utc = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%S")
        self.timestamp_instrument_cluster = self.utc
        self.car_captured_utc_timestamp = (datetime.datetime.now(datetime.UTC) - datetime.timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%S")

        self.profile1_target_soc = 80
        self.profile2_target_soc = 80
        self.profile3_target_soc = 80
        self.profile4_target_soc = 80
        self.profile5_target_soc = 80
        self.profile6_target_soc = 80
        self.profile7_target_soc = 80

        self.activated_profile_id = "null"

        self.prepare_payload(**kwargs)
        self.payload = f"<rptProfileStateReport:rptProfileStateReport xmlns:rptCommonTypes=\"http://www.vw.com/mbb/rptCommonTypes\" \r\n" \
                       f"xmlns:rptProfileStateReport=\"http://www.vw.com/mbb/rptProfileStateReport\" \r\n" \
                       f"xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" \r\n" \
                       f"xsi:schemaLocation=\"http://www.vw.com/mbb/rptProfileStateReport ../../XSD_mbb/2018.2/GLCS/rptProfileStateReport_v1_0_2.xsd \">\r\n" \
                       f"<rptCommonTypes:carCapturedUTCTimestamp>{self.car_captured_utc_timestamp}</rptCommonTypes:carCapturedUTCTimestamp>\r\n" \
                       f"<rptCommonTypes:instrumentClusterTime>{self.timestamp_instrument_cluster}</rptCommonTypes:instrumentClusterTime>\r\n" \
                       f"<rptCommonTypes:privateCurrentState>available</rptCommonTypes:privateCurrentState>\r\n" \
                       f"\r\n" \
                       f"  <!-- Default-Profile 1 -->\r\n" \
                       f"  <!-- EDIT Target SOC Only !!!!!!! -->\r\n" \
                       f" <rptCommonTypes:profile>\r\n" \
                       f"   <rptCommonTypes:minSOC>2</rptCommonTypes:minSOC>\r\n" \
                       f"   <rptCommonTypes:powerLimitation>\r\n" \
                       f"     <rptCommonTypes:endHour>2</rptCommonTypes:endHour>\r\n" \
                       f"     <rptCommonTypes:endMinute>0</rptCommonTypes:endMinute>\r\n" \
                       f"     <rptCommonTypes:power>25100</rptCommonTypes:power>\r\n" \
                       f"     <rptCommonTypes:startHour>0</rptCommonTypes:startHour>\r\n" \
                       f"     <rptCommonTypes:startMinute>0</rptCommonTypes:startMinute>\r\n" \
                       f"   </rptCommonTypes:powerLimitation>\r\n" \
                       f"   <rptCommonTypes:preferredChargingTime>\r\n" \
                       f"     <rptCommonTypes:endHour>0</rptCommonTypes:endHour>\r\n" \
                       f"     <rptCommonTypes:endMinute>0</rptCommonTypes:endMinute>\r\n" \
                       f"     <rptCommonTypes:startHour>0</rptCommonTypes:startHour>\r\n" \
                       f"     <rptCommonTypes:startMinute>0</rptCommonTypes:startMinute>\r\n" \
                       f"   </rptCommonTypes:preferredChargingTime>\r\n" \
                       f"   <rptCommonTypes:profileActivation>true</rptCommonTypes:profileActivation>\r\n" \
                       f"   <rptCommonTypes:profileID>1</rptCommonTypes:profileID>\r\n" \
                       f"   <rptCommonTypes:profileName>Default</rptCommonTypes:profileName>\r\n" \
                       f"   <rptCommonTypes:profileOptions>\r\n" \
                       f"     <rptCommonTypes:autoPlugUnlockEnabled>false</rptCommonTypes:autoPlugUnlockEnabled>\r\n" \
                       f"     <rptCommonTypes:energyCostOptimisationEnabled>false</rptCommonTypes:energyCostOptimisationEnabled>\r\n" \
                       f"     <rptCommonTypes:energyMixOptimisationEnabled>false</rptCommonTypes:energyMixOptimisationEnabled>\r\n" \
                       f"     <rptCommonTypes:powerLimitationEnabled>false</rptCommonTypes:powerLimitationEnabled>\r\n" \
                       f"     <rptCommonTypes:preferredChargingEnabled>false</rptCommonTypes:preferredChargingEnabled>\r\n" \
                       f"     <rptCommonTypes:smartChargingEnabled>true</rptCommonTypes:smartChargingEnabled>\r\n" \
                       f"     <rptCommonTypes:timeBasedEnabled>false</rptCommonTypes:timeBasedEnabled>\r\n" \
                       f"     <rptCommonTypes:usePrivateCurrentEnabled>false</rptCommonTypes:usePrivateCurrentEnabled>\r\n" \
                       f"   </rptCommonTypes:profileOptions>\r\n" \
                       f"   <rptCommonTypes:profilePosition>\r\n" \
                       f"     <rptCommonTypes:profileLatitude>0</rptCommonTypes:profileLatitude>\r\n" \
                       f"     <rptCommonTypes:profileLongitude>0</rptCommonTypes:profileLongitude>\r\n" \
                       f"     <rptCommonTypes:profileRadius>100</rptCommonTypes:profileRadius>\r\n" \
                       f"     <rptCommonTypes:profileRadiusUnit>noUnit</rptCommonTypes:profileRadiusUnit>\r\n" \
                       f"   </rptCommonTypes:profilePosition>\r\n" \
                       f"   <!-- EDIT Target SOC Only !!!!!!! -->\r\n" \
                       f"   <rptCommonTypes:profileTargetSOC>{self.profile1_target_soc}</rptCommonTypes:profileTargetSOC>\r\n" \
                       f"   <rptCommonTypes:timerActionList>\r\n" \
                       f"     <rptCommonTypes:timerAction>1</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>2</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>3</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>4</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>5</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>6</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>7</rptCommonTypes:timerAction>\r\n" \
                       f"   </rptCommonTypes:timerActionList>\r\n" \
                       f" </rptCommonTypes:profile>\r\n" \
                       f"\r\n" \
                       f"  <!-- Customer Profile 2 --> \r\n" \
                       f"  <!-- EDIT only where it says!-->\r\n" \
                       f"\r\n" \
                       f"   <rptCommonTypes:profile>\r\n" \
                       f"   <rptCommonTypes:minSOC>25</rptCommonTypes:minSOC>                                           <!-- edit: 25 (= Audi set) or 2 (= Audi unset) -->\r\n" \
                       f"   <rptCommonTypes:powerLimitation>\r\n" \
                       f"     <rptCommonTypes:endHour>0</rptCommonTypes:endHour>\r\n" \
                       f"     <rptCommonTypes:endMinute>0</rptCommonTypes:endMinute>\r\n" \
                       f"     <rptCommonTypes:power>25100</rptCommonTypes:power>\r\n" \
                       f"     <rptCommonTypes:startHour>0</rptCommonTypes:startHour>\r\n" \
                       f"     <rptCommonTypes:startMinute>0</rptCommonTypes:startMinute>\r\n" \
                       f"   </rptCommonTypes:powerLimitation>\r\n" \
                       f"   <rptCommonTypes:preferredChargingTime> \r\n" \
                       f"     <rptCommonTypes:endHour>0</rptCommonTypes:endHour>                                        <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:endMinute>0</rptCommonTypes:endMinute>                                    <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:startHour>0</rptCommonTypes:startHour>                                    <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:startMinute>0</rptCommonTypes:startMinute>                                <!-- edit: -->\r\n" \
                       f"   </rptCommonTypes:preferredChargingTime>\r\n" \
                       f"   <rptCommonTypes:profileActivation>true</rptCommonTypes:profileActivation>\r\n" \
                       f"   <rptCommonTypes:profileID>2</rptCommonTypes:profileID>                                      <!-- edit: -->\r\n" \
                       f"   <rptCommonTypes:profileName>IngArbeit</rptCommonTypes:profileName>                          <!-- edit: -->\r\n" \
                       f"   <rptCommonTypes:profileOptions>\r\n" \
                       f"     <rptCommonTypes:autoPlugUnlockEnabled>true</rptCommonTypes:autoPlugUnlockEnabled>\r\n" \
                       f"     <rptCommonTypes:energyCostOptimisationEnabled>true</rptCommonTypes:energyCostOptimisationEnabled>\r\n" \
                       f"     <rptCommonTypes:energyMixOptimisationEnabled>true</rptCommonTypes:energyMixOptimisationEnabled>\r\n" \
                       f"     <rptCommonTypes:powerLimitationEnabled>true</rptCommonTypes:powerLimitationEnabled>\r\n" \
                       f"     <rptCommonTypes:preferredChargingEnabled>true</rptCommonTypes:preferredChargingEnabled>   <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:smartChargingEnabled>true</rptCommonTypes:smartChargingEnabled>\r\n" \
                       f"     <rptCommonTypes:timeBasedEnabled>true</rptCommonTypes:timeBasedEnabled>\r\n" \
                       f"     <rptCommonTypes:usePrivateCurrentEnabled>true</rptCommonTypes:usePrivateCurrentEnabled>\r\n" \
                       f"   </rptCommonTypes:profileOptions>\r\n" \
                       f"   <rptCommonTypes:profilePosition>\r\n" \
                       f"     <rptCommonTypes:profileLatitude>48793656</rptCommonTypes:profileLatitude>                 <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:profileLongitude>11407060</rptCommonTypes:profileLongitude>               <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:profileRadius>100</rptCommonTypes:profileRadius>\r\n" \
                       f"     <rptCommonTypes:profileRadiusUnit>invalid</rptCommonTypes:profileRadiusUnit>\r\n" \
                       f"   </rptCommonTypes:profilePosition>\r\n" \
                       f"   <rptCommonTypes:profileTargetSOC>{self.profile2_target_soc}</rptCommonTypes:profileTargetSOC> <!-- edit: -->\r\n" \
                       f"   <rptCommonTypes:timerActionList>\r\n" \
                       f"     <rptCommonTypes:timerActionList>\r\n" \
                       f"     <rptCommonTypes:timerAction>1</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>2</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>3</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>4</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>5</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>6</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>7</rptCommonTypes:timerAction>\r\n" \
                       f"   </rptCommonTypes:timerActionList>\r\n" \
                       f"   </rptCommonTypes:timerActionList>\r\n" \
                       f" </rptCommonTypes:profile>\r\n" \
                       f"\r\n" \
                       f"  <!-- Customer Profile 3 --> \r\n" \
                       f"  <!-- EDIT only where it says!-->\r\n" \
                       f"\r\n" \
                       f"   <rptCommonTypes:profile>\r\n" \
                       f"   <rptCommonTypes:minSOC>2</rptCommonTypes:minSOC>                                            <!-- edit: 25 (= Audi set) or 2 (= Audi unset) -->\r\n" \
                       f"   <rptCommonTypes:powerLimitation>\r\n" \
                       f"     <rptCommonTypes:endHour>0</rptCommonTypes:endHour>\r\n" \
                       f"     <rptCommonTypes:endMinute>0</rptCommonTypes:endMinute>\r\n" \
                       f"     <rptCommonTypes:power>25100</rptCommonTypes:power>\r\n" \
                       f"     <rptCommonTypes:startHour>0</rptCommonTypes:startHour>\r\n" \
                       f"     <rptCommonTypes:startMinute>0</rptCommonTypes:startMinute>\r\n" \
                       f"   </rptCommonTypes:powerLimitation>\r\n" \
                       f"   <rptCommonTypes:preferredChargingTime> \r\n" \
                       f"     <rptCommonTypes:endHour>0</rptCommonTypes:endHour>                                        <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:endMinute>0</rptCommonTypes:endMinute>                                    <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:startHour>0</rptCommonTypes:startHour>                                    <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:startMinute>0</rptCommonTypes:startMinute>                                <!-- edit: -->\r\n" \
                       f"   </rptCommonTypes:preferredChargingTime>\r\n" \
                       f"   <rptCommonTypes:profileActivation>true</rptCommonTypes:profileActivation>\r\n" \
                       f"   <rptCommonTypes:profileID>3</rptCommonTypes:profileID>                                      <!-- edit: -->\r\n" \
                       f"   <rptCommonTypes:profileName>IngHauptbahnhof</rptCommonTypes:profileName>                    <!-- edit: -->\r\n" \
                       f"   <rptCommonTypes:profileOptions>\r\n" \
                       f"     <rptCommonTypes:autoPlugUnlockEnabled>true</rptCommonTypes:autoPlugUnlockEnabled>\r\n" \
                       f"     <rptCommonTypes:energyCostOptimisationEnabled>true</rptCommonTypes:energyCostOptimisationEnabled>\r\n" \
                       f"     <rptCommonTypes:energyMixOptimisationEnabled>true</rptCommonTypes:energyMixOptimisationEnabled>\r\n" \
                       f"     <rptCommonTypes:powerLimitationEnabled>true</rptCommonTypes:powerLimitationEnabled>\r\n" \
                       f"     <rptCommonTypes:preferredChargingEnabled>true</rptCommonTypes:preferredChargingEnabled>   <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:smartChargingEnabled>true</rptCommonTypes:smartChargingEnabled>\r\n" \
                       f"     <rptCommonTypes:timeBasedEnabled>true</rptCommonTypes:timeBasedEnabled>\r\n" \
                       f"     <rptCommonTypes:usePrivateCurrentEnabled>true</rptCommonTypes:usePrivateCurrentEnabled>\r\n" \
                       f"   </rptCommonTypes:profileOptions>\r\n" \
                       f"   <rptCommonTypes:profilePosition>\r\n" \
                       f"     <rptCommonTypes:profileLatitude>48743019</rptCommonTypes:profileLatitude>                 <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:profileLongitude>11437349</rptCommonTypes:profileLongitude>               <!-- edit: -->  \r\n" \
                       f"     <rptCommonTypes:profileRadius>100</rptCommonTypes:profileRadius>\r\n" \
                       f"     <rptCommonTypes:profileRadiusUnit>invalid</rptCommonTypes:profileRadiusUnit>\r\n" \
                       f"   </rptCommonTypes:profilePosition>\r\n" \
                       f"   <rptCommonTypes:profileTargetSOC>{self.profile3_target_soc}</rptCommonTypes:profileTargetSOC> <!-- edit: -->\r\n" \
                       f"   <rptCommonTypes:timerActionList>\r\n" \
                       f"     <rptCommonTypes:timerActionList>\r\n" \
                       f"     <rptCommonTypes:timerAction>1</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>2</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>3</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>4</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>5</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>6</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>7</rptCommonTypes:timerAction>\r\n" \
                       f"   </rptCommonTypes:timerActionList>\r\n" \
                       f"   </rptCommonTypes:timerActionList>\r\n" \
                       f" </rptCommonTypes:profile>\r\n" \
                       f"\r\n" \
                       f"  <!-- Customer Profile 4 --> \r\n" \
                       f"  <!-- EDIT only where it says!-->\r\n" \
                       f"\r\n" \
                       f"   <rptCommonTypes:profile>\r\n" \
                       f"   <rptCommonTypes:minSOC>15</rptCommonTypes:minSOC>                                           <!-- edit: 25 (= Audi set) or 2 (= Audi unset) -->\r\n" \
                       f"   <rptCommonTypes:powerLimitation>\r\n" \
                       f"     <rptCommonTypes:endHour>0</rptCommonTypes:endHour>\r\n" \
                       f"     <rptCommonTypes:endMinute>0</rptCommonTypes:endMinute>\r\n" \
                       f"     <rptCommonTypes:power>25100</rptCommonTypes:power>\r\n" \
                       f"     <rptCommonTypes:startHour>0</rptCommonTypes:startHour>\r\n" \
                       f"     <rptCommonTypes:startMinute>0</rptCommonTypes:startMinute>\r\n" \
                       f"   </rptCommonTypes:powerLimitation>\r\n" \
                       f"   <rptCommonTypes:preferredChargingTime> \r\n" \
                       f"     <rptCommonTypes:endHour>0</rptCommonTypes:endHour>                                        <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:endMinute>0</rptCommonTypes:endMinute>                                    <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:startHour>0</rptCommonTypes:startHour>                                    <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:startMinute>0</rptCommonTypes:startMinute>                                <!-- edit: -->\r\n" \
                       f"   </rptCommonTypes:preferredChargingTime>\r\n" \
                       f"   <rptCommonTypes:profileActivation>true</rptCommonTypes:profileActivation>\r\n" \
                       f"   <rptCommonTypes:profileID>4</rptCommonTypes:profileID>                                      <!-- edit: -->\r\n" \
                       f"   <rptCommonTypes:profileName>zuHause_Vohburg</rptCommonTypes:profileName>                    <!-- edit: -->\r\n" \
                       f"   <rptCommonTypes:profileOptions>\r\n" \
                       f"     <rptCommonTypes:autoPlugUnlockEnabled>true</rptCommonTypes:autoPlugUnlockEnabled>\r\n" \
                       f"     <rptCommonTypes:energyCostOptimisationEnabled>true</rptCommonTypes:energyCostOptimisationEnabled>\r\n" \
                       f"     <rptCommonTypes:energyMixOptimisationEnabled>true</rptCommonTypes:energyMixOptimisationEnabled>\r\n" \
                       f"     <rptCommonTypes:powerLimitationEnabled>true</rptCommonTypes:powerLimitationEnabled>\r\n" \
                       f"     <rptCommonTypes:preferredChargingEnabled>true</rptCommonTypes:preferredChargingEnabled>   <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:smartChargingEnabled>true</rptCommonTypes:smartChargingEnabled>\r\n" \
                       f"     <rptCommonTypes:timeBasedEnabled>true</rptCommonTypes:timeBasedEnabled>\r\n" \
                       f"     <rptCommonTypes:usePrivateCurrentEnabled>true</rptCommonTypes:usePrivateCurrentEnabled>\r\n" \
                       f"   </rptCommonTypes:profileOptions>\r\n" \
                       f"   <rptCommonTypes:profilePosition>\r\n" \
                       f"     <rptCommonTypes:profileLatitude>48768399</rptCommonTypes:profileLatitude>                 <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:profileLongitude>11618159</rptCommonTypes:profileLongitude>               <!-- edit: --> \r\n" \
                       f"     <rptCommonTypes:profileRadius>100</rptCommonTypes:profileRadius>\r\n" \
                       f"     <rptCommonTypes:profileRadiusUnit>invalid</rptCommonTypes:profileRadiusUnit>\r\n" \
                       f"   </rptCommonTypes:profilePosition>\r\n" \
                       f"   <rptCommonTypes:profileTargetSOC>{self.profile4_target_soc}</rptCommonTypes:profileTargetSOC> <!-- edit: -->\r\n" \
                       f"   <rptCommonTypes:timerActionList>\r\n" \
                       f"     <rptCommonTypes:timerActionList>\r\n" \
                       f"     <rptCommonTypes:timerAction>1</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>2</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>3</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>4</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>5</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>6</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>7</rptCommonTypes:timerAction>\r\n" \
                       f"   </rptCommonTypes:timerActionList>\r\n" \
                       f"   </rptCommonTypes:timerActionList>\r\n" \
                       f" </rptCommonTypes:profile>\r\n" \
                       f"\r\n" \
                       f"  <!-- Customer Profile 5 --> \r\n" \
                       f"  <!-- EDIT only where it says!-->\r\n" \
                       f"\r\n" \
                       f"   <rptCommonTypes:profile>\r\n" \
                       f"   <rptCommonTypes:minSOC>35</rptCommonTypes:minSOC>                                           <!-- edit: 25 (= Audi set) or 2 (= Audi unset) -->\r\n" \
                       f"   <rptCommonTypes:powerLimitation>\r\n" \
                       f"     <rptCommonTypes:endHour>0</rptCommonTypes:endHour>\r\n" \
                       f"     <rptCommonTypes:endMinute>0</rptCommonTypes:endMinute>\r\n" \
                       f"     <rptCommonTypes:power>25100</rptCommonTypes:power>\r\n" \
                       f"     <rptCommonTypes:startHour>0</rptCommonTypes:startHour>\r\n" \
                       f"     <rptCommonTypes:startMinute>0</rptCommonTypes:startMinute>\r\n" \
                       f"   </rptCommonTypes:powerLimitation>\r\n" \
                       f"   <rptCommonTypes:preferredChargingTime> \r\n" \
                       f"     <rptCommonTypes:endHour>0</rptCommonTypes:endHour>                                        <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:endMinute>0</rptCommonTypes:endMinute>                                    <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:startHour>0</rptCommonTypes:startHour>                                    <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:startMinute>0</rptCommonTypes:startMinute>                                <!-- edit: -->\r\n" \
                       f"   </rptCommonTypes:preferredChargingTime>\r\n" \
                       f"   <rptCommonTypes:profileActivation>true</rptCommonTypes:profileActivation>\r\n" \
                       f"   <rptCommonTypes:profileID>5</rptCommonTypes:profileID>                                      <!-- edit: -->\r\n" \
                       f"   <rptCommonTypes:profileName>Muc_QuartettMobile</rptCommonTypes:profileName>                 <!-- edit: -->\r\n" \
                       f"   <rptCommonTypes:profileOptions>\r\n" \
                       f"     <rptCommonTypes:autoPlugUnlockEnabled>true</rptCommonTypes:autoPlugUnlockEnabled>\r\n" \
                       f"     <rptCommonTypes:energyCostOptimisationEnabled>true</rptCommonTypes:energyCostOptimisationEnabled>\r\n" \
                       f"     <rptCommonTypes:energyMixOptimisationEnabled>true</rptCommonTypes:energyMixOptimisationEnabled>\r\n" \
                       f"     <rptCommonTypes:powerLimitationEnabled>true</rptCommonTypes:powerLimitationEnabled>\r\n" \
                       f"     <rptCommonTypes:preferredChargingEnabled>true</rptCommonTypes:preferredChargingEnabled>   <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:smartChargingEnabled>true</rptCommonTypes:smartChargingEnabled>\r\n" \
                       f"     <rptCommonTypes:timeBasedEnabled>true</rptCommonTypes:timeBasedEnabled>\r\n" \
                       f"     <rptCommonTypes:usePrivateCurrentEnabled>true</rptCommonTypes:usePrivateCurrentEnabled>\r\n" \
                       f"   </rptCommonTypes:profileOptions>\r\n" \
                       f"   <rptCommonTypes:profilePosition>\r\n" \
                       f"     <rptCommonTypes:profileLatitude>48179009</rptCommonTypes:profileLatitude>                 <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:profileLongitude>11595463</rptCommonTypes:profileLongitude>               <!-- edit: -->  \r\n" \
                       f"     <rptCommonTypes:profileRadius>100</rptCommonTypes:profileRadius>\r\n" \
                       f"     <rptCommonTypes:profileRadiusUnit>invalid</rptCommonTypes:profileRadiusUnit>\r\n" \
                       f"   </rptCommonTypes:profilePosition>\r\n" \
                       f"   <rptCommonTypes:profileTargetSOC>{self.profile5_target_soc}</rptCommonTypes:profileTargetSOC> <!-- edit: -->\r\n" \
                       f"   <rptCommonTypes:timerActionList>\r\n" \
                       f"     <rptCommonTypes:timerActionList>\r\n" \
                       f"     <rptCommonTypes:timerAction>1</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>2</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>3</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>4</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>5</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>6</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>7</rptCommonTypes:timerAction>\r\n" \
                       f"   </rptCommonTypes:timerActionList>\r\n" \
                       f"   </rptCommonTypes:timerActionList>\r\n" \
                       f" </rptCommonTypes:profile>\r\n" \
                       f"\r\n" \
                       f"  <!-- Customer Profile 6 --> \r\n" \
                       f"  <!-- EDIT only where it says!-->\r\n" \
                       f"\r\n" \
                       f"   <rptCommonTypes:profile>\r\n" \
                       f"   <rptCommonTypes:minSOC>25</rptCommonTypes:minSOC>                                           <!-- edit: 25 (= Audi set) or 2 (= Audi unset) -->\r\n" \
                       f"   <rptCommonTypes:powerLimitation>\r\n" \
                       f"     <rptCommonTypes:endHour>0</rptCommonTypes:endHour>\r\n" \
                       f"     <rptCommonTypes:endMinute>0</rptCommonTypes:endMinute>\r\n" \
                       f"     <rptCommonTypes:power>25100</rptCommonTypes:power>\r\n" \
                       f"     <rptCommonTypes:startHour>0</rptCommonTypes:startHour>\r\n" \
                       f"     <rptCommonTypes:startMinute>0</rptCommonTypes:startMinute>\r\n" \
                       f"   </rptCommonTypes:powerLimitation>\r\n" \
                       f"   <rptCommonTypes:preferredChargingTime> \r\n" \
                       f"     <rptCommonTypes:endHour>0</rptCommonTypes:endHour>                                        <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:endMinute>0</rptCommonTypes:endMinute>                                    <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:startHour>0</rptCommonTypes:startHour>                                    <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:startMinute>0</rptCommonTypes:startMinute>                                <!-- edit: -->\r\n" \
                       f"   </rptCommonTypes:preferredChargingTime>\r\n" \
                       f"   <rptCommonTypes:profileActivation>true</rptCommonTypes:profileActivation>\r\n" \
                       f"   <rptCommonTypes:profileID>6</rptCommonTypes:profileID>                                      <!-- edit: -->\r\n" \
                       f"   <rptCommonTypes:profileName>IngAudiForum</rptCommonTypes:profileName>                       <!-- edit: -->\r\n" \
                       f"   <rptCommonTypes:profileOptions>\r\n" \
                       f"     <rptCommonTypes:autoPlugUnlockEnabled>true</rptCommonTypes:autoPlugUnlockEnabled>\r\n" \
                       f"     <rptCommonTypes:energyCostOptimisationEnabled>true</rptCommonTypes:energyCostOptimisationEnabled>\r\n" \
                       f"     <rptCommonTypes:energyMixOptimisationEnabled>true</rptCommonTypes:energyMixOptimisationEnabled>\r\n" \
                       f"     <rptCommonTypes:powerLimitationEnabled>true</rptCommonTypes:powerLimitationEnabled>\r\n" \
                       f"     <rptCommonTypes:preferredChargingEnabled>true</rptCommonTypes:preferredChargingEnabled>   <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:smartChargingEnabled>true</rptCommonTypes:smartChargingEnabled>\r\n" \
                       f"     <rptCommonTypes:timeBasedEnabled>true</rptCommonTypes:timeBasedEnabled>\r\n" \
                       f"     <rptCommonTypes:usePrivateCurrentEnabled>true</rptCommonTypes:usePrivateCurrentEnabled>\r\n" \
                       f"   </rptCommonTypes:profileOptions>\r\n" \
                       f"   <rptCommonTypes:profilePosition>\r\n" \
                       f"     <rptCommonTypes:profileLatitude>48782661</rptCommonTypes:profileLatitude>                 <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:profileLongitude>11413723</rptCommonTypes:profileLongitude>               <!-- edit: -->  \r\n" \
                       f"     <rptCommonTypes:profileRadius>100</rptCommonTypes:profileRadius>\r\n" \
                       f"     <rptCommonTypes:profileRadiusUnit>invalid</rptCommonTypes:profileRadiusUnit>\r\n" \
                       f"   </rptCommonTypes:profilePosition>\r\n" \
                       f"   <rptCommonTypes:profileTargetSOC>{self.profile6_target_soc}</rptCommonTypes:profileTargetSOC> <!-- edit: -->\r\n" \
                       f"   <rptCommonTypes:timerActionList>\r\n" \
                       f"     <rptCommonTypes:timerActionList>\r\n" \
                       f"     <rptCommonTypes:timerAction>1</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>2</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>3</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>4</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>5</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>6</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>7</rptCommonTypes:timerAction>\r\n" \
                       f"   </rptCommonTypes:timerActionList>\r\n" \
                       f"   </rptCommonTypes:timerActionList>\r\n" \
                       f" </rptCommonTypes:profile>\r\n" \
                       f"\r\n" \
                       f"  <!-- Customer Profile 7 --> \r\n" \
                       f"  <!-- EDIT only where it says!-->\r\n" \
                       f"\r\n" \
                       f"   <rptCommonTypes:profile>\r\n" \
                       f"   <rptCommonTypes:minSOC>25</rptCommonTypes:minSOC>                                           <!-- edit: 25 (= Audi set) or 2 (= Audi unset) -->\r\n" \
                       f"   <rptCommonTypes:powerLimitation>\r\n" \
                       f"     <rptCommonTypes:endHour>0</rptCommonTypes:endHour>\r\n" \
                       f"     <rptCommonTypes:endMinute>0</rptCommonTypes:endMinute>\r\n" \
                       f"     <rptCommonTypes:power>25100</rptCommonTypes:power>\r\n" \
                       f"     <rptCommonTypes:startHour>0</rptCommonTypes:startHour>\r\n" \
                       f"     <rptCommonTypes:startMinute>0</rptCommonTypes:startMinute>\r\n" \
                       f"   </rptCommonTypes:powerLimitation>\r\n" \
                       f"   <rptCommonTypes:preferredChargingTime> \r\n" \
                       f"     <rptCommonTypes:endHour>7</rptCommonTypes:endHour>                                        <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:endMinute>0</rptCommonTypes:endMinute>                                    <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:startHour>5</rptCommonTypes:startHour>                                    <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:startMinute>0</rptCommonTypes:startMinute>                                <!-- edit: -->\r\n" \
                       f"   </rptCommonTypes:preferredChargingTime>\r\n" \
                       f"   <rptCommonTypes:profileActivation>true</rptCommonTypes:profileActivation>\r\n" \
                       f"   <rptCommonTypes:profileID>7</rptCommonTypes:profileID>                                      <!-- edit: -->\r\n" \
                       f"   <rptCommonTypes:profileName>Eichstaett_Uni-rb</rptCommonTypes:profileName>                  <!-- edit: -->\r\n" \
                       f"   <rptCommonTypes:profileOptions>\r\n" \
                       f"     <rptCommonTypes:autoPlugUnlockEnabled>true</rptCommonTypes:autoPlugUnlockEnabled>\r\n" \
                       f"     <rptCommonTypes:energyCostOptimisationEnabled>true</rptCommonTypes:energyCostOptimisationEnabled>\r\n" \
                       f"     <rptCommonTypes:energyMixOptimisationEnabled>true</rptCommonTypes:energyMixOptimisationEnabled>\r\n" \
                       f"     <rptCommonTypes:powerLimitationEnabled>true</rptCommonTypes:powerLimitationEnabled>\r\n" \
                       f"     <rptCommonTypes:preferredChargingEnabled>true</rptCommonTypes:preferredChargingEnabled>   <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:smartChargingEnabled>true</rptCommonTypes:smartChargingEnabled>\r\n" \
                       f"     <rptCommonTypes:timeBasedEnabled>true</rptCommonTypes:timeBasedEnabled>\r\n" \
                       f"     <rptCommonTypes:usePrivateCurrentEnabled>true</rptCommonTypes:usePrivateCurrentEnabled>\r\n" \
                       f"   </rptCommonTypes:profileOptions>\r\n" \
                       f"   <rptCommonTypes:profilePosition>\r\n" \
                       f"     <rptCommonTypes:profileLatitude>48888801</rptCommonTypes:profileLatitude>                 <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:profileLongitude>11190069</rptCommonTypes:profileLongitude>               <!-- edit: -->\r\n" \
                       f"     <rptCommonTypes:profileRadius>100</rptCommonTypes:profileRadius>\r\n" \
                       f"     <rptCommonTypes:profileRadiusUnit>invalid</rptCommonTypes:profileRadiusUnit>\r\n" \
                       f"   </rptCommonTypes:profilePosition>\r\n" \
                       f"   <rptCommonTypes:profileTargetSOC>{self.profile7_target_soc}</rptCommonTypes:profileTargetSOC> <!-- edit: -->\r\n" \
                       f"   <rptCommonTypes:timerActionList>\r\n" \
                       f"     <rptCommonTypes:timerActionList>\r\n" \
                       f"     <rptCommonTypes:timerAction>1</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>2</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>3</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>4</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>5</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>6</rptCommonTypes:timerAction>\r\n" \
                       f"     <rptCommonTypes:timerAction>7</rptCommonTypes:timerAction>\r\n" \
                       f"   </rptCommonTypes:timerActionList>\r\n" \
                       f"   </rptCommonTypes:timerActionList>\r\n" \
                       f" </rptCommonTypes:profile>\r\n" \
                       f"\r\n" \
                       f"  <!-- Customer Profile 8 --> \r\n" \
                       f"  <!-- EDIT only where it says!-->  \r\n" \
                       f"\r\n" \
                       f"  <!-- EDIT: Set active Profile here! -->\r\n" \
                       f" <rptCommonTypes:profileActivationState>{self.activated_profile_id}</rptCommonTypes:profileActivationState>\r\n" \
                       f" <rptCommonTypes:smartChargingState>available</rptCommonTypes:smartChargingState>\r\n" \
                       f"</rptProfileStateReport:rptProfileStateReport>\r\n" \

        self.get_payload()

    def get_payload(self):
        """Get payload for RPT service.

        :rtype: str.
        :returns: Payload.
        """
        return self.payload
