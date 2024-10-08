import uuid  # Importing uuid for generating unique IDs for HTML elements


class JSExtractor:
    def __init__(self, file_path):
        # Path where the extracted JavaScript will be saved
        self.file_path = file_path
        # List to store the contents of extracted <script> tags and generated functions
        self.inline_scripts = []

    # Private method to create event listener JavaScript code for a given element ID, event type, and content
    def __create_event_listener(self, id, event, content):
        event_listener = ("document.getElementById('" + id + "').addEventListener('" + event
                          + "', function(event) { " + content + " })\n")
        return event_listener

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
        # Event handler mapping from attribute to event:
        event_handlers = {
            "onabort": "abort",
            "onauxclick": "auxclick",
            "onbeforeinput": "beforeinput",
            "onbeforematch": "beforematch",
            "onbeforetoggle": "beforetoggle",
            "oncancel": "cancel",
            "oncanplay": "canplay",
            "oncanplaythrough": "canplaythrough",
            "onchange": "change",
            "onclick": "click",
            "onclose": "close",
            "oncontextlost": "contextlost",
            "oncontextmenu": "contextmenu",
            "oncontextrestored": "contextrestored",
            "oncopy": "copy",
            "oncuechange": "cuechange",
            "oncut": "cut",
            "ondblclick": "dblclick",
            "ondrag": "drag",
            "ondragend": "dragend",
            "ondragenter": "dragenter",
            "ondragleave": "dragleave",
            "ondragover": "dragover",
            "ondragstart": "dragstart",
            "ondrop": "drop",
            "ondurationchange": "durationchange",
            "onemptied": "emptied",
            "onended": "ended",
            "onformdata": "formdata",
            "oninput": "input",
            "oninvalid": "invalid",
            "onkeydown": "keydown",
            "onkeypress": "keypress",
            "onkeyup": "keyup",
            "onloadeddata": "loadeddata",
            "onloadedmetadata": "loadedmetadata",
            "onloadstart": "loadstart",
            "onmousedown": "mousedown",
            "onmouseenter": "mouseenter",
            "onmouseleave": "mouseleave",
            "onmousemove": "mousemove",
            "onmouseout": "mouseout",
            "onmouseover": "mouseover",
            "onmouseup": "mouseup",
            "onpaste": "paste",
            "onpause": "pause",
            "onplay": "play",
            "onplaying": "playing",
            "onprogress": "progress",
            "onratechange": "ratechange",
            "onreset": "reset",
            "onscrollend": "scrollend",
            "onsecuritypolicyviolation": "securitypolicyviolation",
            "onseeked": "seeked",
            "onseeking": "seeking",
            "onselect": "select",
            "onslotchange": "slotchange",
            "onstalled": "stalled",
            "onsubmit": "submit",
            "onsuspend": "suspend",
            "ontimeupdate": "timeupdate",
            "ontoggle": "toggle",
            "onvolumechange": "volumechange",
            "onwaiting": "waiting",
            "onwebkitanimationend": "webkitAnimationEnd",
            "onwebkitanimationiteration": "webkitAnimationIteration",
            "onwebkitanimationstart": "webkitAnimationStart",
            "onwebkittransitionend": "webkitTransitionEnd",
            "onwheel": "wheel",
            #
            "onblur": "blur",
            "onerror": "error",
            "onfocus": "focus",
            "onload": "load",
            "onresize": "resize",
            "onscroll": "scroll",
            #
            "onafterprint": "afterprint",
            "onbeforeprint": "beforeprint",
            "onbeforeunload": "beforeunload",
            "onhashchange": "hashchange",
            "onlanguagechange": "languagechange",
            "onmessage": "message",
            "onmessageerror": "messageerror",
            "onoffline": "offline",
            "ononline": "online",
            "onpageswap": "pageswap",
            "onpagehide": "pagehide",
            "onpagereveal": "pagereveal",
            "onpageshow": "pageshow",
            "onpopstate": "popstate",
            "onrejectionhandled": "rejectionhandled",
            "onstorage": "storage",
            "onunhandledrejection": "unhandledrejection",
            "onunload": "unload",
            #
            "onreadystatechange": "readystatechange",
            "onvisibilitychange": "visibilitychange"
        }

        # Find all tags in the HTML
        tags = soup.find_all()

        # Iterate through each tag and check if it has any event handler attributes
        for tag in tags:
            # Iterate over a copy of tag.attrs.items() to avoid modifying the dictionary during iteration
            for attr, value in list(tag.attrs.items()):
                if attr in event_handlers:
                    if 'id' not in tag.attrs:
                        # Generate a UUID (random-based UUID) for the HTML tag if it does not have an ID
                        unique_id = uuid.uuid4()

                        # Convert the UUID to string and prefix with "id_" to ensure it's a valid HTML ID
                        html_id = f"id_{unique_id}"

                        tag["id"] = html_id  # Assign the generated ID to the tag

                    # Remove the tag’s inline event handler attribute (e.g., onclick, onmouseover)
                    del tag.attrs[attr]

                    # Create an event listener function using the tag's ID, the event type, and the inline script
                    # content
                    new_function = self.__create_event_listener(tag["id"], event_handlers[attr], value)

                    # Append the new function to the inline_scripts list, if it hasn't been added already
                    if new_function not in self.inline_scripts:
                        self.inline_scripts.append(new_function)

        # Return the modified HTML with event handlers replaced by function calls
        return soup

    # Handle inline JavaScript in URLs and extract their JavaScript
    # For details:
    # https://developer.mozilla.org/en-US/docs/Web/URI/Schemes/javascript
    # https://html.spec.whatwg.org/multipage/browsing-the-web.html#the-javascript:-url-special-case
    # javascript: URLs can be used anywhere a URL is a navigation target. This includes, but is not limited to:
    # The href attribute of an <a> or <area> element.
    # The action attribute of a <form> element.
    # The src attribute of an <iframe> element.
    # The window.location JavaScript property.
    # The browser address bar itself.
    def js_url_filter(self, soup):
        # Find all tags in the HTML
        tags = soup.find_all()
        elements = {
            "href": "click",
            "action": "submit",
            # src should not be used with combination of JS, we don't really hande this case
            "src": "load"
        }

        # Iterate through each tag and check if it has any event handler attributes
        for tag in tags:
            # Iterate over a copy of tag.attrs.items() to avoid modifying the dictionary during iteration
            for attr, value in list(tag.attrs.items()):
                if attr in elements:
                    if tag[attr].startswith("javascript:"):
                        if 'id' not in tag.attrs:
                            # Generate a UUID (random-based UUID) for the HTML tag if it does not have an ID
                            unique_id = uuid.uuid4()

                            # Convert the UUID to string and prefix with "id_" to ensure it's a valid HTML ID
                            html_id = f"id_{unique_id}"

                            tag["id"] = html_id  # Assign the generated ID to the tag

                        value = value.replace("javascript:", "", 1)
                        value = "event.preventDefault(); " + value

                        if attr == "href":
                            tag[attr] = "#"
                        elif attr == "action":
                            del tag.attrs[attr]
                        elif attr == "src":
                            tag[attr] = "about:blank"

                        # Create an event listener function using the tag's ID, the event type, and the inline script
                        # content
                        new_function = self.__create_event_listener(tag["id"], elements[attr], value)

                        # Append the new function to the inline_scripts list, if it hasn't been added already
                        if new_function not in self.inline_scripts:
                            self.inline_scripts.append(new_function)

        # Return the modified HTML with event handlers replaced by function calls
        return soup

# Dynamic Inline Script Generation

# Note: It is possible that one or more of the scripts may utilize Dynamic Inline Script Generation, which is not yet
# covered in this tool due to time constraints. To fully handle this, a deep JavaScript parser would be required,
# potentially involving the generation and analysis of the JavaScript Abstract Syntax Tree (AST).

# Examples:

# document.write('<script>alert("This is dynamically generated")</script>');
# document.body.innerHTML += '<script>alert("Dynamic inline script")</script>';

# var scriptContent = "alert('Executed dynamically using eval!');";
# eval(scriptContent);

# var dynamicFunc = new Function('alert("Dynamic function executed")');
# dynamicFunc();

# var script = document.createElement('script');
# script.textContent = 'console.log("Dynamic script executed")';
# document.body.appendChild(script);

# <script src="https://example.com/data?callback=myFunction"></script>
# <script>
#   function myFunction(data) {
#     console.log('Received data: ', data);
#   }
# </script>

# var button = document.createElement('button');
# button.innerHTML = 'Click me';
# button.onclick = function() {
#   alert('Dynamically added inline event handler');
# };
# document.body.appendChild(button);
