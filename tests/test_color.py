import io

import pytest

from shellcolorize import Color, colorize, supports_color
from shellcolorize.color import _CODES


class FakeTTY(io.StringIO):
    def isatty(self):
        return True


@pytest.fixture(autouse=True)
def clean_env(monkeypatch):
    monkeypatch.delenv("NO_COLOR", raising=False)
    monkeypatch.delenv("FORCE_COLOR", raising=False)
    yield
    Color.enable()


def test_codes_are_ansi_sequences():
    assert Color.RED == "\033[31m"
    assert Color.BG_BRIGHT_WHITE == "\033[107m"
    assert Color.RESET == "\033[0m"
    assert all(code.startswith("\033[") and code.endswith("m") for code in _CODES.values())


def test_supports_color_follows_tty():
    assert supports_color(FakeTTY()) is True
    assert supports_color(io.StringIO()) is False


def test_no_color_wins_over_tty(monkeypatch):
    monkeypatch.setenv("NO_COLOR", "1")
    assert supports_color(FakeTTY()) is False


def test_force_color_enables_without_tty(monkeypatch):
    monkeypatch.setenv("FORCE_COLOR", "1")
    assert supports_color(io.StringIO()) is True
    monkeypatch.setenv("FORCE_COLOR", "0")
    assert supports_color(io.StringIO()) is False


def test_closed_stream_does_not_raise():
    stream = io.StringIO()
    stream.close()
    assert supports_color(stream) is False


def test_disable_and_enable_roundtrip():
    Color.disable()
    assert Color.RED == "" and Color.RESET == ""
    assert f"{Color.BOLD}text{Color.RESET}" == "text"
    Color.enable()
    assert Color.RED == "\033[31m"


def test_auto_matches_stream():
    assert Color.auto(io.StringIO()) is False
    assert Color.GREEN == ""
    assert Color.auto(FakeTTY()) is True
    assert Color.GREEN == "\033[32m"


def test_colorize_plain_when_not_supported(monkeypatch):
    monkeypatch.setenv("NO_COLOR", "1")
    assert colorize("hi", Color.RED) == "hi"


def test_colorize_wraps_and_resets(monkeypatch):
    monkeypatch.setenv("FORCE_COLOR", "1")
    assert colorize("hi", Color.BOLD, Color.RED) == "\033[1m\033[31mhi\033[0m"
