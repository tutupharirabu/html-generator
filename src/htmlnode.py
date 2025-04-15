class HTMLNode:
    """
    A class representing an HTML node.

    Attributes:
        tag (str): A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        value (str): A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        children (list): A list of HTMLNode objects representing the children of this node
        props (dict): A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    """

    def __init__ (self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html (self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html (self):
        if self.props is None:
            return ""
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])
    
    def __repr__ (self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__ (self, tag, value, props=None):
        super(LeafNode, self).__init__(tag, value, None, props)
    
    def to_html (self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        
        if self.tag is None:
            return self.value
        
        if self.props:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        
        return f"<{self.tag}>{self.value}</{self.tag}>"
  
    def __repr__ (self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
  
class ParentNode(HTMLNode):
    def __init__ (self, tag, children, props=None):
        super(ParentNode, self).__init__(tag, None, children, props)
    
    def to_html (self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        
        if self.children is None:
            raise ValueError("invalid HTML: no children")
        
        return f"<{self.tag}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"
    
    def __repr__ (self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"