import pytest

from RightTriangle import RightTriangle


# @pytest.fixture()
# def class_init():
#     return IsoscelesRightTriangle(1, 11.31370849898476)


@pytest.mark.parametrize(
    "leg_one, leg_two, result",
    [
        (0.3413, 0.645, [0.7297333005968688, 1.7160333005968686]),
        (465, 2.475, [465.006586646899, 932.481586646899]),
        (1.22, 6, [6.122777147667551, 13.342777147667551]),
        (9, 8, [12.041594578792296, 29.041594578792296]),
    ]
)
def test_result(leg_one, leg_two, result):
    triangle = RightTriangle(leg_one, leg_two)
    assert triangle.triangle_values() == result


@pytest.mark.parametrize(
    "leg_one, leg_two, result",
    [
        (24, 71, 74.94664769020693),
        (10.341, 14.57, 17.86676190584069),
        (5.21, 3, 6.011996340650915),
        (1, 2.43, 2.6277176408434757),
    ]
)
def test_result(leg_one, leg_two, result):
    triangle = RightTriangle(leg_one, leg_two)
    assert triangle.hypotenuse() == result


@pytest.mark.parametrize(
    "leg_one, leg_two",
    [
        (0.34, -5),
        (0, 2),
        (-354, -0.5474),
        (21, -41),
    ]
)
def test_incorrect_number(leg_one, leg_two):
    with pytest.raises(Exception):
        RightTriangle(leg_one, leg_two)

