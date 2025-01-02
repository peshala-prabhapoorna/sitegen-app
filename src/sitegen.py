import sys

from gencontent import generate_page
from template import template


def generate(markdown):
    return generate_page(markdown, template)

if __name__ == '__main__':
    markdown = sys.argv[1]
    print(generate(markdown))
