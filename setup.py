from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tarefinancial/__init__.py
from tarefinancial import __version__ as version

setup(
	name="tarefinancial",
	version=version,
	description="Zecsn Extension for Tare Financial",
	author="Zecsn Technologies SMC Pvt. Ltd.",
	author_email="contact@zecsn.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
