import os
import sys


def _supports_color() -> bool:
    if os.environ.get("NO_COLOR"):
        return False
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()


class Color:
    # ── Text colors ───────────────────────────────────────────────────────────
    BLACK   = "\033[30m"
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    BLUE    = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN    = "\033[36m"
    WHITE   = "\033[37m"

    # ── Bright text colors ────────────────────────────────────────────────────
    BRIGHT_BLACK   = "\033[90m"
    BRIGHT_RED     = "\033[91m"
    BRIGHT_GREEN   = "\033[92m"
    BRIGHT_YELLOW  = "\033[93m"
    BRIGHT_BLUE    = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN    = "\033[96m"
    BRIGHT_WHITE   = "\033[97m"

    # ── Text styles ───────────────────────────────────────────────────────────
    BOLD          = "\033[1m"
    DIM           = "\033[2m"
    ITALIC        = "\033[3m"
    UNDERLINE     = "\033[4m"
    BLINK         = "\033[5m"
    REVERSE       = "\033[7m"
    STRIKETHROUGH = "\033[9m"

    # ── Background colors ─────────────────────────────────────────────────────
    BG_BLACK   = "\033[40m"
    BG_RED     = "\033[41m"
    BG_GREEN   = "\033[42m"
    BG_YELLOW  = "\033[43m"
    BG_BLUE    = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN    = "\033[46m"
    BG_WHITE   = "\033[47m"

    # ── Bright background colors ──────────────────────────────────────────────
    BG_BRIGHT_BLACK   = "\033[100m"
    BG_BRIGHT_RED     = "\033[101m"
    BG_BRIGHT_GREEN   = "\033[102m"
    BG_BRIGHT_YELLOW  = "\033[103m"
    BG_BRIGHT_BLUE    = "\033[104m"
    BG_BRIGHT_MAGENTA = "\033[105m"
    BG_BRIGHT_CYAN    = "\033[106m"
    BG_BRIGHT_WHITE   = "\033[107m"

    # ── Reset ─────────────────────────────────────────────────────────────────
    RESET = "\033[0m"


def colorize(text: str, *styles: str) -> str:
    """Apply one or more Color attributes to text, then reset automatically.

    Returns plain text unchanged when the terminal does not support color
    (non-TTY output, or the NO_COLOR environment variable is set).

    Examples:
        colorize("Hello", Color.RED)
        colorize("World", Color.BOLD, Color.UNDERLINE, Color.CYAN)
        colorize("Alert", Color.BG_RED, Color.WHITE, Color.BOLD)
    """
    if not _supports_color():
        return text
    return "".join(styles) + text + Color.RESET
