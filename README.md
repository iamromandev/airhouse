**AirHouse** is a data integration project that involves extracting data from **csv** source,
transforming it into desired format, and loading it into our **postress** destination 
[`data warehouse`]. It has its own API service for reporting the warehouse data.
####
**AirHouse** is built on open source `AirByte` for _ETL_ process and `FastAPI` for Reporting service.

## Tools
1. `Docker Engine:` local deployment
2. `AirByte:` ETL process
3. `FastAPI:` web framework for reporting service
4. `Pydantic:` data validation library
5. `SQLModel:` to interact with databases
6. `pylint + mypy + black:` code analyser, type checker and code formatter

## Installation
#### Docker Engine 
Docs - https://docs.docker.com/engine/install/

#### AirHouse
1. git clone https://github.com/iamromandev/airhouse.git
2. run `cd airhouse`
3. run `make start` for reporting api service
4. run `cd airbyte`
5. run `./run-ab-platform.sh` for etl process






