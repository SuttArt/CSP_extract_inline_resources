import sys
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the project root directory to sys.path to make sure packages in the project root are importable
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

from csp_extractor.extractor import extract_resources


def main():
    # Check if the user provided an argument (HTML file path)
    if len(sys.argv) < 2:
        # If no argument, print usage message and exit the program with an error code
        print("Usage: python main.py <path_to_html_file>")
        sys.exit(1)

    # Get the HTML file path from the command line argument
    html_file = sys.argv[1]

    # Call the function to extract resources from the HTML file
    extract_resources(html_file)


# Ensure the script runs only when executed directly, not when imported as a module
if __name__ == "__main__":
    main()
