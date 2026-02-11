import pytest

from rectangle import Rectangle
from square import Square


@pytest.mark.parametrize(
    "figure_1, expected_area",
    [
        pytest.param(Rectangle(10, 5), 50, id="Rectangle area")
    ]
)
def test_rectangle_area(figure_1, expected_area):
    msg = f"{figure_1} must be {expected_area}"
    assert figure_1.area == expected_area, msg


@pytest.mark.parametrize(
    "figure_1, expected_perimeter",
    [
        pytest.param(Rectangle(10, 5), 30, id="Rectangle perimeter")
    ]
)
def test_rectangle_perimeter(figure_1, expected_perimeter):
    msg = f"{figure_1} must be {expected_perimeter}"
    assert figure_1.perimeter == expected_perimeter, msg


@pytest.mark.parametrize(
    "figure_1, figure_2, expected_area",
    [
        pytest.param(
            Rectangle(10, 5),
            Rectangle(2, 3),
            56,
            id="2 Rectangles"
        ),
        pytest.param(
            Square(6),
            Rectangle(10, 5),
            86,
            id="Rectangle and square"
        )
    ]
)
def test_add_area(figure_1, figure_2, expected_area):
    msg = f"Sum of areas should be {expected_area}"
    assert figure_1.add_area(figure_2) == expected_area, msg


@pytest.mark.parametrize(
    "side_a, side_b",
    [
        pytest.param(-1, 1, id="negative sides")
    ]
)
def test_rectangle_invalid_sides(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)
