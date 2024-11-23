"""API server definition."""

import sentry_sdk
from litestar import Litestar
from litestar.config.compression import CompressionConfig
from litestar.config.cors import CORSConfig
from litestar.middleware.rate_limit import RateLimitConfig
from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import ScalarRenderPlugin

from .constants import GIT_SHA, Sentry
from .modules import controllers

sentry_sdk.init(
    dsn=Sentry.dsn,
    environment=Sentry.environment,
    send_default_pii=True,
    traces_sample_rate=0.25,
    profiles_sample_rate=0.25,
    release=f"{Sentry.release_prefix}@{GIT_SHA}",
)


cors_config = CORSConfig(allow_origins=["*"])
rate_limit_config = RateLimitConfig(rate_limit=("hour", 5_000), exclude=["/schema"])


app = Litestar(
    route_handlers=controllers,
    middleware=[rate_limit_config.middleware],
    openapi_config=OpenAPIConfig(title="Core", version=GIT_SHA, render_plugins=[ScalarRenderPlugin()]),
    cors_config=cors_config,
    compression_config=CompressionConfig(backend="brotli", brotli_gzip_fallback=True),
)
