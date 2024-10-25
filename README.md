# CSP Extract Inline Resources

## Description

This project is a task of the IT Security Workshop module. Link to the [Wiki](https://sarwiki.informatik.hu-berlin.de/CSP:_Umwandlung_von_Inline_/_Internal_CSS,_JS_und_DATA_in_externe_Ressourcen).

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
Once the prerequisites are done, you can do the following actions:

### Running the Program
To run the program with a specific HTML file, use the following command:
```bash
python csp_extractor/main.py index.html
```

### Building the Binary

You can also create a standalone binary for your system using PyInstaller.

To build the binary, run:
```bash
pyinstaller --onefile csp_extractor/main.py
```

The generated binary will be available in the dist/ directory.

## Docker

This project can also be built and deployed using Docker. There are three main workflows for using Docker in this project:

1. **Running Apache Server Only**
    ```bash
   docker build -t apache-webseite -f .docker/apache/Dockerfile .
   ```
    ```bash
   docker run -dit --name apache-server -p 8080:80 apache-webseite
   ```
   **Explanation**:  
   This step builds a Docker image using the Apache configuration specified in the `Dockerfile` located in the `.docker/apache/` directory. The `docker run` command starts a container named `apache-server`, exposing it on port 8080 of your host machine and mapping it to port 80 inside the container where Apache is running.

   You can build and run the Apache web server using appropriate Docker commands.

2. **Building the Binary and Starting the Server**
    ```bash
   docker build -t build_and_serve -f .docker/Dockerfile .
   ```
    ```bash
   docker run -dit --name apache-server-build -p 8080:80 build_and_serve
   ```
   **Explanation**:  
   This command sequence builds the binary, prepares it to extract inline resources, and then starts an Apache server to serve the processed HTML content. The `build_and_serve` Docker image handles both the binary creation and the serving of the generated files in a single step.

   To build the binary and serve the generated files via Apache, use the corresponding Docker commands.

3. **Creating Only the Binary**
    ```bash
   docker build -t csp_extractor_build -f .docker/bin/Dockerfile .
   ```
    ```bash
   docker run --name binary_container csp_extractor_build
   ```
    ```bash
   docker cp binary_container:/output/ ./bin 
   ```
   **Explanation**:  
   This process builds the binary using the configuration specified in `.docker/bin/Dockerfile`. After running the container, the `docker cp` command copies the binary from the container's `/output/` directory to the `./bin` directory on your host machine. You can then use the binary independently or as part of another workflow.

   To create the binary and copy it to your host machine, follow the appropriate Docker steps.

## Testing

_TODO: Provide instructions on testing the project and expected outcomes._

## Dependencies

If you add some dependencies, make sure to update the `requirements.txt` file. This will allow others to install the exact same dependencies when setting up the project. 
```bash
pip freeze > requirements.txt
```
This command will save the current state of all installed packages (including version numbers) into requirements.txt. It is good practice to do this after adding new dependencies to ensure your project remains consistent across different environments.
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

_TODO: Provide guidelines for contributing to the project._

## Authors

_TODO: Add authorship and credit information._
