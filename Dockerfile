FROM python:3.12.2-slim

COPY . /app/

WORKDIR /app

# install dependencies
RUN pip install --upgrade pip
RUN pip install -U setuptools
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
