import hashlib

class JSExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        # List of <script> tags; each object is of type `bs4.element.Script`
        self.inline_scripts = []

    def write_js_file(self):
        with open(self.file_path, 'a') as f:
            for script in self.inline_scripts:
                f.write(script)

    # Inline <script> Tag
    def script_tag_filter(self, soup):
        scripts = soup.find_all("script")

        # Iterate over each <script> tag and print it
        for script in scripts:
            script = script.extract()
            self.inline_scripts.append(script.string)

        return soup

    # Inline Event Handlers
    def event_handler_filter(self, soup):
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
            "onwheel"
        ]
        tags = soup.find_all()

        for tag in tags:
            for attr, value in tag.attrs.items():
                if attr in event_handlers:
                    hash_func_name = hashlib.md5(value.encode()).hexdigest()
                    # JS Function must start with an char
                    hash_func_name = "f" + hash_func_name + "()"

                    new_function = "function " + hash_func_name + " { " + value + " }\n"

                    # modify tag’s attribute
                    tag.attrs[attr] = hash_func_name

                    # append new function to script List
                    if new_function not in self.inline_scripts:
                        self.inline_scripts.append(new_function)

        return soup

# JavaScript in HTML Attributes


# Dynamic Inline Script Generation
