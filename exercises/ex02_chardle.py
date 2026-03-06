"""EX02 - Chardle - A cute step toward Wordle."""

__author__: str = "730736150"


def input_word() -> str:
    word = input(
        "Enter a 5-character word: "
    )  # I can't recall if this was mentioned in class, but I looked up how to directly reference the user's input using the input() thing
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()  # for some reason this keeps kicking me out of the workspace and I have to redefine everything, but the code still works as inteded so :/
    return word


def input_letter() -> str:
    letter = input(
        "Enter a single character: "
    )  # This one was far easier as I kinda just copy and pasted what I did before switching aroud what I'm checking for.
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()  # for some reason this keeps kicking me out of the workspace and I have to redefine everything, also I think it's marking my answers as wrong but the output should be perfect
    return letter


def contains_char(word: str, letter: str) -> None:
    print(f"Searching for {letter} in {word}")  # f strings sure do make printing easier
    matching = 0
    if word[0] == letter:
        print(f"{letter} found at index 0")
        matching += 1
    if word[1] == letter:
        print(f"{letter} found at index 1")
        matching += 1
    if word[2] == letter:
        print(f"{letter} found at index 2")
        matching += 1
    if word[3] == letter:
        print(f"{letter} found at index 3")
        matching += 1
    if word[4] == letter:
        print(f"{letter} found at index 4")
        matching += 1
    if (
        matching == 0
    ):  # I've run into an issue where this wants to keep going even id ==0 happens, so I implemented the exit command
        print(f"No instances of {letter} found in {word}")
        return

    if matching == 1:
        print(f"1 instance of {letter} found in {word}")
    else:
        print(f"{matching} instances of {letter} found in {word}")


ex04_list_utils.py


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
