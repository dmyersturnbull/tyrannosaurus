from datetime import date
from pathlib import Path

_statuses = {v.lower(): "{} - {}".format(i+1, v) for i, v in enumerate(['Planning', 'Pre-Alpha', 'Alpha', 'Beta', 'Production/Stable', 'Mature', 'Inactive'])}

here = Path(__file__).parent
readme_file = (here.parent/'README.md') if (here.parent/'README.md').exists() else here/'resources'/'README.md'


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
	description = 'A collection of Python snippets for the Kokel Lab'
	authors = ["Douglas Myers-Turnbull"]
	contributors = ["the Keiser Lab @ UCSF", "UCSF"]
	maintainers = ["Douglas Myers-Turnbull"]
	# license
	license = 'Apache 2.0'
	classifier_osi_license = 'Apache Software License'
	# topics and keywords
	classifier_audiences = ['Developers']
	classifier_topics = ['Libraries :: Python Modules', 'Build Tools', 'Code Generators']
	keywords = ['dependencies', 'requirements', 'install_requires', 'extras_require']
	# -------------------------------------
	# ----------- check these -------------
	credits = list({*authors, *contributors, *maintainers})
	copyright = "Copyright {}–{}".format(project_start_date.year, current_release_date.year)
	url = 'https://github.com/{}/{}'.format(organization, name)
	download_url = url.rstrip('/') + '/archive/' + release + '.tar.gz'
	contact = url
	version = release.split('-')[0] if '-' in release else release
	readme = readme_file.read_text(encoding='utf8')
	readme_format = 'text/markdown'
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
		*['Programming Language :: Python :: 3.'.format(v) for v in range(int(str(min_py_version).split('.')[1]), int(str(max_py_version).split('.')[1])+1)],
		*['Topic :: Software Development :: '+c for c in classifier_topics],
		*['Intended Audience :: '+c for c in classifier_audiences],
		'Operating System :: OS Independent',
	]
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

