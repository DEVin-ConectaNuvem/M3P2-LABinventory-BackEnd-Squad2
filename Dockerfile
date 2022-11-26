FROM python:3.8.13-alpine

ENV PORT 5000

WORKDIR /app

COPY . .

EXPOSE 5000

RUN pip3 install -r requirements.txt

CMD [ "python3", "app.py" ]
