from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in custom_project/__init__.py
from custom_project import __version__ as version

setup(
	name="custom_project",
	version=version,
	description="Extend Project Function",
	author="Immunocan",
	author_email="gaoxinxiang@immunocan.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
