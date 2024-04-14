FROM python:3.10-slim-buster  

WORKDIR /home

COPY requirements/requirements.txt . 
RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "manage.py", "runserver"]