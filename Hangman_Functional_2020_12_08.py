from typing import List

from words import WORD_LIST
import random


def main():
    ATTEMPTS_ALLOWED = 6

    secret_word = get_random_word(WORD_LIST)

    correct_guesses = []
    incorrect_guesses = []
    lives = calc_attempts_remaining(ATTEMPTS_ALLOWED, incorrect_guesses)

    result = None
    while result is None:

        # display lives left
        print_lives_left(lives, ATTEMPTS_ALLOWED)

        # display hidden word
        blanked_word = reveal_letters(secret_word, correct_guesses)
        print(blanked_word)
        print()

        # get guess
        guess = get_guess(correct_guesses + incorrect_guesses)

        if letter_is_in_word(guess, secret_word):
            print("That is correct!")
            correct_guesses.append(guess)
        else:
            print("Incorect.")
            incorrect_guesses.append(guess)
        
        lives = calc_attempts_remaining(ATTEMPTS_ALLOWED, incorrect_guesses)
        
        if all_letters_present_in_list(secret_word, correct_guesses):
            result = "win"
        elif lives <= 0:
            result = "lose"

    print(word_reveal_message(secret_word))
    print(outcome_message(result))


def get_random_word(word_list: List[str]) -> str:
    """Gets a random word.
    
    Args: 
        word_list: the list from which to get the word.
    
    Returns:
        A single word.
    """
    return random.choice(word_list)


def print_lives_left(remaining: int, out_of: int):
    """Prints out lives-left info.
    
    Args:
        remaining: Remaining lives left.
        out_of: How many lives in total you start with.
    """
    return f"You have {remaining} lives remaining out of {out_of}"


def reveal_letters(word: str, visible_letters: List[str]) -> str:
    """Reveal the given letters in a hidden word.
    
    Args:
        word: The word whose letters need to be revealed.
        visible_letters: A list of letters that should be visible in the word.
    
    Returns:
        The word with visible letters shown and all others blanked-out.
    
    Example:
        If the word is "hello" and visible_letters is the list ['e', 'o'],
        The resulting string would be "_ e _ _ o". Separate each character
        with a space to make it easier to read.
    """
    temp = ""
    for i in range(len(word)):
        if word[i] in visible_letters:
            temp += word[i]
        else:
            temp += '_'
        temp += ' '
    return temp[0:len(temp)-1]



def calc_attempts_remaining(attempts_allowed: int, incorrect: List[str]) -> int:
    """Determine the number of guesses remaining.

    Based on the initial number of allowed attempts and the number
    of incorrect guesses.
    
    Args:
        attempts_allowed: The number of total allowed guesses.
        incorrect: A list containing all the incorrect guesses.
    
    Returns:
        How many remaining guesses the player has.
    """
    return attempts_allowed-len(incorrect)


def word_reveal_message(word: str) -> str:
    """Creates a message revealing the secret word.
    
    Args:
        word: the word being revealed.
    
    Returns:
        A message revealing the secret word.
    
    Example: 
        "The secret word was 'orange'."
    """
    return f"The secret word was '{word}'."


def outcome_message(result: str) -> str:
    """Creates a message based on the player's outcome.
    
    Args:
        result: Either 'win' or 'lose'.
    
    Returns:
        An appropriate message based on the player's outcome.
    """
    if result == "win":
        return "Good job, you won!"
    else:
        return "You lost, you suck..."


def get_guess(all_guesses: List[str]) -> str:
    """Gets a valid guess from the player.
    
    This function will ensure:
        - The user enters a single character.
        - The user enters a letter not already guessed.
        - The user enters a valid letter (use str.isalpha())
    
    Args:
        all_guesses: A list of all prervious guesses.
    
    Returns:
        A single letter, not already guessed.
    """
    
    while (True):
        ip = input().lower()
        if len(ip) > 1:
            print("Invalid input: Only enter one letter at a time.")
        elif ip.isalpha() == False:
            print("Invalid input: Only enter alphabetical letters.")
        elif ip in all_guesses:
            print("Invalid input: You've already guessed this letter.")
        else:
            return ip


def letter_is_in_word(letter: str, word: str) -> bool:
    """Determines if a given letter is in a word.
    
    Args:
        letter: The letter to search for.
        word: The word to search.
    
    Returns:
        True if the letter is in the word, False otherwise.
    """
    if letter in word:
        return True
    else:
        return False


def all_letters_present_in_list(word: str, letter_list: List[str]) -> bool:
    """Determines if all a word's letters are in a given list.
    
    For every letter in the given word, is it present in the
    given list of letters? True if so.

    Args:
        word: The word to check.
        letter_list: The letters of the word
    
    Returns:
        True if all the letters in the word are in the list of letters.
    """
    for i in range(len(word)):
        if word[i] not in letter_list:
            return False
    return True


if __name__ == "__main__":
    main()
