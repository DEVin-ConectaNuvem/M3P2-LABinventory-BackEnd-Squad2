FROM python:3.8.13-alpine

ENV PORT 8080

WORKDIR /app

COPY . .

EXPOSE 8080

RUN pip3 install -r requirements.txt

CMD [ "python3", "app.py" ]
