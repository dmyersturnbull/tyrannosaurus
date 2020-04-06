#!/usr/bin/env python3
# coding=utf-8

from pathlib import Path
from setuptools import setup, find_packages
from tyrannosaurus import ProjectInfo as X

root = Path(__file__).parent.parent.absolute()

# generated from requirements.txt
install_requires=[
	'click         >=7.1,<8.0',
	'pur           >=5.3,<6.0',
	'pipreqs       >=0.4,<1.0',
	'hypothesis    >=5.8,<6.0',
	'pytest        >=5.4,<6.0'
]
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
	long_description=X.readme,
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
	include_package_data=True,
	classifiers=X.classifiers,
	keywords=X.keywords,
	entry_points={'console_scripts': ['tyrannosaurus = tyrannosaurus.tyrannosaurus:main']}
)
