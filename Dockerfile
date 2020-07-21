FROM python:3.6

WORKDIR /app
COPY requirement.txt  /app

RUN pip install -r requirement.txt


CMD ["python", "/src/main/python/main.py" , "dev"]

