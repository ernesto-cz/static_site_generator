from enum import Enum


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGES = "images"


class TextNode():

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url):
            return True

        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    '''
    def __select_type(self, text_type):
          match text_type:
              case TextType.NORMAL.value:
                  return TextType.NORMAL
              case TextType.ITALIC.value:
                  return TextType.ITALIC
              case TextType.CODE.value:
                  return TextType.CODE
              case TextType.LINK.value:
                  return TextType.LINK
              case TextType.IMAGES.value:
                  return TextType.IMAGES
              case _:
                  raise ValueError("not a valid text_type")
    '''
