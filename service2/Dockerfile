# start from base
FROM python:3

COPY . /app
WORKDIR /app

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 8080

# run the command
CMD ["python",  "./app2.py"]