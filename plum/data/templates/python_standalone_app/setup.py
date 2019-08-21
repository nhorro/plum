import setuptools
import glob

with open("README.md", "r") as fh:
    long_description = fh.read()

def recursive_get_package_data():
    package_files = glob.glob("[project_name]/data/**/*")
    print(package_files)
    return package_files

setuptools.setup(
    name="[project_name]",
    version="1.0.0",
    author="[author]",
    author_email="[author_email]",
    description="[project_summary]",
    long_description="[project_long_summary]",
    long_description_content_type="text/markdown",
    url="[project_url]",
    packages=setuptools.find_packages(),    
    include_package_data=True,
    package_data={"plum": recursive_get_package_data() },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "[project_name] = [project_name]:app"
        ]
    }
)