from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="temp-mail-so",
    version="1.0.0",
    author="TempMail.so",
    author_email="author@tempmail.so",
    description="A Python SDK for TempMail.so temporary email service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TempMailAPI/Temp-Mail-AP",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.25.1",
    ],
)
