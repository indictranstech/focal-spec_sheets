from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='spec_sheets',
    version=version,
    description='Specfications for costing sheets',
    author='indictranstech',
    author_email='a@b.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
