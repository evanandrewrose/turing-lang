try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Turing Machine Lanuage',
	'author': 'Evan Rose',
	'url': 'INSERT URL',
	'download_url': 'DOWNLOAD URL',
	'author_email': 'evanandrewrose@gmail.com',
	'version': '0.1',
	'install_requires': [],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'turing-lang'
}

setup(**config)
