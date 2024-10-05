import re
import csv
import subprocess
import argparse

# Command line arg
parser = argparse.ArgumentParser(description='Build Codelabs')
parser.add_argument('--test', action=argparse.BooleanOptionalAction, default=True, help='Enabled to build in a test directory prior to overwriting root. Default behavior is to ALWAYS build in a test directory. Disable to add to root /docs dir.')

args = parser.parse_args()
if args.test:
    root = "./test"
else:
    root = "."

# claat build and CSV information
def run(row):
    doc_id = re.search(r"https://docs\.google\.com/document/d/([a-zA-Z0-9_-]+)", row['Google Doc URL']).group(1)
    command = ["./claat", "export", "-o", f"{root}{row['url_loc']}", doc_id]
    out = subprocess.run(command, capture_output=False, text=False, check=False)
    return out

data = []
with open('docs.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)
        run(row)

# Redirect and HTML processing
for row in data:
    # Redirect processing
    if row['title'] != '':
        with open(f"{root}{row['url_loc']+row['url_name']}/redirect.md", "w") as file:
            # Write some text to the file
            yaml = "---\n" + \
                   f"title: {row['title']}\n" + \
                   f"parent: {row['parent']}\n" + \
                   ('' if row['grand_parent'] == '' else f"grand_parent: {row['grand_parent']}\n") + \
                   f"nav_order: {row['nav_order']}\n" + \
                   f"permalink: {row['url_loc']+row['url_name']}/\n" + \
                   "---\n\n" + \
                   "{% include_relative index.html %}"
                
            file.write(yaml)

    # HTML update
    with open(f"{root}{row['url_loc']+row['url_name']}/index.html", "r") as file:
        original_html = file.read()

    # Append favicon data
    new_favicon_line = '<link rel="icon" type="image/png" href="/assets/images/favicon.ico"/>'
    insert_position = original_html.find('<meta charset="UTF-8">') + len('<meta charset="UTF-8">')
    modified_html = original_html[:insert_position] + '\n  ' + new_favicon_line + original_html[insert_position:]

    # Append redirect script
    new_script = '  <script>\n' + \
        '    // This is to override the close / done handling on the page\n' + \
        '    // https://github.com/googlecodelabs/tools/issues/103\n' + \
        '    document.addEventListener("DOMContentLoaded", function() {\n' + \
        f'      document.getElementById("arrow-back").href="{row["redirect"]}";\n' + \
        '      document.getElementById("arrow-back").addEventListener( "click", function() {\n' + \
        '        window.history.back();\n' + \
        '      });\n' + \
        f'      document.getElementById("done").href="{row["redirect"]}";\n' + \
        '      document.getElementById("done").addEventListener( "click", function() {\n' + \
        '        window.history.back();\n' + \
        '      });\n' + \
        '    }, false);\n' + \
        '  </script>\n'

    insert_position = modified_html.rfind('</body>')
    modified_html = modified_html[:insert_position] + new_script + modified_html[insert_position:]
    with open(f"{root}{row['url_loc']+row['url_name']}/index.html", "w") as file:
        file.write(modified_html)
