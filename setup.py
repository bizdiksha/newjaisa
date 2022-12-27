from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in newjaisa/__init__.py
from newjaisa import __version__ as version

setup(
	name="newjaisa",
	version=version,
	description="app to contain customizations for newjaisa",
	author="Diksha Jadhav",
	author_email="diksha.jadhav@bizmap.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
