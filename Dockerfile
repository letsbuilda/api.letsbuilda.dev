FROM python:3.13-slim@sha256:751d8bece269ba9e672b3f2226050e7e6fb3f3da3408b5dcb5d415a054fcb061

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
