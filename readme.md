Please see instructional video on how to use the API; a simple, but brief overview on how to make and verify API calls via POSTMAN pertaining to the Canary Interview Challenge:

Set video to 720p HD in Youtube settings

https://www.youtube.com/watch?v=g7mKaZQzu-I&list=UUuHCRMLMzGMPeFlw4VzFphg&index=1


For this project, I decided to use python and flask with a Postgres backend due to the fact that it is lightweight and quick for implementation.  In a real world application, I would use a more enterprise ready get request that can process multiple requests from concurrent users in real time - normally, this implementation could either be built with a binary tree lookup when searching data or if not - an Elastic Search Server, which is already optimized for commercical performance.  I use virtual environmets as a best practice to avoid mixing up library and python versions.    

The API has the following endpoints - a GET request and POST 

It can be queried using the following API route below.  I use postman to test the endpoints.

http://127.0.0.1:5000/bundles?sensor_type=temperature&device_uuid=b21ad0676f26439482cc9b1c7e827de4&start_time=1510093205&end_time=1510093209

The URL above accepts the following parameters below, each with their own specific criteria.  All parameters are required, the start and end time are denoted by integers as the required format for date is in linux time.  Once a sensor type, sensor UUID, and start and end times are specified in the URL gateway, a get request is sent to the server to return the results that correlate with the search criteria.

The steps to run the application are below.  I chose to use the built in Flask server with a Postgres backend, and Postman to query the API.

Input Parameters: 

UUID = > String 
Sensor Type = > Humidity or Temperature 
Sensor Input Parameters = > Between 0 and 100, inclusive
Sensor Reading Time and End Time= > The requested output is in linux time, so it will be represented as an integer

## Database Configuration:

This was coded on MAC OSX

Download the postgress app from here:

https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

For Database UI download Pg Admin:

https://www.pgadmin.org/


from the UI create a database named `webdev`
And user with

username: `postgres` 
password: `postgres` 

you can use other credentials but you will have to update that in config file


## Web App


create python 3 virtualenv

`virtualenv app`

Activate the environment

`source app/bin/activate`, to exit out of the virtual environment, type 'deactivate' in the terminal.



```
cd webdev
export PYTHONPATH="${PYTHONPATH}:${pwd}"  add the current directory to the python path

```


install the requirements

`pip install -r requirements.txt`

Run Migrations

`alembic upgrade head`

start the app

`python webdev.py`

Endpoint to access is

`127.0.0.1:5000/bundles`

Query the API, I use POSTMAN

http://127.0.0.1:5000/bundles?sensor_type=humidity&device_uuid=b21ad0676f26439482cc9b1c7e827de4&start_time=7&end_time=222222222222222222222
