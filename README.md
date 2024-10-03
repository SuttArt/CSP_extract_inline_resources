# CSP Extract Inline Resources

## Description

This project is a task of the IT Security Workshop module.

CSP Extract Inline Resources is a tool designed to automate the process of transforming HTML files by extracting inline resources such as CSS, JavaScript, and data into separate external files. This ensures compatibility with strict Content Security Policies (CSP) that prohibit "unsafe-inline" content, improving security and allowing the HTML to render properly in environments where inline resources are blocked.

### Motivation

In some cases, it's necessary to generate data in HTML format, allowing it to be viewed in a browser. However, for security reasons, many web servers implement a Content Security Policy (CSP) to mitigate attacks such as cross-site scripting (XSS). One common restriction is the prohibition of "unsafe-inline" content, which can lead to the browser ignoring inline JavaScript and styles due to CSP headers.

This project aims to automate the process of extracting inline resources into external files, ensuring the HTML content remains functional while adhering to CSP requirements.

## Features
- Extracts inline CSS, JavaScript, and other data from an HTML file.
- Saves extracted resources as external files.
- Updates the HTML file to link external resources.

## Prerequisites

Before you begin, make sure you have the following installed on your system:

1. **Python (Latest Version)**: This project requires the latest version of Python 3.x. You can download and install Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

To verify that Python is installed and check the version, you can run the following command in your terminal or command prompt:

```bash
python --version
```
If pip is not installed, you can install it by following the instructions here.

2. **pip**: pip is the Python package installer, and it usually comes with Python by default. 

To verify that pip is installed, run:
```bash
pip --version
```
If pip is not installed, you can install it by following the instructions here : [https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/).
3. **venv Module**: Ensure that the venv module is installed. This module comes bundled with Python 3.x by default. 
 
You can verify its presence by running:
```bash
python -m venv --help
```
4. **Create and Activate a Virtual Environment**: Once Python and `venv` are available, you should create and activate a virtual environment for the project. This will ensure all dependencies are installed in an isolated environment.

To create and activate the virtual environment:

On Unix/macOS:
```bash
python -m venv .venv
source .venv/bin/activate
```
On Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```
After activating the virtual environment, your terminal prompt will change, indicating that the virtual environment is active. From here, you can proceed to install the project dependencies.

## Installation

Once the prerequisites are done, you can install the project dependencies using the following command:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Program
To run the program with a specific HTML file, use the following command:
```bash
python csp_extractor/main.py index.html
```

You can also use Makefile to run it:
```bash
make start HTML_FILE=index.html
```

### Building the Binary

You can also create a standalone binary for your system using PyInstaller.

To build the binary, run:
```bash
pyinstaller --onefile csp_extractor/main.py
```

You can also use Makefile to build it:
```bash
make build-binary
```

The generated binary will be available in the dist/ directory.

## Testing

_TODO: Provide instructions on testing the project and expected outcomes._

## Dependencies

_TODO: List all dependencies required for this project._

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

_TODO: Provide guidelines for contributing to the project._

## Authors

_TODO: Add authorship and credit information._
