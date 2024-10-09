import os
import base64
import re


def extract_images_from_html(soup):
    images = []
    for img_tag in soup.find_all('img'):
        img_details = {'src': img_tag.get('src'),
                       'attributes': {attr: img_tag.get(attr) for attr in img_tag.attrs if attr != 'src'}}
        if img_details['src']:
            images.append(img_details)
    return images


def save_image_from_base64(image, output_dir):

    base64_regex = re.compile(r"data:(?P<mime>[\w+/]+);base64,(?P<data>[A-Za-z0-9+/=]+)")
    match = base64_regex.match(image['src'])

    if match:
        mime_type = match.group('mime')  # Extract MIME type
        base64_data = match.group('data')  # Extract Base64-encoded data

        if '+' in mime_type:
            extension = mime_type.split('+')[0].split('/')[-1]
        else:
            # Determine the appropriate file extension from the MIME type
            extension = mime_type.split('/')[-1]

        alt_text = image['attributes'].get('alt', 'extracted_image').split('.')[0]
        filename = f"{alt_text}.{extension}"
        filepath = os.path.join(output_dir, filename)

        # Decode the Base64 data and write it to a file
        with open(filepath, "wb") as file:
            file.write(base64.b64decode(base64_data))
        print(f"Saved image as {filepath}")

        return 1
    else:
        return 0

def extract_all_additional_data(soup, img_path):

    images = extract_images_from_html(soup)

    for img in images:
        #print(f"Image Path: {img['src']}")
        #print(f"Attributes: {img['attributes']}")
        state = save_image_from_base64(img, img_path)
        print(state)

    return soup
