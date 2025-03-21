from datetime import datetime
import pytest
import utils


@pytest.mark.date_format_valid
@pytest.mark.parametrize("date, date_format, expected", [
    ("21/03/2025", "%d/%m/%Y", True),
    ("2025/03/21", "%d/%m/%Y", False)
])
def test_date_format_valid(date, date_format, expected):
    assert utils.date_format_valid(date, date_format) == expected


@pytest.mark.parse_date
@pytest.mark.parametrize("date, date_format, expected", [
    ("21/03/2025", "%d/%m/%Y", datetime(2025, 3, 21))
])
def test_parse_date(date, date_format, expected):
    assert utils.parse_date(date, date_format) == expected


@pytest.mark.date_range_valid
@pytest.mark.parametrize("date1, date2, expected", [
    (datetime(2025, 3, 21), datetime(2025, 3, 22), True),
    (datetime(2025, 3, 22), datetime(2025, 3, 21), False),
])
def test_date_range_valid(date1, date2, expected):
    assert utils.date_range_valid(date1, date2) == expected
