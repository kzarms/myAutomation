# escape=\
#Get image
FROM mcr.microsoft.com/powershell
LABEL project="AzureAD"

#Install pester module 
SHELL [ "pwsh", "-Command", "$ErrorActionPreference = 'Stop'; $ProgressPreference = 'SilentlyContinue';" ]
RUN Install-Module pester -Force

#Set working dir with all tests inside
WORKDIR /test
ENTRYPOINT [ "pwsh", "-c", "Invoke-Pester", "-Strict", "-EnableExit" ]
