FROM python:3.8.13-alpine

ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=True
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080
ENV SECRET_KEY=ALGUMSEGREDO
ENV OAUTHLIB_INSECURE_TRANSPORT=1
ENV FRONTEND_URL=http://localhost:3000/
ENV BACKEND_URL=http://localhost:8080/
ENV PORT=8080

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8080

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app

USER appuser

CMD [ "python3", "app.py" ]
