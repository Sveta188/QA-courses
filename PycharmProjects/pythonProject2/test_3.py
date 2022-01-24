import pytest


@pytest.mark.parametrize("param, instance", [
    (10, int),
    (0.3, float),
    ("Str", str),
    ((1, 2, 3), tuple)])
class TestMyTest(object):
    @pytest.mark.xfail
    def test_is_inst(self, param, instance):
        assert isinstance(param, instance) is True
