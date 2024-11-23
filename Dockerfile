FROM python:3.13-slim@sha256:4efa69bf17cfbd83a9942e60e2642335c3b397448e00410063a0421f9727c4c4

# Define Git SHA build argument for sentry
ARG git_sha="development"
ENV GIT_SHA=$git_sha

COPY requirements.txt requirements.txt
RUN python -m pip install --requirement requirements.txt

COPY pyproject.toml README.md ./
COPY src/ src/
RUN PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir .

RUN adduser --disabled-password api
USER api

# HTTP
EXPOSE 8080

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "api.server:app"]
