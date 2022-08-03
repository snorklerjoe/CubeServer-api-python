"""Installs the API Server Python package"""

from setuptools import setup, find_packages


# Load __version__ from file:
with open("cubeserver_api_wrapper/_version.py", "r", encoding="utf-8") as version_file:
      exec(version_file.read())

# Metadata:
VERSION: str = __version__
"""Version string"""

AUTHORS: str = "Joseph R. Freeston"
"""A comma-separated list of contributors"""

GITHUB_URL: str = "https://github.com/snorklerjoe/CubeServer-api-python"
"""A URL to the source code and info on GitHub"""

DESCRIPTION = (
      'A wrapper for the API for logging data into the database.'
)

# Setup:
setup(name='CubeServer-api-wrapper',
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHORS,
      url=GITHUB_URL,
      packages=find_packages(),
      install_requires=[
            'requests[security]>=2.28.0,<3.0'
      ]
     )
