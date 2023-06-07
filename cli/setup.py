from setuptools import setup

setup(
    name='graphe',
    version='0.1.0',
    py_modules=['graphe'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'graphe = graphe:cli',
        ],
    },
)