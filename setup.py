from __future__ import print_function
from setuptools import setup
import os
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

if not os.access("README.txt", os.F_OK) :
	eprint("Generate README.txt, using distreadem.sh (requires pandoc)")
	sys.exit(-1)
long_description = open('README.txt').read()


setup(
	name = "qgmap",
	version = "0.2",
	description = "Google Map widget for PySyde/PyQt4",
	author = "David Garcia Garzon",
	author_email = "voki@canvoki.net",
	url = 'https://github.com/vokimon/python-qgmap',
	long_description = long_description,
	license = 'GNU General Public License v3 or later (GPLv3+)',
	packages=[
		'qgmap',
		],
	package_dir={'qgmap': 'qgmap'},
    package_data={'qgmap': ['qgmap.js','qgmap.html']},
	scripts=[
		'qgmap-example.py',
		],
	classifiers = [
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 2.7',
		'Topic :: Scientific/Engineering :: GIS',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Environment :: X11 Applications :: Qt',
		'Environment :: Win32 (MS Windows)',
		'Intended Audience :: Developers',
		'Development Status :: 5 - Production/Stable',
		'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
		'Operating System :: OS Independent',
	],
	)

