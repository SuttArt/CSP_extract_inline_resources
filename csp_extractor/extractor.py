import os
from bs4 import BeautifulSoup
from csp_extractor.js_extractor import *
from csp_extractor.css_extractor import *

def extract_resources(html_file):
    paths = create_dist_structure()

    # Logic to read the HTML file and extract inline resources
    print(f"Processing {html_file}...")

    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    soup = extract_all_css(soup, paths)

    # JS Filter region
    js_filter = JSExtractor(paths["js_file"])
    soup = js_filter.script_tag_filter(soup)


    # HTML region
    #Add <script src="index.js" defer></script>
    new_tag = soup.new_tag("script")
    new_tag["src"] = os.path.basename(paths["js_file"])
    soup.head.append(new_tag)
    print(soup.head)

    with open(paths["html_file"], 'a', encoding='utf-8') as f:
        f.write(soup.prettify())

def create_dist_structure():
    # Define the directory and file paths
    dist_dir = "www_dist"
    files = ["index.html", "main.css", "index.js"]
    return_struct = {
        "html_file": "",
        "css_file": "",
        "js_file": "",
    }

    # Create the dist_dir directory if it doesn't exist
    if not os.path.exists(dist_dir):
        os.makedirs(dist_dir)

    # Create the three files inside dist_dir
    for file in files:
        file_path = os.path.join(dist_dir, file)

        # Get the absolute path of the file
        absolute_path = os.path.abspath(file_path)

        open(file_path, 'w')
        if file.endswith(".html"):
            return_struct["html_file"] = absolute_path
        elif file.endswith(".css"):
            return_struct["css_file"] = absolute_path
        elif file.endswith(".js"):
            return_struct["js_file"] = absolute_path

    return return_struct
