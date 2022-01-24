import pytest


class TestPy:
    @pytest.mark.skip
    def test_1(self):
        print("test_1")

    def test_2(self):
        print("test_2")
