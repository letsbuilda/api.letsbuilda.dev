FROM --platform=linux/amd64 python:3.11-slim@sha256:66e41d125c90d679ad69b264ac7b78a3bd27e7510b63ba5987ad42678bbefc32

# Set Git SHA environment variable
ARG git_sha="development"
ENV GIT_SHA=$git_sha

COPY . .

RUN pip install .

CMD ["uvicorn", "api.server:app", "--host", "0.0.0.0", "--port", "8080"]
