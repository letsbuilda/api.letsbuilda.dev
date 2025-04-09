FROM python:3.13-slim@sha256:e8eb2555f37d060a136bb68261e6998b90b499b4b83aee3e6d8b3a874741eb32

COPY --from=ghcr.io/astral-sh/uv:0.6.13@sha256:0b6dc79013b689f3bc0cbf12807cb1c901beaafe80f2ee10a1d76aa3842afb92 /uv /bin/

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
