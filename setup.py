#!/usr/bin/env python3
# coding=utf-8

import shutil
from pathlib import Path
from setuptools import setup, find_packages
from tyrannosaurus import ProjectInfo as X

root = Path(__file__).parent.parent.absolute()

# copy the readme and changelog to resources dir
readme_path = Path(X.name) / X.readme_path
changelog_path = (Path(X.name) / X.changelog_path)
readme_path.parent.mkdir(exist_ok=True, parents=True)
shutil.copy(X.readme_path.name, readme_path)
if Path(X.changelog_path.name).exists():
	changelog_path.parent.mkdir(exist_ok=True, parents=True)
	shutil.copy(X.changelog_path.name, changelog_path)

install_requires = Path('requirements.txt').read_text(encoding='utf8').splitlines()
extras_require = {}

# make an 'all' for easy installation
extras_require['all'] = []
for x in extras_require.values():
	extras_require['all'].extend(x)

setup(
	name=X.name,
	version=X.version,
	download_url = X.download_url,
	description=X.description,
	long_description=changelog_path.read_text(encoding='utf8'),
	long_description_content_type=X.readme_format,
	author=', '.join(X.authors),
	maintainer=', '.join(X.maintainers),
	license=X.license,
	url=X.url,
	project_urls=X.project_urls,
	packages=find_packages(str(root)),
	test_suite='tests',
	python_requires='>={},<={}'.format(X.min_py_version, X.max_py_version),
	install_requires=install_requires,
	extras_require=extras_require,
	zip_safe=False,
	package_data=X.package_data,
	classifiers=X.classifiers,
	keywords=X.keywords,
	entry_points=X.entry_points
)
