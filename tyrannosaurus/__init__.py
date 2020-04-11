from datetime import date
from pathlib import Path
from dataclasses import dataclass
from typing import Generator, Optional, Tuple as Tup

@dataclass
class ConsoleScript:
	cmd: str
	module: str
	function: str


_statuses = {
	v.lower(): "{} - {}".format(i+1, v)
	for i, v in enumerate(['Planning', 'Pre-Alpha', 'Alpha', 'Beta', 'Production/Stable', 'Mature', 'Inactive'])
}

_known_formats = {
		'.md': 'text/markdown',
		'.rst': 'text/x-rst',
		'.txt': 'text/plain',
		'': 'text/plain'
	}
def guess_format(s):
	return _known_formats.get(Path(s).suffix)

def find_file(stubs):
	for stub in stubs:
		for suffix, fmt in _known_formats.items():
			p = Path(str(stub)+suffix)
			if p.exists():
				return p, fmt
	return None, None

class ProjectInfo:
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
	min_py_version = 3.7
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
	classifier_topics = ['Software Development :: Libraries :: Python Modules', 'Software Development :: Build Tools', 'Software Development :: Code Generators']
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
		"Development Status :: {}".format(_statuses[status.lower()]),
		'Natural Language :: English',
		'License :: OSI Approved :: '+classifier_osi_license,
		'Programming Language :: Python :: 3 :: Only',
		*['Programming Language :: Python :: 3.'+str(v) for v in range(int(str(min_py_version).split('.')[1]), int(str(max_py_version).split('.')[1])+1)],
		*['Intended Audience :: '+c for c in classifier_audiences],
		*['Topic :: '+c for c in classifier_topics],
		*['Framework :: {}' + c for c in classifier_frameworks],
		'Operating System :: OS Independent',
	]
	@classmethod
	def list_doc_files(cls, under=resource_path) -> Generator[Tup[Path, str], None, None]:
		for f in Path(under).iterdir():
			if f.is_file():
				path, fmt = find_file(f.name)
				if path is not None:
					yield path, fmt
	@classmethod
	def read_readme(cls, under: Path = resource_path) -> Tup[Optional[str], Optional[str]]:
		path, fmt = find_file([under/'README'])
		if path is None: return None, None
		return path.read_text(encoding='utf8'), fmt
	@classmethod
	def read_changelog(cls, under=resource_path) -> Tup[Optional[str], Optional[str]]:
		path, fmt = find_file([under/'CHANGES', under/'CHANGELOG'])
		if path is None: return None, None
		return path.read_text(encoding='utf8'), fmt
	# -------------------------------------

__version__ = ProjectInfo.version
__status__ = ProjectInfo.broad_status
__authors__ = ProjectInfo.authors
__credits__ = ProjectInfo.credits
__maintainer__ = ', '.join(ProjectInfo.maintainers)
__copyright__ = ProjectInfo.copyright
__license__ = ProjectInfo.license
__date__ = ProjectInfo.current_release_date
__contact__ = ProjectInfo.contact

__all__ = ['ProjectInfo']

