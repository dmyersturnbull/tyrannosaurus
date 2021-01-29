"""
Utilities for tests.

Original source: https://github.com/dmyersturnbull/tyrannosaurus
Copyright 2020–2021 Douglas Myers-Turnbull
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
"""
# NOTE: If you modify this file, you should indicate your license and copyright as well.
from __future__ import annotations
import logging
import os
import random
import shutil
import stat
import tempfile
import time
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path, PurePath
from typing import Generator, Union
from warnings import warn


# Keeps created temp files; turn on for debugging
KEEP = False


class TestResources:
    """
    A static singleton with utilities for filesystem operations in tests.
    Use ``TestResources.resource`` to get a file under ``tests/resources/``.

    Initializes a temporary directory with ``tempfile.TemporaryDirectory``
    and populates it with a single subdirectory, ``TestResources.global_temp_dir``.
    Temp directories for independent tests can be created underneath using
    ``TestResources.temp_dir``.
    """

    logger = logging.getLogger("TYRANNO.TEST")

    _start_dt = datetime.now()
    _start_ns = time.monotonic_ns()
    if KEEP:
        _tempfile_dir = None
        _temp_dir = Path("tmp-test-data")
    else:
        _tempfile_dir = tempfile.TemporaryDirectory()
        _temp_dir = Path(_tempfile_dir.name)

    logger.info(f"Set up main temp dir {_temp_dir.absolute()}")

    @classmethod
    def resource(cls, *nodes: Union[PurePath, str]) -> Path:
        """
        Gets a path of a test resource file under ``resources/``.

        Arguments:
            nodes: Path nodes under the ``resources/`` dir

        Returns:
            The Path ``resources``/``<node-1>``/``<node-2>``/.../``<node-n>``
        """
        return Path(Path(__file__).parent, "resources", *nodes).resolve()

    @classmethod
    @contextmanager
    def temp_dir(
        cls,
        copy_resource: Union[None, str, Path] = None,
        force_delete: bool = True,
    ) -> Generator[Path, None, None]:
        """
        Context manager.
        Creates a new temporary directory underneath ``global_temp_dir``.
        Note that it deletes the directory if it already exists,
        then deletes (if the path exists) when the context closes.

        Arguments:
            copy_resource: Copy from underneath the resource dir
            force_delete: If necessary, change the permissions to delete

        Yields:
            The created directory as a ``pathlib.Path``
        """
        path = TestResources._temp_dir / ("%0x" % random.getrandbits(64))
        if path.exists():
            cls._delete_tree(path, surefire=force_delete)
        if copy_resource is None:
            path.mkdir(parents=True)
            TestResources.logger.info(f"Created empty temp dir {path}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            copy_path = Path(Path(__file__).parent) / "resources" / copy_resource
            shutil.copytree(str(copy_path), str(path))
            TestResources.logger.info(f"Copied {copy_resource} to temp {path}")
        yield path
        # note the global dir is only cleaned by tempfile on exit
        if not KEEP:
            cls._delete_tree(path, surefire=force_delete)

    @classmethod
    def global_temp_dir(cls) -> Path:
        """
        The global temporary directory, which is underneath ``tempfile.TemporaryDirectory``.
        The parent directory will be destroyed, along with all of its components,
        as specified by ``tempfile``.
        """
        return cls._temp_dir

    @classmethod
    def start_datetime(cls) -> datetime:
        """
        The datetime that ``tests/__init__.py`` was imported.
        """
        return cls._start_dt

    @classmethod
    def start_monotonic_ns(cls) -> int:
        """
        The nanosecond value of the ``time.monotonic`` clock at which ``tests/__init__.py`` was imported.
        """
        return cls._start_ns

    @classmethod
    def destroy(cls) -> None:
        """
        Deletes the full tempdir tree.
        """
        if not KEEP:
            cls._tempfile_dir.cleanup()

    @classmethod
    def _delete_tree(cls, path: Path, surefire: bool = False) -> None:
        def on_rm_error(func, pth, exc_info):
            # from: https://stackoverflow.com/questions/4829043/how-to-remove-read-only-attrib-directory-with-python-in-windows
            os.chmod(pth, stat.S_IWRITE)
            os.unlink(pth)

        kwargs = dict(onerror=on_rm_error) if surefire else {}
        if path.exists():
            try:
                shutil.rmtree(str(path), **kwargs)
            except OSError:
                warn(f"Testing dir {path} could not be deleted")


__all__ = ["TestResources"]
