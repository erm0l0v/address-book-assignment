from os import path


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def _read(file_name):
    try:
        return open(path.join(path.dirname(__file__), file_name)).read()
    except IOError:
        return ''


def load_requirements(file_name):
    requirements = []
    for l in _read(file_name).split('\n'):
        if l and not l.startswith('#'):
            if l.startswith('-r'):
                requirements.extend(load_requirements(l[3:]))
            else:
                requirements.append(l)
    return requirements


requirements = load_requirements('requirements.txt')

readme = _read('README.md')

setup(
    name='address_book_assignment',
    version='0.1.0',
    description="assignment",
    long_description=readme,
    author="Kirill Ermolov",
    author_email='erm0l0v@ya.ru',
    url='https://github.com/erm0l0v/address_book_assignment',
    packages=[
        'address_book'
    ],
    package_dir={'address_book_assignment':
                 'address_book_assignment'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=requirements
)
