def get_num_words(book_text: str) -> int:
    words = book_text.split()
    return len(words)


def get_character_counts(book_text : str) -> dict[str, int]:
    character_dict = {}
    for character in book_text:
        c = character.lower()
        if c in character_dict:
            character_dict[c] += 1
        else:
            character_dict[c] = 1

    return character_dict

"""
When sorting tuples, Python normally compares the first value first, then the second value if there's a tie. So we could store our data as (count, character) and sort it without a key:
chars = [
    (4868, "b"),
    (44538, "e"),
    (25894, "a"),
]

print(sorted(chars, reverse=True))
# [(44538, 'e'), (25894, 'a'), (4868, 'b')]

For BookBot, we'll keep each tuple as (character, count) because that shape is easier to read. The key=sort_on argument lets us sort by count without rearranging the data to fit Python's default tuple sorting behavior.
"""
def sort_on(tup : tuple[str, int]) -> int:
    return tup[1]


def chars_dict_to_sorted_list(character_dict : dict[str, int]) -> list[tuple[str, int]]:
    chars_list = []
    for char in character_dict:
        count = character_dict[char]
        chars_list.append((char, count))

    sorted_chars_list = sorted(chars_list, reverse=True, key=sort_on)
    return sorted_chars_list

