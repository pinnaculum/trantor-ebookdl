
import sys
from setuptools import setup

PY_VER = sys.version_info

if PY_VER >= (3, 5):
    pass
elif PY_VER >= (3, 4):
    raise RuntimeError("You need python3.5 or newer")


install_reqs = []
with open('requirements.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        install_reqs.append(line)


setup(
    name='trantor-ebookdl',
    version='0.1',
    license='GPL3',
    author='cipres',
    author_email='alkaline@gmx.co.uk',
    description='Ebooks downloader for the Imperial Library of Trantor',
    packages=[],
    include_package_data=False,
    scripts=['trantor-ebookdl'],
    install_requires=install_reqs,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3'
    ]
)
