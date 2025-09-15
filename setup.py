from setuptools import find_packages, setup

try:
    with open("README.md", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "Python client for OneChat API."

setup(
    name="one-chat-api",
    version="0.4.1",
    description="Python client for OneChat API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Pargorn Ruasijan (xNewz)",
    author_email="contact@pargorn.com",
    packages=find_packages(),
    install_requires=[
        "requests>=2.32.2",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
