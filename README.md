# Bus Arrival Backend App
Backend serverless application that fetches the respective bus arrival information. Built using Serverless Framework and deployed on AWS Lambda + API Gateway.

## Getting started
- Setup local dev env
- Run local dev server
- Deployment

### Setup local dev env

1. Create python virtual environment

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

### Deployment

  Create and push tags (vX.X.X)

  Example

  `git tag v0.1.0`

  `git push origin --tags`

## Endpoints
- /api/buses
- /api/bus-stops
- /api/arrival/{bus-stop-code}

### /api/buses

Returns an array of bus services

Method: GET

Example response
```json
{
  "buses": [
    {
      "ServiceNo": "118",
      "Operator": "GAS",
      "Direction": 1,
      "Category": "TRUNK",
      "OriginCode": "65009",
      "DestinationCode": "97009",
      "AM_Peak_Freq": "5-08",
      "AM_Offpeak_Freq": "8-12",
      "PM_Peak_Freq": "8-10",
      "PM_Offpeak_Freq": "09-14",
      "LoopDesc": ""
    },
    ...,
    {
      "ServiceNo": "118",
      "Operator": "GAS",
      "Direction": 2,
      "Category": "TRUNK",
      "OriginCode": "97009",
      "DestinationCode": "65009",
      "AM_Peak_Freq": "10-10",
      "AM_Offpeak_Freq": "8-11",
      "PM_Peak_Freq": "4-08",
      "PM_Offpeak_Freq": "9-12",
      "LoopDesc": ""
    }
  ]
}
```

### /api/buses

Returns an array of bus stops.

Method: GET

Example response:
```json
{
  "busStops": [
    {
      "BusStopCode": "01012",
      "RoadName": "Victoria St",
      "Description": "Hotel Grand Pacific",
      "Latitude": 1.29684825487647,
      "Longitude": 103.85253591654006
    },
    {
      "BusStopCode": "01013",
      "RoadName": "Victoria St",
      "Description": "St. Joseph's Ch",
      "Latitude": 1.29770970610083,
      "Longitude": 103.8532247463225
    }
  ]
}
```
### /api/arrival/{bus-stop-code}

Returns an array of bus services and its estimated arrival time for a bus stop.

Method: GET

URL Param: Bus stop code, 5 digit number

Example response:
```json
{
  "services": [
    {
      "ServiceNo": "117",
      "Operator": "SBST",
      "NextBus": {
        "OriginCode": "65009",
        "DestinationCode": "58009",
        "EstimatedArrival": "2020-12-02T12:54:12+08:00",
        "Latitude": "1.4100626666666667",
        "Longitude": "103.8299775",
        "VisitNumber": "1",
        "Load": "SEA",
        "Feature": "WAB",
        "Type": "DD"
      },
      "NextBus2": {
        ...
      },
      "NextBus3": {
        ...
      }
    },
    {
      "ServiceNo": "39",
      "Operator": "SBST",
      "NextBus": {
        ...
      },
      "NextBus2": {
        ...
      },
      "NextBus3": {
        "OriginCode": "",
        "DestinationCode": "",
        "EstimatedArrival": "",
        "Latitude": "",
        "Longitude": "",
        "VisitNumber": "",
        "Load": "",
        "Feature": "",
        "Type": ""
      }
    }
  ]
}
```