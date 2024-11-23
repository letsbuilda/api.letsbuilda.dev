"""Loads configuration from environment variables and `.env` files.

By default, the values defined in the classes are used, these can be overridden by an env var with the same name.

An `.env` file is used to populate env vars, if present.
"""

from os import getenv
from typing import Final

from pydantic_settings import BaseSettings

GIT_SHA: Final[str] = getenv("GIT_SHA", "development")
"""Git SHA for Sentry"""


class EnvConfig(
    BaseSettings,
    env_file=".env",
    env_file_encoding="utf-8",
    extra="ignore",
    env_nested_delimiter="__",
):
    """Our default configuration for models that should load from .env files."""


class _Sentry(EnvConfig, env_prefix="sentry_"):
    """Environment variables for Sentry."""

    dsn: str = ""
    release_prefix: str = "api"
    environment: str = "production"


Sentry = _Sentry()
