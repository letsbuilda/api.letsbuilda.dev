FROM --platform=linux/amd64 python:3.11-slim@sha256:2f749ef90f54fd4b3c77cde78eec23ab5b8199d9ac84e4ced6ae523ef223ef7b

RUN adduser --disabled-password api
USER api

ENV PATH="${PATH}:/home/api/.local/bin"

# Set Git SHA environment variable
ARG git_sha="development"
ENV GIT_SHA=$git_sha

WORKDIR /app
COPY pyproject.toml src ./
RUN python -m pip install .

EXPOSE 8080

CMD ["uvicorn", "api.server:app", "--host", "0.0.0.0", "--port", "8080"]
