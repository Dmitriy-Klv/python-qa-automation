import pytest

from src.simple_math import SimpleMath


@pytest.fixture
def math_tool():
    return SimpleMath()


class TestSimpleMath:

    def test_square_positive_int(self, math_tool):
        assert math_tool.square(5) == 25

    def test_square_negative_int(self, math_tool):
        assert math_tool.square(-5) == 25

    def test_square_zero(self, math_tool):
        assert math_tool.square(0) == 0

    def test_cube_positive_int(self, math_tool):
        assert math_tool.cube(3) == 27

    def test_cube_negative_int(self, math_tool):
        assert math_tool.cube(-3) == -27
