import os
from bs4 import BeautifulSoup  # Import BeautifulSoup for HTML parsing

from csp_extractor.data_extractor import extract_all_additional_data
from csp_extractor.js_extractor import *  # Import JS extraction-related logic
from csp_extractor.css_extractor import * # Import CSS extraction-related logic

def extract_resources(html_file):
    # Create necessary directories and empty files for the output (HTML, CSS, JS)
    paths = create_dist_structure()
    # Print a message to indicate which file is being processed
    print(f"Processing {html_file}...")

    # Open and read the HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # CSS filter region
    soup = extract_all_css(soup, paths)

    #Addtional data filter region | Starting with images, still needs improvement
    print(paths["img_dir"])
    soup = extract_all_additional_data(soup, paths["img_dir"])

    # JS Filter region
    js_filter = JSExtractor(paths["js_file"])  # Initialize JS extractor with the JS output file path

    # Filter out script tags and event handlers and process them
    soup = js_filter.script_tag_filter(soup)
    soup = js_filter.event_handler_filter(soup)
    soup = js_filter.js_url_filter(soup)

    # Write the extracted and processed JavaScript content to the JS file
    js_filter.write_js_file()

    # HTML region
    # Create a new <script> tag for the external JS file and append it to the <head> of the HTML document
    new_tag = soup.new_tag("script")
    new_tag["src"] = os.path.basename(paths["js_file"])
    # None to not have any value, like <script src="index.js" defer></script>
    new_tag["defer"] = None
    soup.head.append(new_tag)

    # Write the modified HTML (with externalized resources) to the output file
    with open(paths["html_file"], 'a', encoding='utf-8') as f:
        f.write(soup.prettify())


def create_dist_structure():
    # Define the directory where the output files (HTML, CSS, JS) will be saved
    dist_dir = "www_dist"
    # Define the directory where the output images will be saved
    img_dir = os.path.join(dist_dir, "img")

    # File names for the output HTML, CSS, and JS files
    files = ["index.html", "main.css", "index.js"]

    # Structure to hold the paths to the output files
    return_struct = {
        "html_file": "",
        "css_file": "",
        "js_file": "",
        "img_dir": os.path.abspath(img_dir),
    }

    # Create the dist_dir directory if it doesn't already exist
    if not os.path.exists(dist_dir):
        os.makedirs(dist_dir)

    # Create the img_dir directory if it doesn't already exist
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    # Create the three files inside dist_dir and store their absolute paths in return_struct
    for file in files:
        file_path = os.path.join(dist_dir, file)

        # Get the absolute path of the file
        absolute_path = os.path.abspath(file_path)

        # Create the file (if it doesn't exist) and open it in write mode
        open(file_path, 'w')

        # Assign the absolute path of each file to the appropriate entry in return_struct
        if file.endswith(".html"):
            return_struct["html_file"] = absolute_path
        elif file.endswith(".css"):
            return_struct["css_file"] = absolute_path
        elif file.endswith(".js"):
            return_struct["js_file"] = absolute_path

    # Return the paths to the created files
    return return_struct
