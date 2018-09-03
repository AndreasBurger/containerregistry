import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ccwienk-containerregistry",
    version="0.0.1",
    author="Christian Cwienk",
    author_email="Christian.Cwienk@sap.com",
    description="A set of Python libraries and tools for interacting with a Docker Registry.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ccwienk/containerregistry",
    packages=setuptools.find_packages(),
    install_requires=[
        'httplib2>=0.11.3, <0.12',
        'six>=1.9,<1.10',
        'oauth2client>=4.0,<4.1',
        'futures>=3.1.1, <3.2',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)