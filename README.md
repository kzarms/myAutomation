# myAutomation
This is my personal repository.

Initial intention to save config setup for Ubuntu machines and Windows Machines

## Ubuntu

```
sudo python3 ubuntuSetup.py
```

## AzureAD
[![Actions Status](https://github.com/kzarms/myAutomation/workflows/AzureAD/badge.svg)](https://github.com/kzarms/myAutomation/actions)
This module is for user creation in AzureAD.

Manual code check
```
Invoke-ScriptAnalyzer -Path AzureAD/ -ReportSummary
Invoke-Pester -Script AzureAD/
```


Support, docker execution with powerhsell 7

```
docker build -t azuread/pester-runner .
docker run -it --rm -v ${pwd}:/test azuread/pester-runner
```

Run from docker-compose:

```
docker-compose up
docker-compose run --rm azuread

#Retur exit code
docker-compose up --exit-code-from azuread
```