#!/usr/bin/env python
import json


FILENAME_TEMPLATE = "{directory}/{name}.html"
PAGE_TEMPLATE = """---
layout: {layout}
location: {location}
---"""


def main():
    with open("towns.json") as f:
        data = json.load(f)
        towns = data['towns']
        pages = data['pages']

        for page in pages:
            for town in towns:
                filename = FILENAME_TEMPLATE.format(directory=page['directory'], name=town['name'])
                rendered_template = PAGE_TEMPLATE.format(layout=page['layout'], location=town['location'])

                with open(filename, 'w') as page_file:
                    page_file.write(rendered_template)


if __name__ == "__main__":
    main()
