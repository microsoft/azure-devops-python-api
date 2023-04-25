# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from setuptools import setup, find_packages

NAME = "azure-devops"
VERSION = "7.1.0b2"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "msrest>=0.7.1,<0.8.0"
]

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
]

setup(
    name=NAME,
    version=VERSION,
    license='MIT',
    description="Python wrapper around the Azure DevOps 7.x APIs",
    author="Microsoft Corporation",
    url="https://github.com/microsoft/azure-devops-python-api",
    keywords=["Microsoft", "VSTS", "Team Services", "SDK", "AzureTfs", "AzureDevOps", "DevOps"],
    install_requires=REQUIRES,
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
    long_description="Azure DevOps Python clients"
)
