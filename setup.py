from distutils.core import setup


with open('README.md') as file:
    long_description = file.read()


setup(name='twitter-application-only-auth',
      version='0.3.0',
      author='Pablo SEMINARIO',
      author_email='pablo@seminar.io',
      url='https://github.com/pabluk/twitter-application-only-auth',
      description='A simple implementation of '
      'the Twitter Application-only authentication',
      long_description=long_description,
      license='GNU General Public License v3 (GPLv3)',
      packages=['application_only_auth'],
      provides=['application_only_auth (0.3.0)'],
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Topic :: Software Development :: Libraries'])
