from __future__ import annotations
import re
import abc
from dataclasses import dataclass
from copy import copy
import enum
from pathlib import Path, PurePath
from functools import total_ordering
from typing import Optional, Sequence, Mapping, Union, Tuple as Tup
from tyrannosaurus.model import *


class ServiceError(Error, IOError):
    def __init__(self, service: ServiceName, msg: str, e: Exception):
        super().__init__("Service {} failed: {}".format(service, msg), e)
        self.service, self.msg = service, msg


class Service(metaclass=abc.ABCMeta):

    @property
    def name(self) -> ServiceName:
        raise NotImplementedError()

    @property
    def known_paths(self) -> Sequence[Path]:
        raise NotImplementedError()

    def find_latest(self, package: str):
        raise NotImplementedError()

    def has_compatible_version(self, package: str, requirements: VersionRange):
        raise NotImplementedError()

    def read(self, text: str) -> DependencyList:
        raise NotImplementedError()

    def write(self, deps: DependencyList) -> str:
        raise NotImplementedError()

    def modify_file(self, path: Path, deps: DependencyList) -> None:
        raise NotImplementedError()

class SetuptoolsService(Service):
    pass

class CondaEnvService(Service):
    pass

class CondaRecipeService(Service):
    pass

class RequirementsService(Service):
    pass

class PipfileService(Service):
    pass

class PiplockService(Service):
    pass

class PoetryService(Service):
    pass

class PoetryLock(Service):
    pass

class ServiceManager:

    def bump(self, source: ServiceName, target: ServiceName):
        pass
