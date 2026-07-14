# Quick Start

---

## Installation

The Keyword-Driven-Testing project has follow dependencies:
1. Install Python Version 3.13.x   https://www.python.org/downloads/
2. Install mosquitto broker
3. Install all site-packages from file ./requirements.txt  
4. Uninstall standard enna_hcp_configuration. Is neccessary to you can use local variant.
> Example Powershell
>```powershell
>pip install -r ./enna_kwd_testing/requirements.txt
>pip uninstall enna_hcp_configuration
>````

Read also ENNA documentation - https://pages.git.hub.vwgroup.com/TA/enna/latest/getting_started/

---

## Execution

1. Start mossquitto broker on your computer 

2. If you run test automation.   
You must set environment variables:  
    ENNA_HCP_CONFIG_PATH = "./enna_kwd_testing/config"  
    TestCubeName = "Name of your own bench"
More information under: https://pages.git.hub.vwgroup.com/TA/enna/latest/handbook/core/configuration/

3. Folder of control files exist.
4. Start .enna_kwd_testing/enna_kwd_testing/runner/start_campaign_connect_apps

> Example Powershell:
>```powershell
>$Env:PYTHONPATH = "./enna_kwd_testing;./enna_hcp_configuration"
>$Env:ENNA_CONFIG_PATH = "./enna_kwd_testing/config"
>$Env:TestCubeName = "common"
>python -m enna_kwd_testing.runner.start_campaign_connect_apps --testcycle_path .\test_cases\<cluster>\<component>
>```
> Example Yaml:
> ```yaml
>    - script: |  
>        cd $(Build.Repository.LocalPath)
>        python -m enna_kwd_testing.enna_kwd_testing.runner.start_campaign_connect_appsm --testcycle_path $(path_to_order)${{parameters.folder}} 
>      displayName: 'Run tests'
>      env:
         PYTHONPATH: $(Build.Repository.LocalPath)\enna_kwd_testing;$(Build.Repository.LocalPath)\enna_hcp_configuration
>        ENNA_CONFIG_PATH: $(Build.Repository.LocalPath)\config
>        TestCubeName: $(${{parameters.agent}})
>```
