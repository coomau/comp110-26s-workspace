"""EX03 - Wordle - Wordle."""

__author__: str = "730736150"


def input_guess(secret_word_len: int) -> str:
    guess = input(f"Enter a {secret_word_len} character word: ")
    while len(guess) != secret_word_len:
        guess = input(
            f"That wasn't {secret_word_len} chars! Try again: "
        )  # I do not love adding these little spaces at the end of my stings, sometimes I'll forget it and I'll redo do it thinking something else is wrong...
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks if the single-character string char_guess is found anywhere within the secret_word."""
    assert (
        len(char_guess) == 1
    )  # I didn't reall know what to do until i read your expected results and then took the assert function from there.
    index = 0
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        index += 1
    return False


WHITE_BOX: str = "\U00002b1c"  # just straight copy paste on these things.
GREEN_BOX: str = "\U0001f7e9"
YELLOW_BOX: str = "\U0001f7e8"


def emojified(guess: str, secret: str) -> str:
    """Returns emojis showing how each character of guess compares to the secret."""
    assert len(guess) == len(secret)
    result: str = ""  # I love adding these little guys, makes things much easier.
    index: int = 0
    while index < len(secret):
        if (
            guess[index] == secret[index]
        ):  # Once i got this first one down the other three were pretty easy.
            result += GREEN_BOX
        elif contains_char(secret, guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1
    return result


def main(secret: str) -> None:
    """The main game loop."""  # haha the game
    turns: int = (
        1  # I initially started this at zero till i realized you can't play without having taken a turn.
    )
    max_turns: int = 6
    won: bool = False
    while turns <= max_turns and not won:
        print(f"=== Turn {turns}/{max_turns} ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            won = True
        else:
            turns += 1
    if won:
        print(f"You won in {turns}/{max_turns} turns!")  # I loveeee f strings.
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
