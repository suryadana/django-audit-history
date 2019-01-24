import os
from setuptools import setup

base = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(base, 'README.rst')).read()

setup(
    name='django-audit-history',
    version='0.1',
    packages=['audit_history'],
    description='''
    A library django for get history request, response and exception handler
    ''',
    long_description=README,
    author='Komang Suryadana',
    author_email='suryadana80@gmail.com',
    url='https://github.com/suryadana/django-audit-history/',
    license='MIT',
    install_requires=[
        'Django>=1.10',
    ]
)
