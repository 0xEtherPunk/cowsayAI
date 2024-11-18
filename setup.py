from setuptools import setup, find_packages
from src.version import VERSION

setup(
    name="cowsayai",
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
        "cowsay>=5.0",
    ],
    entry_points={
        'console_scripts': [
            'cowsayai=src.main:main',
        ],
    },
    author="0xEtherPunk",
    description="AI-powered cowsay with wisdom and humor",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/0xEtherPunk/cowsayAI",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
) 