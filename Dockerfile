FROM python:3.14-slim@sha256:5e59aae31ff0e87511226be8e2b94d78c58f05216efda3b07dbbed938ec8583b

COPY --from=ghcr.io/astral-sh/uv:0.11.6@sha256:b1e699368d24c57cda93c338a57a8c5a119009ba809305cc8e86986d4a006754 /uv /bin/

# Define Git SHA build argument for Sentry
ARG git_sha="development"
ENV GIT_SHA=$git_sha

RUN adduser --disabled-password api
USER api

WORKDIR /app

COPY uv.lock pyproject.toml ./
RUN uv sync --frozen --no-editable --no-default-groups --no-install-project

COPY --chown=api:api src/ src/
RUN uv sync --frozen --no-editable --no-default-groups

# HTTP
EXPOSE 8080

ENTRYPOINT ["uv", "run", "--no-sync", "gunicorn", "--bind", "0.0.0.0:8080", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "api.server:app"]
