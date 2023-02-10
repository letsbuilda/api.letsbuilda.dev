FROM --platform=linux/amd64 python:slim-bullseye

# Define Git SHA build argument for Sentry
ARG git_sha="development"

COPY . .

RUN pip install .

CMD ["uvicorn", "api.server:app", "--host", "0.0.0.0", "--port", "8080"]
