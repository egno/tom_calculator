FROM python:3.8

COPY requirements.txt /src/requirements.txt

WORKDIR /src

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python", "app.py"]