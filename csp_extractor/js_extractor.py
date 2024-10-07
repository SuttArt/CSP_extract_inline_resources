import hashlib  # Importing hashlib to generate unique names for functions based on content hashes


class JSExtractor:
    def __init__(self, file_path):
        # Path where the extracted JavaScript will be saved
        self.file_path = file_path
        # List to store the contents of extracted <script> tags and generated functions
        self.inline_scripts = []

    # Write the extracted and generated JavaScript to the file
    def write_js_file(self):
        # Open the specified file in append mode and write each script or function
        with open(self.file_path, 'a') as f:
            for script in self.inline_scripts:
                f.write(script)

    # Extract and remove inline <script> tags from the HTML
    def script_tag_filter(self, soup):
        # Find all <script> tags in the parsed HTML
        scripts = soup.find_all("script")

        # Iterate over each <script> tag, extract it, and store its content
        for script in scripts:
            script = script.extract()  # Remove the script tag from the DOM
            self.inline_scripts.append(script.string)  # Append the script content to the inline_scripts list

        # Return the modified HTML without the <script> tags
        return soup

    # Handle inline event handlers (like onclick, onmouseover, etc.) and extract their JavaScript
    def event_handler_filter(self, soup):
        # List of all possible event handler attributes in HTML
        # For details:
        # https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes#event_handler_attributes
        # https://html.spec.whatwg.org/multipage/webappapis.html#event-handlers-on-elements,-document-objects,-and-window-objects
        event_handlers = [
            "onabort",
            "onauxclick",
            "onbeforeinput",
            "onbeforematch",
            "onbeforetoggle",
            "oncancel",
            "oncanplay",
            "oncanplaythrough",
            "onchange",
            "onclick",
            "onclose",
            "oncontextlost",
            "oncontextmenu",
            "oncontextrestored",
            "oncopy",
            "oncuechange",
            "oncut",
            "ondblclick",
            "ondrag",
            "ondragend",
            "ondragenter",
            "ondragleave",
            "ondragover",
            "ondragstart",
            "ondrop",
            "ondurationchange",
            "onemptied",
            "onended",
            "onformdata",
            "oninput",
            "oninvalid",
            "onkeydown",
            "onkeypress",
            "onkeyup",
            "onloadeddata",
            "onloadedmetadata",
            "onloadstart",
            "onmousedown",
            "onmouseenter",
            "onmouseleave",
            "onmousemove",
            "onmouseout",
            "onmouseover",
            "onmouseup",
            "onpaste",
            "onpause",
            "onplay",
            "onplaying",
            "onprogress",
            "onratechange",
            "onreset",
            "onscrollend",
            "onsecuritypolicyviolation",
            "onseeked",
            "onseeking",
            "onselect",
            "onslotchange",
            "onstalled",
            "onsubmit",
            "onsuspend",
            "ontimeupdate",
            "ontoggle",
            "onvolumechange",
            "onwaiting",
            "onwebkitanimationend",
            "onwebkitanimationiteration",
            "onwebkitanimationstart",
            "onwebkittransitionend",
            "onwheel",
            "onblur",
            "onerror",
            "onfocus",
            "onload",
            "onresize",
            "onscroll",
            "onafterprint",
            "onbeforeprint",
            "onbeforeunload",
            "onhashchange",
            "onlanguagechange",
            "onmessage",
            "onmessageerror",
            "onoffline",
            "ononline",
            "onpageswap",
            "onpagehide",
            "onpagereveal",
            "onpageshow",
            "onpopstate",
            "onrejectionhandled",
            "onstorage",
            "onunhandledrejection",
            "onunload",
            "onreadystatechange",
            "onvisibilitychange"
        ]

        # Find all tags in the HTML
        tags = soup.find_all()

        # Iterate through each tag and check if it has any event handler attributes
        for tag in tags:
            for attr, value in tag.attrs.items():
                if attr in event_handlers:
                    # Generate a unique function name by hashing the event handler's JavaScript code
                    hash_func_name = hashlib.md5(value.encode()).hexdigest()

                    # Ensure function name starts with a letter and end with parentheses
                    hash_func_name = "f" + hash_func_name + "()"

                    # Create the new JavaScript function definition
                    new_function = "function " + hash_func_name + " { " + value + " }\n"

                    # Modify the tag’s event handler attribute to call the newly created function
                    tag.attrs[attr] = hash_func_name

                    # Append the new function to the inline_scripts list, if it hasn't been added already
                    if new_function not in self.inline_scripts:
                        self.inline_scripts.append(new_function)

        # Return the modified HTML with event handlers replaced by function calls
        return soup

# JavaScript in HTML Attributes


# Dynamic Inline Script Generation
