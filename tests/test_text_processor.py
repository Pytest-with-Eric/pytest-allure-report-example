import pytest
import allure
from pathlib import Path
from text_processor.text_processor import (
    count_words,
    reverse_string,
    is_palindrome,
    capitalize_text,
)


@allure.title("Count Words Test")
@allure.description(
    "Test the count_words function with various inputs and check the output."
)
@allure.tag("text_processor", "count_words")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
def test_count_words():
    assert count_words("hello world") == 2
    assert count_words("") == 0
    assert count_words("one") == 1


@allure.epic("Text Processor")
@allure.feature("Reverse String")
@allure.story("Reverse String Test")
def test_reverse_string():
    assert reverse_string("abc") == "cba"
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""


@allure.parent_suite("Text Processor")
@allure.suite("Palindrome Test")
@allure.sub_suite("Palindrome")
def test_is_palindrome():
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("Hello") is False
    assert is_palindrome("RaC eCar") is True
    assert is_palindrome("") is False


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello", "Hello"),
        ("HELLO", "Hello"),
        ("123", "123"),
        ("", False),
        (None, False),
    ],
)
def test_capitalize_text(text, expected):
    assert capitalize_text(text) == expected


def test_capitalize_text_with_fixture(word_fixture):
    assert capitalize_text(word_fixture) == "Hello"


def test_attach_screenshot():
    png_bytes = Path("images/screenshot.png").read_bytes()
    allure.attach(
        png_bytes,
        name="Home Page Screenshot",
        attachment_type=allure.attachment_type.PNG,
    )
