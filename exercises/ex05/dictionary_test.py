"""EX06 - Directory Utility Tests - Test with dictionary functions already established."""

__author__: str = "730736150"

import pytest
from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance


def test_invert() -> None:  # simple use case
    """Test invert."""
    assert invert({"a": "1", "b": "2"}) == {"1": "a", "2": "b"}


def test_invert_multiple_pairs() -> None:  # multiple value use case
    """Test invert with multiple pairs."""
    assert invert({"x": "apple", "y": "banana"}) == {
        "apple": "x",
        "banana": "y",
    }


def test_invert_key_error() -> (
    None
):  # edge case (should be raised when it sees duplicate keys)
    """Test invert error cause of duplicate values."""
    with pytest.raises(KeyError):
        invert({"a": "1", "b": "1"})


def test_favorite_color() -> None:  # simple use case
    """Test favorite_color."""
    assert favorite_color({"Alice": "blue", "Bob": "red", "Carol": "blue"}) == "blue"


def test_favorite_color_one_entry() -> None:  # use case with only one value
    """Test favorite_color with only one value."""
    assert favorite_color({"Alice": "green"}) == "green"


def test_favorite_color_tie() -> None:  # edge case (grabs the first one in a tie)
    """Test favorite_color returns first encountered in a tie."""
    assert favorite_color({"A": "red", "B": "blue"}) == "red"


def test_count() -> None:  # simple use case
    """Test count."""
    assert count(["a", "b", "a"]) == {"a": 2, "b": 1}


def test_count_all_unique() -> None:  # simple use case
    """Test count when all are unique."""
    assert count(["x", "y", "z"]) == {"x": 1, "y": 1, "z": 1}


def test_count_empty_list() -> None:  # edge case should return an empty dict
    """Test count with an empty list."""
    assert count([]) == {}


def test_alphabetizer() -> None:  # simple use case
    """Test group words by first letter."""
    result = alphabetizer(["apple", "banana", "apricot"])
    assert result == {"a": ["apple", "apricot"], "b": ["banana"]}


def test_alphabetizer_big_case() -> None:  # use case, upper case becomes lower case
    """Test alphabetizer when uppercase letters."""
    result = alphabetizer(["Apple", "banana", "Avocado"])
    assert result == {"a": ["Apple", "Avocado"], "b": ["banana"]}


def test_alphabetizer_not_letter() -> (
    None
):  # edge case, should ignore words that don't start with a letter
    """Test alphabetizer ignores non-letter starts."""
    result = alphabetizer(["123", "!hello", "world"])
    assert result == {"w": ["world"]}


def test_update_attendance_existing_day() -> None:  # simple use case, existing day
    """Test adding to an existing day."""
    attendance = {"Monday": ["Alice"]}
    update_attendance(attendance, "Monday", "Bob")
    assert attendance == {"Monday": ["Alice", "Bob"]}


def test_update_attendance_new_day() -> None:  # simple use case, new day
    """Test adding to a new day."""
    attendance = {}
    update_attendance(attendance, "Tuesday", "Alice")
    assert attendance == {"Tuesday": ["Alice"]}


def test_update_attendance_multiple_updates() -> None:  # edge case, multiple updates
    """Test multiple updates."""
    attendance = {}
    update_attendance(attendance, "Monday", "Alice")
    update_attendance(attendance, "Monday", "Bob")
    update_attendance(attendance, "Tuesday", "Carol")
    assert attendance == {
        "Monday": ["Alice", "Bob"],
        "Tuesday": ["Carol"],
    }
