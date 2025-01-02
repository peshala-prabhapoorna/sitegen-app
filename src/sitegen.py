import sys

from gencontent import generate_page


template_path = "./template.html"


def generate(markdown):
    return generate_page(markdown, template_path)

if __name__ == '__main__':
    markdown = sys.argv[1]
    print(generate(markdown))
