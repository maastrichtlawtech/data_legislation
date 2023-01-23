import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.GDPR',
      version='0.0.1',
      description=('Questions to help you determine whether the EU General Data Protection Regulation is applicable in your case.'),
      long_description='# docassemble.GDPR\n\n[Regulation (EU)\
      2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) of the European\
      Parliament and of the Council of 27 April 2016 on the protection of\
      natural persons with regard to the processing of personal data and on\
      the free movement of such data \n\n## Author\n\nSystem Administrator, admin@admin.com\n\n',
      long_description_content_type='text/markdown',
      author='Gijs van Dijck',
      author_email='gijs.vandijck@maastrichtuniversity.nl',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/GDPR/',\
                                     package='docassemble.GDPR'),
     )
