FROM --platform=linux/amd64 python:slim-bullseye

# Set Git SHA environment variable
ARG git_sha="development"
ENV GIT_SHA=$git_sha

COPY . .

RUN pip install .

CMD ["uvicorn", "api.server:app", "--host", "0.0.0.0", "--port", "8080"]
