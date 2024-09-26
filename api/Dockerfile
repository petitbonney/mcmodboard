FROM python:3.10-alpine

WORKDIR /app
COPY api.py requirements.txt ./
RUN pip install -r requirements.txt

ENTRYPOINT [ "fastapi", "run", "api.py" ]
