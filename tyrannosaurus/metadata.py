from datetime import date
from pathlib import Path, PurePath
from dataclasses import dataclass
from typing import Generator, Iterable, Sequence, Optional, Union, Tuple as Tup

@dataclass
class ConsoleScript:
	cmd: str
	module: str
	function: str

class Utils:

	min_supportable_python = 3.6

	statuses = {
		v.lower(): "{} - {}".format(i+1, v)
		for i, v in enumerate([
			'Planning',
			'Pre-Alpha',
			'Alpha',
			'Beta',
			'Production/Stable',
			'Mature',
			'Inactive'
		])
	}

	known_formats = {
			'.md': 'text/markdown',
			'.rst': 'text/x-rst',
			'.txt': 'text/plain',
			'': 'text/plain'
		}

	@classmethod
	def version_range(cls, minimum: float, maximum: float) -> Sequence[float]:
		if not 3.0 <= cls.min_supportable_python < 3.0 <= 4.0:
			raise ValueError("This function only handles Python 3!")
		if maximum < minimum:
			raise ValueError("Version {}–{} range is reversed".format(minimum, maximum))
		if minimum < cls.min_supportable_python or maximum < cls.min_supportable_python:
			raise ValueError("This doesn't support Python < 3.6. You need to modify this source.")
		return [v/10 for v in range(int(10*minimum), int(10*maximum), 1)]

	@classmethod
	def status_full_name(cls, name: str) -> str:
		return cls.statuses[name.lower()]

	@classmethod
	def guess_format(cls, s):
		return cls.known_formats.get(Path(s).suffix)

	@classmethod
	def find_file(cls, stubs: Iterable[Union[str, PurePath]]):
		for stub in stubs:
			for suffix, fmt in cls.known_formats.items():
				p = Path(str(stub)+suffix)
				if p.exists():
					return p, fmt
		return None, None

	@classmethod
	def list_doc_files(cls, under: Union[str, PurePath]) -> Generator[Tup[Path, str], None, None]:
		for f in Path(under).iterdir():
			if f.is_file():
				path, fmt = Utils.find_file(f.name)
				if path is not None:
					yield path, fmt

	@classmethod
	def read_readme(cls, under: Union[str, PurePath]) -> Tup[Optional[str], Optional[str]]:
		path, fmt = Utils.find_file([under/'README'])
		if path is None: return None, None
		return path.read_text(encoding='utf8'), fmt

	@classmethod
	def read_changelog(cls, under: Union[str, PurePath]) -> Tup[Optional[str], Optional[str]]:
		path, fmt = Utils.find_file([under/'CHANGES', under/'CHANGELOG', under/'HISTORY'])
		if path is None: return None, None
		return path.read_text(encoding='utf8'), fmt

	def __repr__(self): return self.__class__.__name__
	def __str__(self): return self.__class__.__name__
	def __eq__(self, other): return type(self) == type(other)


class Info:
	"""Information needed by setup.py and/or docs/conf.py."""

	# ------------ bump these -------------
	release = '0.0.1'
	current_release_date = date(2020, 4, 5)
	# -------------------------------------
	# ---------- modify these -------------
	# name and Github account/org
	organization = 'dmyersturnbull'
	name = 'tyrannosaurus'
	# status
	status = 'Alpha'
	broad_status = 'Development'
	project_start_date = date(2020, 4, 2)
	# python versions
	min_py_version = 3.6
	max_py_version = 3.9
	# descriptions and authors
	description = 'Generate ready-to-go Python projects and manage their dependencies'
	authors = ["Douglas Myers-Turnbull"]
	contributors = ["the Keiser Lab @ UCSF", "UCSF"]
	maintainers = ["Douglas Myers-Turnbull"]
	# paths
	resource_path = Path('resources')
	# license
	license = 'Apache 2.0'
	classifier_osi_license = 'Apache Software License'
	# topics and keywords
	classifier_audiences = ['Developers']
	classifier_topics = [
		'Software Development :: Libraries :: Python Modules',
		'Software Development :: Build Tools',
		'Software Development :: Code Generators'
	]
	classifier_frameworks = []
	keywords = ['dependencies', 'requirements', 'install_requires', 'extras_require']
	# command data
	console_scripts = [ConsoleScript('tyrannosaurus', 'tyrannosaurus.main', 'main')]
	# -------------------------------------

	# ----------- check these -------------
	credits = list({*authors, *contributors, *maintainers})
	copyright = "Copyright {}–{}".format(project_start_date.year, current_release_date.year)
	url = 'https://github.com/{}/{}'.format(organization, name)
	download_url = url.rstrip('/') + '/archive/' + release + '.tar.gz'
	contact = url
	version = release.split('-')[0] if '-' in release else release
	python_versions = Utils.version_range(min_py_version, max_py_version)
	entry_points = {
		'console_scripts': [
			"{} = {}{}".format(s.cmd, s.module, '' if s.function is None else ':' + s.function)
			for s in console_scripts
		]
	}
	project_urls = {
		'organization': 'https://github.com/{}'.format(organization),
		'package': "https://pypi.org/project/{}".format(name),
		'build': "https://travis-ci.org/{}/{}".format(organization, name),
		'docs': 'https://{}.readthedocs.io'.format(name),
		'source': 'https://github.com/{}/{}'.format(organization, name),
		'issues': 'https://github.com/{}/{}/issues'.format(organization, name),
	}
	classifiers = [
		"Development Status :: {}".format(Utils.status_full_name(status)),
		'Natural Language :: English',
		'License :: OSI Approved :: '+classifier_osi_license,
		'Programming Language :: Python :: 3 :: Only',
		*['Programming Language :: Python :: '+str(v) for v in python_versions],
		*['Intended Audience :: '+c for c in classifier_audiences],
		*['Topic :: '+c for c in classifier_topics],
		*['Framework :: {}' + c for c in classifier_frameworks],
		'Operating System :: OS Independent',
	]

	@classmethod
	def read_readme(cls) -> Tup[Optional[str], Optional[str]]:
		return Utils.read_readme(cls.resource_path)

	@classmethod
	def read_changelog(cls) -> Tup[Optional[str], Optional[str]]:
		return Utils.read_changelog(cls.resource_path)
	# -------------------------------------

__version__ = Info.version
__status__ = Info.broad_status
__authors__ = Info.authors
__credits__ = Info.credits
__maintainer__ = ', '.join(Info.maintainers)
__copyright__ = Info.copyright
__license__ = Info.license
__date__ = Info.current_release_date
__contact__ = Info.contact

__all__ = ['Info']
