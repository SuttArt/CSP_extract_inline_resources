import os
import uuid

def write_file(file_name, content, mode):
    with open(file_name, mode, encoding="utf-8") as file:
        file.write(content)

def write_html_file(file_name, soup):
    with open(file_name, "w", encoding="utf-8") as html_file:
        html_file.write(soup.prettify())

def is_style_attr(tag):
    return tag.has_attr('style')

def find_inline_style(soup):

    css_inline_rules = {}
    for tag in soup.findAll(is_style_attr):

        if not tag.has_attr('id'):
            unique_id = str(uuid.uuid4())[:8]  # Generate a short unique id
            tag['id'] = f"element-{unique_id}"

        css_inline_rules[tag['id']] = tag['style']
        del tag['style']

    return css_inline_rules

def inline_dict_to_string(inline_dict):

    inline_content = ""
    for element_id, styles in inline_dict.items():
        inline_content += f"#{element_id} {{ {styles} }}\n"
    return inline_content

def css_tags_to_string(tag_list):
    css_content = ""
    for tag in tag_list:
        css_content += tag.string
    return css_content

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

def extract_all_css(soup, paths):

    style_tag_list = extract_style_tags(soup)
    head_css_content = css_tags_to_string(style_tag_list)

    inline_style_tags = find_inline_style(soup)
    inline_css_content = inline_dict_to_string(inline_style_tags)

    all_css_content = head_css_content + "\n" + inline_css_content

    add_link_to_html_header(soup, os.path.basename(paths["css_file"]))
    write_file(paths["css_file"], all_css_content, "w")

    return soup