try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'Stefan Peng',
	'url': 'URL',
	'download_url': 'download url',
	'author_email': 'stefanpeng9@gmail.com'
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex47']
	'scripts': [],
	'name': 'projectname'
}

setup(**config)