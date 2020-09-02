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
        'django>2.0,<2.2',
        'django-compressor',
        'UW-RestClients-Core<1.0,>=0.9',
        'lesscpy',
        'django-pyscss',
        'pyyaml',
        'ua-parser',
        'user-agents',
        'django-user-agents',
        'UW-Django-SAML2<2.0',
    ],
    license='Apache License, Version 2.0',
    description='A Django app to ...',
    long_description=README,
    url='http://www.example.com/',
    author='Your Name',
    author_email='yourname@example.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
