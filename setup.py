import setuptools
REQUIRED = [
    "numpy",
    "pandas"
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
    setuptools.setup(
    name="mgospod",
    version = "0.1.13",
    author = "cmgospod",
    description = "a collection of data science helper functions",
    long_description = LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/cmgospod/lambdata-cmgospod",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires = REQUIRED,
    classifiers=["Programming Language :: Python :: 3",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    ]
    )
