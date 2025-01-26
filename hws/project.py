import string

def load_ascii_art(file_path):
    ascii_map = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().strip()
        blocks = content.split("\n\n")
        characters = string.ascii_uppercase

        for i, block in enumerate(blocks):
            lines = block.split("\n")
            if i < len(characters):
                char = characters[i]
                ascii_map[char] = lines

    return ascii_map

def print_ascii_text(text, ascii_map):
    lines = [""] * 8
    for char in text:
        ascii_art = ascii_map.get(char.upper(), ascii_map.get('?'))
        if ascii_art:
            for i in range(8):
                lines[i] += ascii_art[i] + "  "
    print("\n".join(lines))

def main():
    ascii_file = "/Users/alibidanov/Downloads/standard.txt"
    ascii_map = load_ascii_art(ascii_file)

    user_input = input("Enter text: ")

    print_ascii_text(user_input, ascii_map)

if __name__ == "__main__":
    main()