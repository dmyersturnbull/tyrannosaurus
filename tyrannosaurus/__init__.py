from setuptools import find_packages
from datetime import date
from pathlib import Path

root = Path(__file__).parent.parent.absolute()

class ProjectInfo:
	"""Information needed by setup.py and/or docs/conf.py."""
	# ------------ bump these -------------
	release = '0.0.1'
	current_release_date = date(2020, 4, 5)
	# -------------------------------------
	organization = 'dmyersturnbull'
	name = 'tyrannosaurus'
	status = 'Alpha'
	copyright_start_date = date(2016, 2, 22)
	project_start_date = date(2020, 3, 28)
	first_release_date = date(2020, 4, 2)
	version = release.split('-')[0] if '-' in release else release
	packages = find_packages(str(root))
	description = 'A collection of Python snippets for the Kokel Lab'
	readme = Path(root / 'README.md').read_text(encoding='utf8')
	author = "Douglas Myers-Turnbull"
	copyright = "Copyright {}–{}, Douglas Myers-Turnbull & UCSF".format(copyright_start_date.year, current_release_date.year)
	credits = ["Douglas Myers-Turnbull", "the Keiser Lab @ UCSF", "UCSF"]
	license = 'Apache 2.0'
	maintainer = "Douglas Myers-Turnbull"
	url = 'https://github.com/{}/{}'.format(organization, name)
	download_url = url.rstrip('/') + '/archive/' + release + '.tar.gz'
	min_py_version = 3.7
	max_py_version = 3.9
	project_urls = {
		'organization': 'https://github.com/{}'.format(organization),
		'package': "https://pypi.org/project/{}".format(name),
		'build': "https://travis-ci.org/{}/{}".format(organization, name),
		'docs': 'https://{}.readthedocs.io'.format(name),
		'source': 'https://github.com/{}/{}'.format(organization, name),
		'license': 'https://www.apache.org/licenses/LICENSE-2.0',
		'issues': 'https://github.com/{}/{}/issues'.format(organization, name),
	}
	classifiers = [
		"Development Status :: 3 - Alpha",
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'License :: OSI Approved :: Apache Software License',
		'Programming Language :: Python :: 3 :: Only',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Software Development :: Build Tools',
		'Topic :: Software Development :: Code Generators',
		'Operating System :: OS Independent',
		'Typing :: Typed'
	]
	keywords = ['dependencies', 'requirements', 'install_requires', 'extras_require']

__version__ = ProjectInfo.version
__status__ = ProjectInfo.status
__author__ = ProjectInfo.author
__copyright__ = ProjectInfo.copyright
__credits__ = ProjectInfo.credits
__maintainer__ = ProjectInfo.maintainer
