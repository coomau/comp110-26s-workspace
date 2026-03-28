"""EX05 - Directory Utility Functions - practice with dictionary functions."""

__author__: str = "730736150"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of a dictionary."""
    result: dict[str, str] = {}
    for (
        key
    ) in (
        input_dict
    ):  # Loop through each key in the input dictionary. found this gem of formatting in part 3.
        value = input_dict[key]
        if (
            value in result
        ):  # Check if the value already exists as a key in the result dictionary
            raise KeyError(
                f'Duplicate key found during inversion: "{value}"'
            )  # I'll see if this matters to the autograder, but this is my error message
        result[value] = key
    return result


def favorite_color(colors: dict[str, str]) -> str:
    """Return the most common color in the given name->color dictionary."""
    color_counts: dict[str, int] = {}
    for name in colors:  # Count how many times each color appears
        color = colors[name]
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1
    most_popular = ""
    max_count = 0
    for color in color_counts:  # Find the color with the highest count
        if color_counts[color] > max_count:
            max_count = color_counts[color]
            most_popular = color
    return most_popular


def count(values: list[str]) -> dict[str, int]:
    """Count the number of occurrences of each string in a list."""
    result: dict[str, int] = {}
    for (
        item
    ) in (
        values
    ):  # If the item already exists in the dictionary, increase its count, otherwise keep the count at 1
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Group words by their starting letter."""
    result: dict[str, list[str]] = {}
    for (
        word
    ) in (
        words
    ):  # Only process words that start with a letter & create a new list for this letter if it doesn't exist
        if word and word[0].isalpha():
            first_letter = word[0].lower()
            if first_letter in result:
                result[first_letter].append(word)
            else:
                result[first_letter] = [word]
    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Update the attendance dictionary with a student for a given day."""
    if (
        day not in attendance
    ):  # If the day already exists, append the student to the list, otherwise create a new list with the student
        attendance[day] = []
    attendance[day].append(student)
