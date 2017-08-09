from setuptools import setup

PACKAGE = "icinga2api"
NAME = "python-icinga2api"
DESCRIPTION = "python icinga2 api "
URL = "https://github.com/ifischer/python-icinga2api"
AUTHOR = __import__(PACKAGE).__author__
AUTHOR_EMAIL = __import__(PACKAGE).__contact__
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=[PACKAGE],
    zip_safe=False,
    long_description=open("README.md").read(),
    install_requires=[
        'requests',
        'requests[security]',
        'six'
    ]
)
