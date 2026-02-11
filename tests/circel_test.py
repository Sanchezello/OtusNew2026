import pytest

from SRC.circle import Circle
from SRC.triangle import Triangle


@pytest.mark.parametrize(
    "figure1, expected_area",
    [
        pytest.param(Circle(5), 78.54, id="Circle area")
    ]
)
def test_circle_area(figure1, expected_area):
    msg = f"Circle with radius {figure1.radius} must be {expected_area}"
    assert round(figure1.area, 2) == expected_area, msg


@pytest.mark.parametrize(
    "figure1, expected_perimeter",
    [
        pytest.param(Circle(5), 31.42, id="Circle perimeter")
    ]
)
def test_circle_perimeter(figure1, expected_perimeter):
    msg = f"Circle perimeter {figure1.radius} must be {expected_perimeter}"
    assert round(figure1.perimeter, 2) == expected_perimeter, msg


@pytest.mark.parametrize(
    "figure1, figure2, expected_area",
    [
        pytest.param(
            Circle(5),
            Triangle(3, 4, 5),
            84.54,
            id="Circle and triangle"
        ),
        pytest.param(
            Circle(5),
            Circle(5),
            157.08,
            id="Two equal circles"
        ),
        pytest.param(
            Circle(5),
            Circle(7),
            232.48,
            id="Two different circles"
        )
    ]
)
def test_add_area(figure1, figure2, expected_area):
    result = round(figure1.add_area(figure2), 2)
    msg = f"Sum of areas should be {expected_area}"
    assert result == expected_area, msg


@pytest.mark.parametrize(
    "radius",
    [
        pytest.param(-1, id="negative radius"),
        pytest.param(0, id="zero radius")
    ]
)
def test_circle_invalid_radius(radius):
    with pytest.raises(ValueError):
        Circle(radius)
