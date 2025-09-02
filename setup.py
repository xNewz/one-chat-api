from setuptools import setup, find_packages

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "The OneChat Python library provides an interface for sending messages, broadcasting messages to multiple users, sending location information, sending stickers, and sending files through the OneChat API."  # fallback text

setup(
    name="one-chat-api",
    version="0.3.2",
    description="The OneChat Python library provides an interface for sending messages, broadcasting messages to multiple users, sending location information, sending stickers, and sending files through the OneChat API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Pargorn Ruasijan (xNewz)",
    author_email="contact@pargorn.com",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
