FROM python:3.11-slim@sha256:1966141ab594e175852a033da2a38f0cb042b5b92896c22073f8477f96f43b06

RUN adduser --disabled-password api
USER api

ENV PATH="${PATH}:/home/api/.local/bin"

# Define Git SHA build argument for sentry
ARG git_sha="development"
ENV GIT_SHA=$git_sha

WORKDIR /home/api

COPY requirements.txt .
RUN python -m pip install --requirement requirements.txt

COPY --chown=api:api . .
RUN python -m pip install .

EXPOSE 8080

CMD ["uvicorn", "api.server:app", "--host", "0.0.0.0", "--port", "8080"]
