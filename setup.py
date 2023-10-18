import os
from setuptools import find_packages, setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='mdot',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'setuptools',
        'django~=4.2',
        'django-compressor',
        'UW-RestClients-Core~=1.4',
        'django-htmlmin',
        'lesscpy',
        'django-pyscss',
        'pyyaml',
        'ua-parser',
        'user-agents',
        'django-user-agents',
        'UW-Django-SAML2',
    ],
    license='Apache License, Version 2.0',
    description='Mobile UW web application',
    long_description=README,
    url='https://github.com/uw-it-aca/mdot',
    author='UW-IT T&LS',
    author_email='aca-it@uw.edu',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
