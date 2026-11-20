import pytest
from src.grade_average import calculate_average


@pytest.mark.parametrize(
    "mark_one, mark_two, expected",
    [
        (0, 0, 0.0),
        (100, 100, 100.0),
        (0, 100, 50.0),
        (80, 90, 85.0),
        (50, 51, 50.5),  # Exposes defect: // 2 returns 50 instead of 50.5
    ],
)
def test_valid_marks_returns_expected_average(mark_one, mark_two, expected):
    # Arrange & Act
    result = calculate_average(mark_one, mark_two)

    # Assert
    assert result == expected


@pytest.mark.parametrize(
    "mark_one, mark_two",
    [
        (-1, 50),
        (50, -1),
        (101, 50),
        (50, 101),
    ],
)
def test_out_of_range_marks_raises_value_error(mark_one, mark_two):
    # Arrange, Act & Assert
    with pytest.raises(ValueError):
        calculate_average(mark_one, mark_two)


@pytest.mark.parametrize(
    "mark_one, mark_two",
    [
        ("50", 50),
        (50, "50"),
        (50.5, 50),
        (True, 50),
        (50, False),
        (None, 50),
    ],
)
def test_invalid_type_marks_raises_type_error(mark_one, mark_two):
    # Arrange, Act & Assert
    with pytest.raises(TypeError):
        calculate_average(mark_one, mark_two)

# Test push to GitHub