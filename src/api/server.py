"""API server definition."""

from os import getenv

import sentry_sdk
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import __version__
from .modules import routers

release_prefix = getenv("API_SENTRY_RELEASE_PREFIX", "api")
git_sha = getenv("GIT_SHA", "development")
sentry_sdk.init(
    dsn=getenv("API_SENTRY_DSN"),
    environment=getenv("API_SENTRY_ENV"),
    send_default_pii=True,
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
    release=f"{release_prefix}@{git_sha}",
)


app = FastAPI(
    title="Let's Build A API",
    description="An API to host Let's Build A's projects",
    version=__version__,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


for router in routers:
    app.include_router(router)
