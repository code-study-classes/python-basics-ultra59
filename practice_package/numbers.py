from pathlib import Path

get_filename_without_extension = lambda full_path: Path(Path(full_path).stem).stem  # noqa: E731


def shuffle_sentence_characters(original_sentence):
    odd_pos_chars = []
    even_pos_chars_reversed = []
    for char_index in range(len(original_sentence)):
        if char_index % 2 == 0:
            even_pos_chars_reversed.insert(0, original_sentence[char_index])
        else:
            odd_pos_chars.append(original_sentence[char_index])
    return ''.join(odd_pos_chars) + ''.join(even_pos_chars_reversed)


def validate_parentheses(bracket_expression):
    opened_count = 0
    closed_count = 0
    error_pos = 0
    for current_pos in range(len(bracket_expression)):
        if bracket_expression[current_pos] != ' ':
            error_pos += 1
        if bracket_expression[current_pos] == '(':
            opened_count += 1
        elif bracket_expression[current_pos] == ')':
            closed_count += 1
        if closed_count > opened_count:
            return error_pos
    return -1 if opened_count > closed_count else 0


def reverse_domain_parts(domain_string):
    return '.'.join(domain_string.split('.')[::-1])


VOWEL_LETTERS = {'a', 'e', 'i', 'o', 'u', 'y'}


def count_consecutive_vowels(input_word):
    vowel_group_counter = 0
    in_vowel_sequence = False
    for current_char in input_word.lower():
        if current_char in VOWEL_LETTERS:
            if not in_vowel_sequence:
                vowel_group_counter += 1
                in_vowel_sequence = True
        else:
            in_vowel_sequence = False
    return vowel_group_counter