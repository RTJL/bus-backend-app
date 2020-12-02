# Bus Arrival Backend App
Backend serverless application that fetches the respective bus arrival information. Built using Serverless Framework and deployed on AWS Lambda + API Gateway.

## Getting started
- Setup local dev env
- Run local dev server

### Setup local dev env

1. Create and activate python virtual environment

    `python3 -m venv .venv`

2. Create your own `.envrc` config file

    `cp .envrc.template .envrc`

3. Replace the API key(REPLACE_WITH_YOUR_KEY) with your own

    `export LTA_ACCOUNT_KEY=REPLACE_WITH_YOUR_KEY`

4. Grant direnv permissions and re-enter the directory 

    `direnv allow`
    `cd ..`
    `cd bus-backend-app`

### Run local dev server

Start local dev server using serverless
    
    `sls offline start --stage local --runSchedulesOnInit`
