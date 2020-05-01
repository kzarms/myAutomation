# myAutomation
This is my personal repository.
Initial intention to save config setup for Ubuntu machines and Windows Machines i use

`
sudo python3 ubuntuSetup.py
`

## WorkWithPester and docker

Manual execution in AzureAD
`
docker build -t azuread/pester-runner .
docker run -it --rm -v ${pwd}:/test azuread/pester-runner
`

Run from docker-compose:
`
docker-compose up
docker-compose run --rm azuread

#Retur exit code
docker-compose up --exit-code-from azuread
`