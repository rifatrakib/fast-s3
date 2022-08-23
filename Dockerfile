FROM python:3.9-slim

COPY ./app /src/app
COPY ./requirements.txt /src

WORKDIR /src

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--reload"]