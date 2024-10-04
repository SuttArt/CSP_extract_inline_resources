class JSExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        # List of <script> tags; each object is of type `bs4.element.Script`
        self.inline_scripts = []

    def __write_js_file(self, content):
        with open(self.file_path, 'a') as f:
            f.write(content)

    #Inline <script> Tag
    def script_tag_filter(self, soup):
        scripts = soup.find_all("script")

        # Iterate over each <script> tag and print it
        for script in scripts:
            script = script.extract()
            self.inline_scripts.append(script.string)
            self.__write_js_file(script.string)

        return soup

#Inline Event Handlers


#JavaScript in HTML Attributes


#Dynamic Inline Script Generation
