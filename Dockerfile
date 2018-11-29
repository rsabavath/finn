FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python3.6 /src/main/resources/manage.py runserver 0.0.0.0:5000 &
