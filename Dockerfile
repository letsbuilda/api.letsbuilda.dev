FROM python:3.12-slim@sha256:43a49c9cc2e614468e3d1a903aabe17a97a4c788c76cf5337b5cdc3535b07d4f

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
