import pytest

from rectangle import Rectangle
from square import Square


@pytest.mark.parametrize(
    "figure1, expected_area",
    [
        pytest.param(Square(6), 36, id="Square area")
    ]
)
def test_square_area(figure1, expected_area):
    msg = f"{figure1} must be {expected_area}"
    assert figure1.area == expected_area, msg


@pytest.mark.parametrize(
    "figure1, expected_perimeter",
    [
        pytest.param(Square(6), 24, id="Square perimeter")
    ]
)
def test_square_perimeter(figure1, expected_perimeter):
    msg = f"{figure1} must be {expected_perimeter}"
    assert figure1.perimeter == expected_perimeter, msg


@pytest.mark.parametrize(
    "figure1, figure2, expected_area",
    [
        pytest.param(
            Square(4),
            Rectangle(4, 5),
            36,
            id="Square and other figure"
        ),
        pytest.param(
            Square(4),
            Square(5),
            41,
            id="Square and other square"
        ),
        pytest.param(
            Square(4),
            Square(5),
            41,
            id="Square and same figure"
        )
    ]
)
def test_add_area(figure1, figure2, expected_area):
    msg = f"Sum of areas should be {expected_area}"
    assert figure1.add_area(figure2) == expected_area, msg


@pytest.mark.parametrize(
    "side_a",
    [
        pytest.param(-1, id="negative value"),
        pytest.param(0, id="zero")
    ]
)
def test_square_invalid_sides(side_a):
    with pytest.raises(ValueError):
        Square(side_a)


@pytest.mark.skip(reason="known bug https://jira.com/0001")
def test_square_cannot_be_triangle():
    with pytest.raises(ValueError):
        Square(4, 4, 4)
