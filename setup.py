import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plum",
    version="1.0.0",
    author="nhorro",
    author_email="nhorro@gmail.com",
    description="Project scaffolding",
    long_description="Simple program in python to generate a project skeleton from templates in the spirit of Yeoman, CookieCutter and others.",
    long_description_content_type="text/markdown",
    url="https://github.com/nhorro/plum",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)