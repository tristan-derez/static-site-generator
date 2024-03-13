import re
from htmlnode import ParentNode
from inline_md import text_to_textnodes
from textnode import text_node_to_html_node

blocktype_paragraph = "paragraph"
blocktype_heading = "heading"
blocktype_code = "code"
blocktype_quote = "quote"
blocktype_ulist = "unordered_list"
blocktype_olist = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    filtered_blocks = []

    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)

    return filtered_blocks


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == blocktype_paragraph:
        return paragraph_to_html_node(block)
    if block_type == blocktype_heading:
        return heading_to_html_node(block)
    if block_type == blocktype_code:
        return code_to_html_node(block)
    if block_type == blocktype_olist:
        return olist_to_html_node(block)
    if block_type == blocktype_ulist:
        return ulist_to_html_node(block)
    if block_type == blocktype_quote:
        return quote_to_html_node(block)
    raise ValueError("Unknown block type")


def block_to_block_type(block):
    lines = block.split("\n")

    if re.match(r"^#+\s", block):
        return blocktype_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return blocktype_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return blocktype_paragraph
        return blocktype_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return blocktype_paragraph
        return blocktype_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return blocktype_ulist
        return blocktype_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return blocktype_paragraph
            i += 1
        return blocktype_olist

    return blocktype_paragraph


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)
