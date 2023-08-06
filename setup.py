from pathlib import Path

from setuptools import find_namespace_packages
from setuptools import setup

DOCS_PATH = Path(__file__).parents[0] / "docs/README.md"
PATH = Path("README.md")
if not PATH.exists():
    with open(DOCS_PATH, encoding="utf-8") as f1:
        with open(PATH, "w+", encoding="utf-8") as f2:
            f2.write(f1.read())

setup(
    name="revChatGPT",
    version="5.0.1",
    description="ChatGPT is a reverse engineering of OpenAI's ChatGPT API",
    long_description=open(PATH, encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TheRealVeni/ChatGPT-Architecture/tree/main",
    author="Veni Code",
    author_email="problade@t-online.de",
    license="GNU General Public License v2.0",
    packages=find_namespace_packages("src"),
    package_dir={"": "src"},
    py_modules=["revChatGPT"],
    package_data={"": ["*.json"]},
    install_requires=[
        "OpenAIAuth==0.3.6",
        "requests[socks]",
        "httpx[socks]",
        "async_tio",
        "prompt-toolkit",
        "tiktoken>=0.3.0",
        "openai",
    ],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)