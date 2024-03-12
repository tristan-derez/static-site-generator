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


def block_to_block_type(block):
    lines = block.split("\n")
    heading_prefixes = ["# ", "## ", "### ", "#### ", "##### ", "###### "]

    if any(block.startswith(prefix) for prefix in heading_prefixes):
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
