from generate_server import(
    generate_pages_recursive
)

from static_public import(
    source_to_destination
)

def main():
    '''
    FROM_PATH = "content/index.md"
    TEMPLATE_PATH = "template.html"
    DEST_PATH = "public/index.html"

    FROM_PATH_GLOR = "content/blog/glorfindel/index.md"
    DEST_PATH_GLOR = "public/blog/glorfindel/index.html"
    FROM_PATH_TOM = "content/blog/tom/index.md"
    DEST_PATH_TOM = "public/blog/tom/index.html"
    FROM_PATH_MAJESTY = "content/blog/majesty/index.md"
    DEST_PATH_MAJESTY = "public/blog/majesty/index.html"
    FROM_PATH_CONTACT = "content/contact/index.md"
    DEST_PATH_CONTACT = "public/contact/index.html"

    SOURCE = "static/"
    DESTINATION = "public/"

    source_to_destination(SOURCE, DESTINATION)
    generate_page(FROM_PATH, TEMPLATE_PATH, DEST_PATH)
    generate_page(FROM_PATH_GLOR, TEMPLATE_PATH, DEST_PATH_GLOR)
    generate_page(FROM_PATH_TOM, TEMPLATE_PATH, DEST_PATH_TOM)
    generate_page(FROM_PATH_MAJESTY, TEMPLATE_PATH, DEST_PATH_MAJESTY)
    generate_page(FROM_PATH_CONTACT, TEMPLATE_PATH, DEST_PATH_CONTACT)
    '''
    SOURCE = "static/"
    DESTINATION = "public/"
    CONTENT_PATH = "content/"
    TEMPLATE_PATH = "template.html"
    source_to_destination(SOURCE, DESTINATION)
    generate_pages_recursive(CONTENT_PATH, TEMPLATE_PATH, DESTINATION)

if __name__ == "__main__":
    main()
