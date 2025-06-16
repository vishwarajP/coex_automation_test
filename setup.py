from setuptools import setup, find_packages

setup(
    name="coaex_automation",
    version="0.1.0",
    packages=find_packages(),
    package_data={
        'coaex_automation': ['config/*.yaml'],
    },
    install_requires=[
        'pytest>=6.0',
        'pyyaml',
        'scapy',  # If using scapy
    ],
    python_requires='>=3.8',
)