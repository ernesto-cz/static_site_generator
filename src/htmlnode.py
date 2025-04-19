class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError("🛠️ still working on it 🐍")

    def props_to_html(self):
        if self.props is None:
            return ""
        return "".join(
            map(lambda kv: f' {kv[0]}="{kv[1]}"', self.props.items())
        )
