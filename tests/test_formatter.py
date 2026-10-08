import pytest

from byteformat import format_bytes, parse_bytes


def test_format_zero():
    assert format_bytes(0) == "0 B"


def test_format_kilobytes():
    assert format_bytes(1024) == "1 KB"


def test_format_megabytes():
    assert format_bytes(1_048_576) == "1 MB"


def test_format_fractional():
    assert format_bytes(1536) == "1.5 KB"


def test_format_negative_raises():
    with pytest.raises(ValueError, match="non-negative"):
        format_bytes(-1)


def test_parse_kilobytes():
    assert parse_bytes("1 KB") == 1024


def test_parse_unknown_raises():
    with pytest.raises(ValueError, match="Unknown"):
        parse_bytes("5 XY")


def test_roundtrip():
    for n in [0, 1, 1024, 1_048_576, 1_073_741_824]:
        assert parse_bytes(format_bytes(n)) == n
