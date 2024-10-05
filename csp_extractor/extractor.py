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

    # soup.style = <style> ... content <style/>
    # soup.style.string = content without tags

    style_tag_list = extract_style_tags(soup)
    css_content = css_tags_to_string(style_tag_list)
    if css_content != "":
        add_link_to_html_header(soup, "main.css")
        #bug with full absolut path, using name for now

    print(soup.prettify())

    # iterates through the tree to find all tags that have a style attribute
    #style_tag_list = soup.findAll(is_style_attr)
    #for tag in style_tag_list:
        #print(tag["style"] + " " + tag.name)

    # if time, clean up files with whitespaces and false indent
    write_css_file(paths["css_file"], css_content)
    write_html_file(paths["html_file"], soup)

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
