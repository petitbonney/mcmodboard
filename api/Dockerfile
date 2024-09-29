FROM python:3.10-alpine

WORKDIR /app
COPY api.py requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "fastapi", "run", "api.py" ]
