from distutils.command.build import build

from setuptools import find_packages, setup


class CustomBuild(build):
    # lifted from pretalx (Apache 2.0), thanks!
    # https://github.com/pretalx/pretalx/blob/master/src/setup.py

    def run(self):
        import os

        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dino.test_settings")

        import django

        django.setup()

        from django.core import management

        management.call_command('collectstatic', verbosity=1, interactive=False)
        build.run(self)


setup(
    name='dino',
    version='0.1',
    python_requires='>=3.8',
    description='Admin interface for PowerDNS.',
    author='uberspace.de',
    author_email='hallo@uberspace.de',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    keywords='dns powerdns pdns admin administration',
    install_requires=[
        'Django>=3.2,<4.3',
        'dj-database-url>=0.5,<2.3',
        'requests>=2.25',
        'python-powerdns@https://github.com/uberspace/python-powerdns/archive/1c61c574399e3e486a6e0b9d1e3d0521b2fa00a0.zip',
        'django-allauth>=0.50,<0.64',
        'rules>=3.0,<4.0',
        'whitenoise>=5.0,<7.0',
        'django-csp>=3.7,<4.0',
        'django-foundation-formtags>=0.1,<1.0',
        'idna>=3.0',
        'uwsgi>=2.0.20',
    ],
    extras_require={
        'mysql': [
            'mysqlclient>=1.3.13',
        ],
        'pgsql': [
            'psycopg2>=2.5.4',
        ],
        'dev': [
            'isort',
            'pylama',
            'ipython',
            'django-extensions',
        ],
        'test': [
            'pytest!=4.2.0,>=3.6',  # pytest-django version requirement
            'pytest-cov',
            'pytest-django',
            'pytest-mock',
            'pytest-lazy-fixture==0.6.*',
            'beautifulsoup4',
        ],
        'doc': [
            'sphinx',
            'sphinx_rtd_theme',
            'sphinx-autobuild',
        ],
    },
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    cmdclass={'build': CustomBuild},
)
