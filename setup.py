import os
from setuptools import setup, find_packages
import brutebuster_signals


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="django-brutebuster-signals",
    version=brutebuster_signals.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    keywords='brutebuster signals email',
    packages=find_packages(),
    author='Tobias Lorenz',
    author_email='tobias.lorenz@bitmazk.com',
    url="https://github.com/bitmazk/django-brutebuster-signals",
    include_package_data=True,
    install_requires=[
        'django-brutebuster',
    ],
)
