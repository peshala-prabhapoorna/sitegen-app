# SiteGen: Static Site Generator

SiteGen is a static site generator that converts markdown formatted text files  
and static content attached to them into a HTML formatted static web page.

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
## How to use the application
- Place the markdown files that you want to convert to html in the `content`  
directory.

The generated html files will follow the directory structure inside the  
`content` directory. Getting directory structure correct is import for the  
links in the final result to work. 

- Place the static files attached to the markdown files inside the `static`  
directory. The static files in the `static` directory should follow the  
directory structure as used in the markdown files. Otherwise the files will  
be unreachable for the generated static (HTML) sites.  

- Run the `main.sh` script.
```bash
./main.sh
```
This will run the application and generate the markdown conetnt in the  
`public` folder. Then it will serve the content inside the `public`  
directory using the `http.server` module in the Python.
## Test the application
Use the `test.sh` script to run the unit tests to test the application.  
```bash
./test.sh
```
