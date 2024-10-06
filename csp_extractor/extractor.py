import os
from bs4 import BeautifulSoup
from csp_extractor.css_extractor import *

def extract_resources(html_file):
    paths = create_dist_structure()

    # Logic to read the HTML file and extract inline resources
    print(f"Processing {html_file}...")

    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    style_tag_list = extract_style_tags(soup)
    css_content = css_tags_to_string(style_tag_list)
    if css_content != "":
        add_link_to_html_header(soup, os.path.basename(paths["css_file"]))

    write_file(paths["css_file"], css_content, "w")

    inline_style_tags = find_inline_style(soup)
    inline_css_content = inline_dict_to_string(inline_style_tags)

    write_file(paths["css_file"], inline_css_content , "a")

    write_html_file(paths["html_file"], soup)

    #use soup for further modification and saving

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

        open(file_path, 'a')
        if file.endswith(".html"):
            return_struct["html_file"] = absolute_path
        elif file.endswith(".css"):
            return_struct["css_file"] = absolute_path
        elif file.endswith(".js"):
            return_struct["js_file"] = absolute_path

    return return_struct
