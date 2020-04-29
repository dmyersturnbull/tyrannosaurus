from __future__ import annotations

import abc
from pathlib import Path
from typing import Sequence

from tyrannosaurus.model import DependencyList, Error, ServiceName, VersionRange


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


class ServiceManager:
    def bump(self, source: ServiceName, target: ServiceName):
        pass
