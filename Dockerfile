FROM python:3.8.13-alpine

ENV PORT 8080
ENV HOST 0.0.0.0

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8080

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app

USER appuser

CMD [ "python3", "app.py" ]
