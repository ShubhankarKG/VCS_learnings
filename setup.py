# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='vcs_learning',
    version='0.1',
    description="Learning to develop a Version Control System",
    long_description_markdown_filename='README.md',
    url='https://github.com/ShubhankarKG/VCS_learnings.git',
    license='AGPL-3.0-or-later',
    keywords='git version-control',
    packages=find_packages(include='vcs'),
    classifiers=[
        'Development Status :: In Progress',
        'Intended Audience :: Developers',
        'License :: GNU AFFERO GENERAL PUBLIC LICENSE',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],

    include_package_data=True,
    py_modules=['vcs'],
    # install_requires=install_requires,
    # extras_require=deps,
    # setup_requires=['setuptools-markdown'],
    # zip_safe=False,
)
