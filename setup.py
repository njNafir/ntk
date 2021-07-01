import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="ntk",
    version="1.1.3",
    description="NTK is set of widgets and utils that implement high-level APIs.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/njnafir/ntk",
    author="Nj Nafir",
    author_email="njnafir@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=['ntk', 'ntk.db', 'ntk.objects', 'ntk.utils', 'ntk.widgets'],
    include_package_data=True,
    install_requires=[],
)
