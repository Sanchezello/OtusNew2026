import pytest

from rectangle import Rectangle
from triangle import Triangle


@pytest.mark.parametrize(
    "figure1, expected_area",
    [
        pytest.param(Triangle(4, 4, 4), 6.93, id="Triangle area")
    ]
)
def test_triangle_area(figure1, expected_area):
    msg = f"{figure1} must be {expected_area}"
    assert round(figure1.area, 2) == expected_area, msg


@pytest.mark.parametrize(
    "figure1, expected_perimeter",
    [
        pytest.param(Triangle(4, 4, 4), 12, id="Triangle perimeter")
    ]
)
def test_triangle_perimeter(figure1, expected_perimeter):
    msg = f"{figure1} must be {expected_perimeter}"
    assert figure1.perimeter == expected_perimeter, msg


@pytest.mark.parametrize(
    "figure1, figure2, expected_area",
    [
        pytest.param(
            Triangle(4, 4, 4),
            Rectangle(2, 6),
            18.93,
            id="Triangle and other figure"
        ),
        pytest.param(
            Triangle(4, 4, 4),
            Triangle(3, 4, 5),
            12.93,
            id="Triangle and other triangle"
        ),
        pytest.param(
            Triangle(4, 4, 4),
            Triangle(4, 4, 4),
            13.86,
            id="Triangle and same figure"
        )
    ]
)
def test_add_area(figure1, figure2, expected_area):
    result = round(figure1.add_area(figure2), 2)
    msg = f"Sum of areas should be {expected_area}"
    assert result == expected_area, msg


@pytest.mark.parametrize(
    "a, b, c",
    [
        pytest.param(-1, 2, 3, id="negative side"),
        pytest.param(0, 4, 5, id="with zero side"),
        pytest.param(0, 0, 0, id="zero sides")
    ]
)
def test_triangle_invalid_sides(a, b, c):
    with pytest.raises(ValueError):
        Triangle(a, b, c)


@pytest.mark.parametrize(
    "a, b, c",
    [
        pytest.param(2, 3, 5, id="sum of two sides equals third"),
        pytest.param(5, 5, 11, id="sum of two sides less than third")
    ]
)
def test_triangle_impossible(a, b, c):
    with pytest.raises(ValueError):
        Triangle(a, b, c)


@pytest.mark.skip(reason="known bug https://jira.com/0002")
def test_triangle_cannot_be_rectangle():
    with pytest.raises(ValueError):
        Triangle(8, 16)


@pytest.mark.skip(reason="known bug https://jira.com/0003")
def test_triangle_cannot_be_square():
    with pytest.raises(ValueError):
        Triangle(5, 5)
