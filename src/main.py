from textnode import TextNode, TextType


def main():
    text = TextNode("Some text", TextType.LINK, "https://www.google.com")
    print(text)


if __name__ == "__main__":
    main()
