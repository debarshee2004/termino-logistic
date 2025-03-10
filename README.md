# Termino-logistic

Termino-logistic is a powerful command-line interface (CLI) tool written in Python that allows users to send HTTP requests effortlessly. It is designed to streamline API interactions by supporting request configurations via YAML and JSON files. With Termino-logistic, users can execute various HTTP methods, manage request headers, send query parameters, and handle responses with ease. This tool is ideal for developers and testers who frequently interact with APIs and require a lightweight yet flexible solution.

## Table of Contents
- [Termino-logistic](#termino-logistic)
  - [Table of Contents](#table-of-contents)
  - [How to use](#how-to-use)
    - [Input Output Redirection](#input-output-redirection)
    - [Sample request file `myrequest.yml`](#sample-request-file-myrequestyml)
    - [A full example file `myrequest.yml`](#a-full-example-file-myrequestyml)
  - [How to Set Up the Project](#how-to-set-up-the-project)
    - [Clone the Repository in Your Local Environment](#clone-the-repository-in-your-local-environment)
    - [Setting Up the Environment](#setting-up-the-environment)
    - [Building and Uploading the Package](#building-and-uploading-the-package)
      - [Explanation:](#explanation)
      - [Understanding `setup.py`](#understanding-setuppy)
  - [How to contribute to this project](#how-to-contribute-to-this-project)
    - [How you can improve the project](#how-you-can-improve-the-project)
    - [How to contribute by writing test cases](#how-to-contribute-by-writing-test-cases)
    - [How to contribute by writing docs](#how-to-contribute-by-writing-docs)
    - [Important notes](#important-notes)
    - [How to raise an issue](#how-to-raise-an-issue)
    - [How to submit a pull request](#how-to-submit-a-pull-request)
    - [Branch Naming Convention](#branch-naming-convention)
  - [Conclusion](#conclusion)
  - [License](#license)


## How to use

Use the terminal first follow the steps and the `setup.py` file to build this project. Then run the tool by running `termino --help` in the terminal.

```sh
# example with using a yml file
termino -f request.yml
# example with using a json file
termino -f request.json

# use the -c flag for colored response
# example with using a yml file
termino -f -c request.yml
# example with using a json file
termino -f -c request.json

# Sending a GET request with custom headers (Note: this will override existing headers(if any) in .yml or .json file)
termino -f request.yml -H "Authorization: Bearer mytoken" -H "User-Agent: CustomClient/1.0"
```

### Input Output Redirection

```sh
# the response is written to stdout, and headers/status are written to stderr,
# so that users can take IO redirection to their advantage.
termino -f myrequest.yml > res.json 2> res_headers.txt

# both stdout and stderr can be redirected to the same file
termino -f myrequest.yml > res.txt 2>&1
```

### Sample request file `myrequest.yml`

```yml
# GET Request
url: https://cdn.animenewsnetwork.com/encyclopedia/api.xml?anime=4658
method: GET
params:
  offset: 2
  limit: 100
headers:
  accept: text/xml
  accept-language: en
timeout: 5000
```

```yml
# Download a book
url: http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf
method: GET
```

**By running the command** `termino -f myrequest.yml > book.pdf`.

### A full example file `myrequest.yml`

```yml
method: XXX # (REQUIRED) GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE
url: XXX # (REQUIRED) must be prefixed with http:// or https://

params: # url query parameters. have as many as you like
  offset: 0
  limit: 10

data: # data for POST
  name: john
  age: 22
  hobbies:
    - running
    - eating
    - sleeping

data: # you can also type data in json format instead of yaml
  {
    "name": "ash",
    "age": 10,
    "hobbies": ["catching pokemons", "eating", "travelling"]
  }

headers: # have as many as you like
  Content-Type: application/json
  Authorization: <Bearer Token>


cookies: # have as many as you like
  mycookie: <Cookie Value>
  myothercookie: <Other Cookie Value>

timeout: 3.14 # seconds

allow_redirects: true # true or false

proxies: # have as many as you like
  http: http://10.10.1.10:3128
  https: https://10.10.1.11:1080
  ftp: ftp://10.10.1.10:3128

# EITHER verify server's TLS certificate. true or false
verify: true
# OR path to a CA bundle to use
verify: some/folder/cacert.crt

# EITHER path to single ssl client cert file (*.pem)
cert: some/folder/client.pem
# OR (*.cert), (*.key) pair.
cert:
  - some/folder/client.cert
  - some/folder/client.key
```

## How to Set Up the Project

### Clone the Repository in Your Local Environment

Star and Fork the repository before cloning it into your local machine. Make sure you have Python `v3.12` installed with pip, also check that Git is installed.

```sh
# do replace the <username> with your actual username
git clone https://github.com/<username>/termino-logistic.git
```

### Setting Up the Environment

For this step, you can use a Conda environment or a Python virtual environment.

```sh
# For Conda
conda env create -f environment.yml
conda env list
conda activate termino-logistic
```

```sh
# For Python Environment
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

_Some extra Conda commands which can be helpful:_

```sh
conda env update --file environment.yml --prune
conda env export --name termino-logistic > environment.yml
conda env remove --name termino-logistic
```

_Use `pip freeze` to check if the dependencies are properly installed:_

```py
# list of libraries
certifi==2025.1.31
charset-normalizer==3.4.1
docutils==0.21.2
id==1.5.0
idna==3.10
jaraco.classes==3.4.0
jaraco.context==6.0.1
jaraco.functools==4.1.0
keyring==25.6.0
lxml==4.9.4
markdown-it-py==3.0.0
mdurl==0.1.2
more-itertools==10.6.0
nh3==0.2.21
packaging==24.2
Pygments==2.19.1
pywin32-ctypes==0.2.3
PyYAML==6.0.2
readme_renderer==44.0
requests==2.32.3
requests-toolbelt==1.0.0
rfc3986==2.0.0
rich==13.9.4
setuptools==75.8.2
twine==6.1.0
urllib3==2.3.0
wheel==0.45.1
```

### Building and Uploading the Package

To build the package, use the following commands:

```sh
python3 setup.py sdist bdist_wheel
twine upload dist/*
```

#### Explanation:

- `python3 setup.py sdist bdist_wheel` creates a source distribution (`sdist`) and a built distribution (`bdist_wheel`).
- `twine upload dist/*` uploads the generated package files to PyPI for distribution.

#### Understanding `setup.py`

The `setup.py` file defines how the package is structured and how it should be installed. Here is the key breakdown:

```py
import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

with (HERE / "requirements.txt").open() as f:
    requirements = f.read().splitlines()

setup(
    name="termino",
    version="0.0.0",
    description="cli tool using python to send request to a server",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/debarshee2004/termino-logistic",
    license="Apache",
    entry_points={
        "console_scripts": [
            "termino = app.main:main",
        ],
    },
    python_requires=">=3.12",
    classifiers=[
        "License :: Apache License",
        "Programming Language :: Python :: 3",
    ],
    packages=["termino"],
    include_package_data=True,
    install_requires=requirements,
)
```

- It reads dependencies from `requirements.txt`.
- Defines metadata like package name, version, description, license, and URL.
- Specifies the entry point (`termino = app.main:main`), allowing the tool to be run as a CLI command.
- Ensures compatibility with Python 3.12 and later.

---

## How to contribute to this project

We welcome contributions to Termino-logistic! Here are some ways you can help improve this project:

### How you can improve the project

1. **Bug fixes**: Find and fix bugs in the existing codebase
2. **Feature enhancements**: Add new features or enhance existing ones
3. **Performance improvements**: Optimize code for better performance
4. **Code refactoring**: Improve code structure and maintainability
5. **Cross-platform compatibility**: Ensure the tool works well across different operating systems

### How to contribute by writing test cases

1. Add test cases for existing functionality in the `tests/` directory
2. Ensure your test cases cover both expected behavior and edge cases
3. Make sure tests are clear, well-documented, and follow the existing testing pattern
4. Run the test suite before submitting your contribution to ensure nothing breaks

### How to contribute by writing docs

1. Improve existing documentation for clarity and completeness
2. Add documentation for new features or undocumented functionality
3. Create tutorials or usage examples that showcase the tool's capabilities
4. Fix typos, grammar issues, or formatting problems in existing documentation

### Important notes

- **Do not update the README.md file** directly without prior approval
- If any configuration file needs to be updated, please message the maintainer on Discord first

### How to raise an issue

1. Before creating a new issue, check if a similar issue already exists
2. Use the provided issue template to provide all necessary information
3. Be specific about the problem, including steps to reproduce, expected behavior, and actual behavior
4. Include version information (OS, Python version, package version)
5. Add relevant logs, screenshots, or error messages

### How to submit a pull request

1. Fork the repository and create a new branch for your feature or bugfix
2. Implement your changes following the project's coding style
3. Add or update tests as necessary
4. Ensure all tests pass before submitting
5. Use the provided pull request template
6. Link any related issues in your pull request description
7. Be responsive to feedback and be prepared to make requested changes

Thank you for considering contributing to Termino-logistic!

### Branch Naming Convention

To maintain a structured and organized development process, follow these branch naming conventions:

- **Feature Branches**: `feature/<short-description>` (e.g., `feature/add-logging`)
- **Bug Fixes**: `fix/<short-description>` (e.g., `fix/request-timeout`)
- **Documentation Updates**: `docs/<short-description>` (e.g., `docs/update-readme`)
- **Hotfixes**: `hotfix/<short-description>` (e.g., `hotfix/security-patch`)
- **Experimental**: `experiment/<short-description>` (e.g., `experiment/new-parser`)

Always create branches from the `main` branch unless instructed otherwise. Ensure your branch name is descriptive and concise.

---

## Conclusion

Termino-logistic is a flexible and efficient CLI tool for interacting with APIs using YAML and JSON configurations. Whether you're testing endpoints, automating API calls, or handling HTTP requests in bulk, this tool simplifies the process. We encourage contributions and feedback from the community to enhance and expand the functionality of Termino-logistic.

## License

This project is licensed under the Apache License. See the [LICENSE](./LICENSE) file for more details.
