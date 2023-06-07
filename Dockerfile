FROM python:3.11-slim@sha256:eaee5f73efa9ae962d2077756292bc4878c04fcbc13dc168bb00cc365f35647e

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
