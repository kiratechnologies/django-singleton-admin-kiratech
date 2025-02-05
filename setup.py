import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-singleton-admin-2-kiratech',
    version='1.0.7',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Easily edit singleton models in the Django admin site',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/porowns/django-singleton-admin',
    author='porowns',
    author_email='porowns@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
    ]
)
