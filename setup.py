from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in rollon_hydraulics/__init__.py
from rollon_hydraulics import __version__ as version

setup(
	name="rollon_hydraulics",
	version=version,
	description="Rollon",
	author="Aerele",
	author_email="hello@aerele.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
