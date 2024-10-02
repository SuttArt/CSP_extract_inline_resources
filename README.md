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

## How to Build This Project

_TODO: Provide instructions on how to build and run the project._

## Usage

_TODO: Provide usage examples and how to run the tool._

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
