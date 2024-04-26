from typing import List
import random
import math

def create_alphabet_soup(alph_len: int) -> List[str]:
    """
    Creates alphabet soup based on input length

    Args:
        alph_len: length of alphabet soup
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_str = []
    for _ in range(alph_len):
        index_random = random.randint(0, len(alphabet) - 1)
        picked_letter = alphabet[index_random]
        final_str.append(picked_letter)
    return final_str


def get_dict_frequency_input_word(input_word: str) -> dict:
    """
    Creates a dict where keys are each letter of word to spell
    and values are the frequency of each letter within same word

    Args:
        input_word: word to process
    """
    map_input_word_letter_freq = {}
    for lett in input_word:
        map_input_word_letter_freq[lett] = map_input_word_letter_freq[lett] + 1 if map_input_word_letter_freq.get(lett) else 1
    return map_input_word_letter_freq


def find_useful_letters_based_on_word(map_word: dict) -> dict:
    """
    Creates dict where keys are each letter of word to spell
    and values are the frequency of each letter within alphabet soup

    Args:
        map_word: dict of word to spell
    """
    map_useful_letters = {key: 0 for key, _ in map_word.items()} # dict comprehension to replicate dict but with 0 as values
    for letter in alphabet_soup: # O(n) time complexity
        if map_word.get(letter): # use of get to avoid keyError / access dicts is O(1)
            map_useful_letters[letter] = map_useful_letters[letter] + 1
    return map_useful_letters


if __name__ == '__main__':
    word_to_spell = 'pennymac'
    alphabet_soup = create_alphabet_soup(300)

    map_input_word_letter_freq = get_dict_frequency_input_word(word_to_spell)

    map_useful_letters = find_useful_letters_based_on_word(map_input_word_letter_freq)
    
    list_quotient_per_letter = [
        math.floor(map_useful_letters[letter] / map_input_word_letter_freq[letter])
        for letter in map_useful_letters.keys()
    ] # this iteration (list comprehension) is O(7) for word = pennymac (in practice is O(1) - constant time complexity)

    number_of_times_to_spell_pennymac = min(list_quotient_per_letter) # find lower number in quotients
    print(f'The number of times we can spell Pennymac is: {number_of_times_to_spell_pennymac}')
