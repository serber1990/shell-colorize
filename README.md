# 🌈 `shellcolorize`

[![PyPI version](https://badge.fury.io/py/shellcolorize.svg)](https://badge.fury.io/py/shellcolorize)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/serber1990/shell-colorize?style=social)](https://github.com/serber1990/shell-colorize/stargazers)

**`shellcolorize`** is a lightweight Python library for adding color and style to terminal output using ANSI codes. Zero dependencies, no configuration — just import and use.

---

## ✨ Features

- 🎨 **Full ANSI palette** — 8 standard + 8 bright text colors, same for backgrounds.
- ✍️ **Text styles** — bold, dim, italic, underline, blink, reverse, strikethrough.
- 🛠 **`colorize()` helper** — applies styles and resets automatically, no manual `RESET` needed.
- 🔇 **Smart color detection** — outputs plain text when piped to a file or when `NO_COLOR` is set.
- 🔗 **Open Source** — MIT License.

---

## 📥 Installation

```bash
pip install shellcolorize
```

---

## 🛠 Usage

### Using `colorize()` (recommended)

`colorize(text, *styles)` applies any combination of colors and styles and resets automatically. It also returns plain text when the output is not a TTY or when the `NO_COLOR` env var is set.

```python
from shellcolorize import Color, colorize

print(colorize("This is red", Color.RED))
print(colorize("Bold and underlined", Color.BOLD, Color.UNDERLINE))
print(colorize("White on blue background", Color.BG_BLUE, Color.WHITE))
print(colorize("Bright green, bold", Color.BRIGHT_GREEN, Color.BOLD))
```

### Using `Color` attributes directly

For inline use in f-strings. Remember to close with `Color.RESET`.

```python
from shellcolorize import Color

print(f"{Color.RED}This is red{Color.RESET}")
print(f"{Color.BG_YELLOW}{Color.BLACK}Black on yellow{Color.RESET}")
print(f"{Color.BOLD}{Color.CYAN}Bold cyan{Color.RESET}")
```

---

## 🎨 Available Colors

### Standard text colors

| Attribute | Attribute |
|-----------|-----------|
| `Color.BLACK` | `Color.BRIGHT_BLACK` |
| `Color.RED` | `Color.BRIGHT_RED` |
| `Color.GREEN` | `Color.BRIGHT_GREEN` |
| `Color.YELLOW` | `Color.BRIGHT_YELLOW` |
| `Color.BLUE` | `Color.BRIGHT_BLUE` |
| `Color.MAGENTA` | `Color.BRIGHT_MAGENTA` |
| `Color.CYAN` | `Color.BRIGHT_CYAN` |
| `Color.WHITE` | `Color.BRIGHT_WHITE` |

### Background colors

| Attribute | Attribute |
|-----------|-----------|
| `Color.BG_BLACK` | `Color.BG_BRIGHT_BLACK` |
| `Color.BG_RED` | `Color.BG_BRIGHT_RED` |
| `Color.BG_GREEN` | `Color.BG_BRIGHT_GREEN` |
| `Color.BG_YELLOW` | `Color.BG_BRIGHT_YELLOW` |
| `Color.BG_BLUE` | `Color.BG_BRIGHT_BLUE` |
| `Color.BG_MAGENTA` | `Color.BG_BRIGHT_MAGENTA` |
| `Color.BG_CYAN` | `Color.BG_BRIGHT_CYAN` |
| `Color.BG_WHITE` | `Color.BG_BRIGHT_WHITE` |

### Text styles

| Attribute | Effect |
|-----------|--------|
| `Color.BOLD` | **Bold** |
| `Color.DIM` | Dimmed |
| `Color.ITALIC` | *Italic* |
| `Color.UNDERLINE` | Underline |
| `Color.BLINK` | Blinking |
| `Color.REVERSE` | Swaps fg/bg colors |
| `Color.STRIKETHROUGH` | ~~Strikethrough~~ |
| `Color.RESET` | Clears all styles |

---

## 🔇 Color detection

`colorize()` automatically outputs plain text (no ANSI codes) in two situations:

- The output is **not a TTY** — e.g. redirected to a file or piped to another command.
- The **`NO_COLOR`** environment variable is set (any value), following the [no-color.org](https://no-color.org) convention.

```bash
# Plain text — no color codes in the file
python script.py > output.txt

# Plain text — respects NO_COLOR
NO_COLOR=1 python script.py
```

> Direct use of `Color` attributes (f-strings) always emits ANSI codes regardless of environment.

---

## 📝 License

MIT — see [LICENSE](LICENSE).

---

## 💬 Feedback

Open an issue or reach out via GitHub.

## 🌐 Connect

[![GitHub](https://img.shields.io/badge/GitHub-@serber1990-181717?style=flat-square&logo=github)](https://github.com/serber1990)
