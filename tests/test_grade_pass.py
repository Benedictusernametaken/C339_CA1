import pytest
from src.grade_pass import has_passed


@pytest.mark.parametrize(
    "score, expected",
    [
        (0, False),
        (49, False),
        (50, True),  
        (75, True),
        (100, True),
    ],
)
def test_valid_score_returns_expected_pass_status(score, expected):
    # Arrange & Act
    result = has_passed(score)

    # Assert
    assert result is expected


@pytest.mark.parametrize("score", [-1, 101])
def test_out_of_range_score_raises_value_error(score):
    # Arrange, Act & Assert
    with pytest.raises(ValueError):
        has_passed(score)


@pytest.mark.parametrize("score", ["50", 50.0, True, False, None])
def test_invalid_type_score_raises_type_error(score):
    # Arrange, Act & Assert
    with pytest.raises(TypeError):
        has_passed(score)