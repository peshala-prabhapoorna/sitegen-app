# Static Site Generator
This application converts markdown documents to html format. Markdown  
syntaxt that the application can handle are listed below:
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
