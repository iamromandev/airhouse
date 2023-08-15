**AirHouse** is a data integration project that involves extracting data from **csv** source,
transforming it into desired format, and loading it into our **postress** destination
[`data warehouse`]. It has its own API service for reporting the warehouse data.

####

**AirHouse** is built on open source `AirByte` for _ETL_ process and `FastAPI` for Reporting API service.

## Tools

1. `Docker Engine:` local deployment
2. `AirByte:` ETL process
3. `FastAPI:` web framework for reporting service
4. `Pydantic:` data validation library
5. `SQLModel:` to interact with databases
6. `pylint + mypy + black:` code analyser, type checker and code formatter

## Installation + Deployment

#### Docker Engine

Follow installation docs - https://docs.docker.com/engine/install/

#### AirHouse

1. git clone https://github.com/iamromandev/airhouse.git
2. run `cd airhouse`
3. run `make start` _for data warehouse and reporting api service_
4. run `cd airbyte`
5. run `./run-ab-platform.sh` _for ETL process_

### Configure ETL process

Open http://localhost:8000 on browser

#### Source
1. Go to `Sources`
2. Check [ ] `Alpha`
3. Search for `CSV`
4. Select `File (CSV, JSON, Excel, Feather, Parquet)`
5. Source name: `CSV Source` (as per project requirement)
6. Dataset Name: `csvdata` (will create table in data warehouse)
7. URL: `https://storage.googleapis.com/covid19-open-data/v2/latest/epidemiology.csv`
8. Click on `Set up source` (repeat if failed first time)

#### Destination
1. Go to `Destinations`
2. Check [ ] `Alpha`
3. Search for `Postgres`
4. Select `Postgres`
5. Destination name: `Postgres Destination` (as per project requirement)
6. Host: `host.docker.internal`
7. Port: `5430`
8. DB Name: `airhouse`
9. User: `airhouse`
10. Optional fields -> Password: `airhouse`
11. Click on `Set up destination` (repeat if failed first time)

#### Connection
1. Go to `Connections`
2. Click on `Create your first connection`
3. Select an existing source > Select `CSV Source`
4. Select an existing destination > Select `Postgres Destination`
5. Configuration > Replication frequency: `Manual`
6. Click on `Set up Connection`
7. Status > Click on `Sync now`
8. Wait for Completion

#### Reporting API Service
Hit http://localhost:8100/api/data/ on browser or postman



