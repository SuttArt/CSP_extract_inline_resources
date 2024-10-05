
def write_css_file(file_name, css_content):
    with open(file_name, "w", encoding="utf-8") as css_file:
        css_file.write(css_content)

def append_css_file(file_name, css_content):
    with open(file_name, "a", encoding="utf-8") as css_file:
        css_file.write(css_content)

def write_html_file(file_name, soup):
    with open(file_name, "w", encoding="utf-8") as html_file:
        html_file.write(str(soup))

def append_html_file(file_name, soup):
    with open(file_name, "a", encoding="utf-8") as html_file:
        html_file.write(str(soup))

def is_style_attr(tag):
    return tag.has_attr('style')

def css_tags_to_string(tag_list):
    css_content = ""
    for tag in tag_list:
        css_content += tag.string
    return css_content

# just stylesheet name not the full path, test bug if time
def add_link_to_html_header(soup, stylesheet_name):

    new_link = soup.new_tag("link", rel="stylesheet", href=stylesheet_name)
    head_tag = soup.find('head')
    if head_tag:
        head_tag.append(new_link)

def extract_style_tags(soup):
    css_tags = []
    list_style_tags = soup.find_all('style')
    for tag in list_style_tags:
        css_tags.append(tag.extract())
    return css_tags