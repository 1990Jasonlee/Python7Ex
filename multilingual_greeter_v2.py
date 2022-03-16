from typing import Dict

# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = {1: 'English\n', 2: 'Spanish\n'
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = {1: 'What is your name?', 2: '¿Cómo te llamas'
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
greetings_dict = {1: 'Hello', 2: 'Hola'
}


def print_language_options(lang_options: Dict[int, str]) -> None:
    """
    Given a dictionary, this functions iterates through the values and prints them out.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language
    :return: None
    """
    print('Please choose a language: ')
    for key, value in lang_options.items():
        print(f'{key}: {value}')

def language_input() -> int:
    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """
    language = input('Please choose a language: ')
    return int(language)

def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    """
    This method determines if the choice the user made is valid.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language

    :param lang_choice: An integer representing the value the user selected
    :return: A boolean representing the validity of the lang_choice
    """
    if lang_choice in lang_options.keys():
        return True
    else:
        return False

def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """
    return name_prompt_options.get(lang_choice)


def name_input(name_prompt: str) -> str:
    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """
    return input(name_prompt)


def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    """
    Using the parameters provided, this function greets the user.

    :param name: The name the user provided
    :param greetings_options: A dictionary where the key is an integer representing a greeting and the value is a string
    with a greeting in the user's chosen language
    :param lang_choice: The language the user has chosen.
    :return:
    """
    print(greetings_options[lang_choice], name)


def prompt():
    mode = input('1: Admin Mode or 2: User Mode ')
    if mode == '1':
        admin()
    elif mode == '2':
        user()
    else:
        print('Invalid Choice')

def admin():
    mode2 = input('1: Add Language or 2: Change Language ')
    add_language = input('Enter new language: ')
    add_ask = input('Enter "What is your name? " in new language: ')
    add_greeting = input('Enter "Hello " in new language')
    new = len(lang_dict) + 1

    new_language = {new:add_language}
    new_ask = {new:add_ask}
    new_greeting = {new:add_greeting}

    lang_dict.update(new_language)
    name_prompt_dict.update(new_ask)
    greetings_dict.update(new_greeting)

def user():
    print_language_options(lang_dict)
    chosen_lang = language_input()
    while language_choice_is_valid(lang_dict, chosen_lang) is False:
        print("Invalid selection. Try again.")
        chosen_lang = language_input()

    selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
    chosen_name = name_input(selected_prompt)
    greet(chosen_name, greetings_dict, chosen_lang)

prompt()