from setuptools import setup, find_packages

# README read-in
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
# END README read-in

setup(
    name='riptide-proxy',
    version='0.5.0',
    packages=find_packages(),
    package_data={'riptide_proxy': ['tpl/*']},
    description='Tool to manage development environments for web applications using containers - HTTP and WebSocket Reverse Proxy Server',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/Parakoopa/riptide-proxy/',
    install_requires=[
        'riptide-lib >= 0.5, < 0.6',
        'tornado >= 6.0',
        'Click >= 7.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points='''
        [console_scripts]
        riptide_proxy=riptide_proxy.main:main
    ''',
)
