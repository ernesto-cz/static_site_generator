import sys

from generate_server import(
    generate_pages_recursive
)

from static_public import(
    source_to_destination
)

def main():
    base_path = sys.argv[1] if len(sys.argv) == 2 else '/'
    SOURCE = "static/"
    DESTINATION = "docs/"
    CONTENT_PATH = "content/"
    TEMPLATE_PATH = "template.html"
    source_to_destination(SOURCE, DESTINATION)
    generate_pages_recursive(CONTENT_PATH, TEMPLATE_PATH, DESTINATION, base_path)

if __name__ == "__main__":
    main()
