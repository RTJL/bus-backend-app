#!/bin/bash
source .venv/bin/activate
pip install -r requirements.txt
npm install
docker pull redis:6.0.9
docker start bus-backend-app-redis || docker run --name bus-backend-app-redis -p 6379:6379 -d redis:6.0.9
sls offline start --stage local --runSchedulesOnInit