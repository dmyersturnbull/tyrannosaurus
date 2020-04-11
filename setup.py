#!/usr/bin/env python3
# coding=utf-8

import re
from pathlib import Path
from _collections import defaultdict
from setuptools import setup, find_packages
from tyrannosaurus import ProjectInfo as X

# copy doc files (.rst, .md, .txt, no-suffix) to resources dir
root = Path(__file__).parent
readme, readme_format = X.read_readme()
for f, _ in X.list_doc_files(root):
	Path(X.name, X.resource_path, f.name).write_text(f.read_text(encoding='utf8'), encoding='utf8')

# this is of course one of the issues that tyrannosaurus solves!
# noinspection PyArgumentList
install_requires, extras_require = [], defaultdict(list)
for line in Path('requirements.txt').read_text(encoding='utf8').splitlines():
	match = re.compile(r'^ *([A-Za-z0-9_-]+) *(\[[A-Za-z0-9-]+\])? *([^ ]*) *$').fullmatch(line)
	if match.group(2) is None:
		install_requires.append(match.group(1) + match.group(3))
	else:
		extras_require[match.group(2)].append(match.group(1) + match.group(2) + match.group(3))
# make an 'all' for easy installation
for reqs in [v for v in extras_require.values()]:
	extras_require['all'].extend(reqs)

setup(
	name=X.name,
	version=X.version,
	download_url = X.download_url,
	description=X.description,
	long_description=readme,
	long_description_content_type=readme_format,
	author=', '.join(X.authors),
	maintainer=', '.join(X.maintainers),
	license=X.license,
	url=X.url,
	project_urls=X.project_urls,
	packages=find_packages(),
	test_suite='tests',
	python_requires='>={},<={}'.format(X.min_py_version, X.max_py_version),
	tests_require=extras_require.get('test', []),
	install_requires=install_requires,
	extras_require=extras_require,
	zip_safe=False,
	package_data={'': ['*.rst', '*.md', str(X.resource_path/'*'), str(X.resource_path/'**'/'*')]},
	classifiers=X.classifiers,
	keywords=X.keywords,
	entry_points=X.entry_points
)
