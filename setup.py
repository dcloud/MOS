from setuptools import setup, find_packages

import mos

setup(
    name='mos',
    version=mos.__version__,
    packages=find_packages(),
    license=mos.__license__,
    long_description=open('README').read(),
    author='Daniel Cloud',
    author_email='daniel+mos@danielcloud.org',
    url='https://github.com/dcloud/MOS',
    include_package_data=True,
    install_requires=[
        'Click',
        # Colorama is only required for Windows.
        'colorama',
    ],
    entry_points='''
        [console_scripts]
        mos=mos.cli:cli
    ''',
)