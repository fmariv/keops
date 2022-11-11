from setuptools import setup

setup(
    name="keops",
    version='0.0.1',
    description='Python package for managing and editing Mapbox Vector Tiles in MBTiles format',
    author='Fran Martín',
    author_email='fmartinrivas2@gmail.com',
    install_requires=[
        'Click',
    ],
    package_dir={"": "."},
    packages=["keops"],
    entry_points='''
        [console_scripts]
        keops=keops.main:main_group
    ''',
)
