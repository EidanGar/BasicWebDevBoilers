import os

file_name = str(input("File Name: "))
html = file_name + ".html"
css = file_name + ".css"
javascript = file_name + ".js"

boiler = ["<!DOCTYPE html>\n", "<html lang=\"en\">\n", "    <head>\n", "        <meta charset=\"utf-8\">\n", "        <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n", "        <title></title>\n", "        <meta name=\"description\" content=\"\">\n", "        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n", f"        <link rel=\"stylesheet\" href=\"{css}\">\n", "    </head>\n", "    <body>\n",  f"        <script src=\"{javascript}\" async defer></script>\n", "    </body>\n", "</html>\n"]

with open(html, "w") as html_file:
    html_file.writelines(boiler)
    if os.path.exists(html):
        print(f"{html} has been created successfully.")
    else:
        print(f"Failed to create {html} file.")

css_boiler = ['* { \n', '\tbox-sizing: border-box;\n', '}\n', 'html, body {\n', '\tmin-height: 100%;\n', '\tbackground: #fff;\n', '\tcolor: #000;\n', '}\n', '\t\n', 'body {\n', '\tfont-size: 1.4rem;\n', '\ttext-rendering: optimizeLegibility;\n', '}\n', '\t\n', 'body, ul, ol, dl {\n', '\tmargin: 0;\n', '}\n', 'article, aside, audio, \n', 'footer, header, nav, section, video {\n', '\tdisplay: block; \n', '\t}\n', '\t\n', '\t\n', 'h1 {\n', '\tfont-size: 1.4rem;\n', '}\n', '\t\n', 'p { \n', '\t-ms-word-break: break-all;\n', '\tword-break: break-all;\n', '\tword-break: break-word;\n', '\t-moz-hyphens: auto;\n', '\t-webkit-hyphens: auto;\n', '\t-ms-hyphens: auto;\n', '\thyphens: auto;\n', '} \n', '\t\n', 'textarea { \n', '\tresize: vertical;\n', '}\n', ' \n', 'table { border-collapse: collapse; }\n', 'td {\n', '\tpadding: .5rem;\n', '}\n', '\t\n', 'img { \n', '\tborder: none;\n', '\tmax-width: 100%;\n', '}\n', '\t\n', 'input[type="submit"]::-moz-focus-inner, \n', '\tinput[type="button"]::-moz-focus-inner {\n', '\t\tborder : 0px;\n', '\t}\n', '\t\n', 'input[type="search"] { \n', '\t-webkit-appearance: textfield;\n', '} \n', 'input[type="submit"] { \n', '\t-webkit-appearance:none;\n', '}\n', '\t\n', 'input:required:after {\n', '\tcolor: #f00;\n', '\tcontent: " *";\n', '}\n', '\n', 'input[type="email"]:invalid { \n', '\tbackground: #f00;\n', '}\n', '\t\n', '.right { \n', '\tfloat: right;\n', '\tmargin-left: 2rem;\n', '\tclear: right;\n', '}\n', '.left { \n', '\tfloat: left;\n', '\tmargin-right: 2rem;\n', '\tclear: left;\n', '}']

with open(css, "w") as css_file:
    css_file.writelines(css_boiler)
    if os.path.exists(css):
        print(f"{css} has been created successfully.")
    else:
        print(f"Failed to create {css} file.")
        os.remove(html)

with open(javascript, "x") as javascript_file:
        print(f"{javascript} has been created successfully.")

if os.path.exists(javascript) == False:
    print(f"Failed to create {javascript} file.")
    os.remove(html)
    os.remove(css)