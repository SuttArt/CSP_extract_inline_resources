import sys
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the project root directory to sys.path
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

from src.extractor import extract_resources


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_html_file>")
        sys.exit(1)

    html_file = sys.argv[1]
    extract_resources(html_file)


if __name__ == "__main__":
    main()