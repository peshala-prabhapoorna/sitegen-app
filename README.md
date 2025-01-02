# SiteGen: Wheel Package

SiteGen is a static site generator that converts markdown formatted text into  
an HTML formatted static web page.

Markdown syntaxt that the application can handle are listed below:
1. Headings
2. Paragraphs
3. Code Blocks
4. Unordered Lists
5. Ordered Lists
6. Quotes
7. Links
8. Embedded Links
9. Inline Code
10. Bold Text
11. Italic Text

Other types of markdown syntax will be parsed as normal text.

## How to Use the Package

Install the package by downloading the latest release. Then import the package  
to use it.

## Build and Run the package

Clone the repository and from the root of the repository run the commands below.

1. Build the package:
```sh
python3 -m build
```

2. Create and activate a virtual environment:
```sh
# create
virtualenv venv

# activate
source venv/bin/activate
```

3. Install the package:
```sh
pip install dist/PACKAGE
```

4. Run the package:
```py
>>>from sitegen import sitegen
>>>sitegen.generate(MARKDOWN)
```

## Test the Package

Use the `test.sh` script to run the unit tests to test the application.  
```bash
./test.sh
```
