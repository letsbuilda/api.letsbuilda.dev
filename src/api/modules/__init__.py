"""Modules of the API."""

from .fun import FunController
from .generators import GeneratorController
from .metadata import MetadataController

controllers = [FunController, GeneratorController, MetadataController]
