# Weather forecast endpoint by Daniel Wong

This is a back end component for the endpoint to calculate the weather forecast by city name.

Stack: Python, Django. 

Services: Reservamos & Open Weather API

## Two ways to run the project: Docker compose or python directly

### Using Docker Compose: How to run the application?

Requirements: Docker engine https://docs.docker.com/engine/install/

In the project directory, you can run:

#### `docker compose up`

Open [http://localhost:8000/api/v1/weather-forecast/?city=merida](http://localhost:8000/api/v1/weather-forecast/?city=merida) to view it in the browser.

### Using Python directly: How to run the application?

Requirements: Python 3.12.2

In the project directory, you can run:

#### `pip install -r requirements.txt`

Installs all requirements for the app.

#### `python manage.py runserver`

Runs the endpoint.\
Open [http://localhost:8000/api/v1/weather-forecast/?city=merida](http://localhost:8000/api/v1/weather-forecast/?city=merida) to view it in the browser.
