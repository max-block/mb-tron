import codecs
import os
import re

import setuptools


def find_version(*file_paths):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *file_paths), "r") as fp:
        version_file = fp.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name="mb-tron",
    version=find_version("mb_tron/__init__.py"),
    python_requires=">=3.9",
    packages=["mb_tron"],
    install_requires=[
        "click==8.0.1",
        "click-aliases==1.0.1",
        "PyYAML==5.4.1",
        "tronpy==0.2.6",
        "mb-commons",
    ],
    extras_require={
        "dev": [
            "pytest==6.2.4",
            "pytest-xdist==2.3.0",
            "pre-commit==2.13.0",
            "wheel==0.36.2",
            "twine==3.4.1",
            "python-dotenv==0.18.0",
        ],
    },
    entry_points={"console_scripts": ["mb-tron = mb_tron.cli:cli"]},
    include_package_data=True,
)
