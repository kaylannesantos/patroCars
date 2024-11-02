FROM bitnami/python:3.12.7
WORKDIR /app

COPY ./app /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload --reload-dir=app
