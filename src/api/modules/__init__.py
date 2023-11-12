"""Modules of the API."""

from importlib import import_module
from pkgutil import walk_packages

from fastapi import APIRouter

from api import modules

routers: list[APIRouter] = []
for module_info in walk_packages(modules.__path__, f"{modules.__name__}."):
    module = import_module(module_info.name)
    router = getattr(module, "router", None)
    if router is not None:
        routers.append(router)
