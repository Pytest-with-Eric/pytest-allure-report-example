import pytest
import allure


@pytest.fixture
@allure.title("Example Word Fixture")
def example_word():
    print("Setting up example word fixture...")
    yield "hello"
    print("Tearing down example word fixture...")
