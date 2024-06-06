def count_words(text: str) -> int:
    """Return the number of words in the given text."""
    if not text:
        return False
    return len(text.split())


def reverse_string(text):
    """Return the reversed version of the given text."""
    return text[::-1]


def is_palindrome(text):
    """Check if the given text is a palindrome (ignores case and spaces)."""
    # Check for empty string
    if not text:
        return False
    cleaned_text = "".join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]


def capitalize_text(text):
    """Return the capitalized version of the given text."""
    if not text:
        return False
    return text.capitalize()
