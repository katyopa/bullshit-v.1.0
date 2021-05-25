from setuptools import setup, find_packages

setup(
    name="tagcounter",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "tagcounter = tagcounter.tagcounter:main",
        ],
    },
    install_requires=[
        # put your requirements separated by comma here
    ],
    version="0.1",
    author="Htosci Dziesci",
    author_email="gtosci_dziesci@gmail.com",
    description="Count Tags",
    license="MIT",
)
