from setuptools import setup, find_packages

setup(
    name="calcctl",
    version="0.6.0",  
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'calcctl=app_ctl.calctl:main',  
        ],
    },
)