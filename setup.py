from setuptools import setup, find_packages

setup(
    name="pygradient",
    version="0.1.0",
    author="Your Name",
    author_email="staff@vx-underground.org",
    description="A package for applying gradient color effects to text",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/OGZhu/pygradient",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests',
    ],
)