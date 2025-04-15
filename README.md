# HTML Generator

A simple, flexible library for programmatically generating HTML content in Python.

## Overview

This project provides a set of classes and utilities to create HTML content using Python objects. Instead of writing HTML markup directly, you can create nodes with specific properties and convert them to valid HTML.

## Components

### HTMLNode System

- **HTMLNode**: Base class with common functionality for all HTML elements
- **LeafNode**: For elements without children (e.g., `<p>`, `<a>`, `<img>`) 
- **ParentNode**: For elements with children (e.g., `<div>`, `<section>`)

### TextNode System

A higher-level abstraction for working with different types of text content:

- **TextType**: Enum for categorizing text (regular text, bold, italic, code, links, images)
- **TextNode**: Represents text content with a specific type and optional URL
- **text_node_to_html_node()**: Converts TextNodes to appropriate HTMLNodes

## Usage Examples

### Creating simple HTML elements

```python
from htmlnode import LeafNode, ParentNode

# Create a paragraph
paragraph = LeafNode("p", "This is a paragraph")
html = paragraph.to_html()  # <p>This is a paragraph</p>

# Create a link
link = LeafNode("a", "Click me", {"href": "https://example.com"})
html = link.to_html()  # <a href="https://example.com">Click me</a>

# Create nested structures
parent = ParentNode("div", [
    LeafNode("h1", "Title"),
    LeafNode("p", "Content")
])
html = parent.to_html()  # <div><h1>Title</h1><p>Content</p></div>
```

### Working with TextNodes

```python
from textnode import TextNode, TextType, text_node_to_html_node

# Create different types of text
regular_text = TextNode("Regular text", TextType.TEXT)
bold_text = TextNode("Bold text", TextType.BOLD)
link = TextNode("Visit our site", TextType.LINK, "https://example.com")
image = TextNode("Image description", TextType.IMAGE, "https://example.com/image.jpg")

# Convert to HTMLNodes
html_node = text_node_to_html_node(link)
html = html_node.to_html()  # <a href="https://example.com">Visit our site</a>
```

## Running the Project

### Requirements

- Python 3.10 or higher (for pattern matching)

### Running the Main Script

```bash
# From the root directory
./main.sh
# or
python3 src/main.py
```

### Running Tests

```bash
# From the root directory
./test.sh
# or
python3 -m unittest discover -s src
```

## Project Structure

```
.
├── .gitignore
├── main.sh              # Script to run the main program
├── test.sh              # Script to run all tests
└── src/
    ├── htmlnode.py      # Base HTML node classes
    ├── textnode.py      # Text node system
    ├── main.py          # Main entry point
    ├── test_htmlnode.py
    ├── test_leaf_htmlnode.py
    ├── test_parent_htmlnode.py
    └── test_textnode.py
```

## Extending the Project

You can extend this project in several ways:
- Add support for more HTML tags and attributes
- Create a higher-level API for building common HTML structures
- Implement a markdown-to-HTML converter using this framework
- Build a complete static site generator
