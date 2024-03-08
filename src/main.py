from textnode import TextNode

def main():
    node1 = TextNode("Hello", "normal")
    node2 = TextNode("World", "bold", "https://example.com")
    print(node1)
    print(node2)


main()