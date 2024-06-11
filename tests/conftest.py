import pytest
import allure


@pytest.fixture
@allure.title("Example Word Fixture")
def word_fixture():
    with allure.step("Setup: Prepare word fixture"):
        print("Setup word_fixture")
    yield "hello"
    with allure.step("Teardown: Clean up word fixture"):
        print("Teardown word_fixture")
