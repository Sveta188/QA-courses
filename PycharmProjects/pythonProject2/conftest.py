import pytest


@pytest.fixture(autouse=True) # автоюз используется для всего сьюта, а сьют в нашем случае это класс
def fix_me():
    print("Hi!")

