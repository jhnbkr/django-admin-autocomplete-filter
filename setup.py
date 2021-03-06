import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-admin-autocomplete-filter',
    version='0.3',
    packages=find_packages(),
    include_package_data=True,
    license='GNU Lesser General Public License v3 (LGPLv3)',  # example license
    description='A simple Django app to render list filters in django admin using autocomplete widget',
    long_description=README,
    url='https://github.com/farhan0581/django-admin-autocomplete-filter',
    author='Farhan Khan',
    author_email='farhan0581@gmail.com',
    install_requires=[
        'django>=2.0',
    ],
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 2.0',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)