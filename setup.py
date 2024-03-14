from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")


setup(
    name="tips-and-tricks-task",
    version="1.0.0",
    description="Completed \"Tips and tricks task\"",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SiarheiMatsevich/python-automation-mentoring",
    author="Siarhei Matsevich",
    author_email="siarhei_matsevich@epam.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Mentors",
        "Topic :: Automated Testing Studying :: Completing Tasks",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="sample, learning, task completing",
    packages=find_packages(where="."),
    python_requires=">=3.9, <4",
    install_requires=["prettytable>=3.9.0",
                      "setuptools>=69.1.0",
                      "wcwidth>=0.2.13"],
)
