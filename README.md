
# 🌈 `shellcolorize`

[![PyPI version](https://badge.fury.io/py/shellcolorize.svg)](https://badge.fury.io/py/shellcolorize)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/serber1990/shellcolorize?style=social)](https://github.com/serber1990/shellcolorize/stargazers)

**`shellcolorize`** is a lightweight Python library for adding color to terminal text using ANSI color codes. This library makes it easy to style your command-line output with vibrant colors and backgrounds, perfect for enhancing readability and making CLI applications more visually appealing.

---

## ✨ Features

- 🌈 **Wide Range of Colors**: Includes standard text and background colors.
- 🚀 **Easy to Use**: Simple and intuitive API to add color to terminal text.
- 💡 **ANSI Standard**: Uses ANSI color codes, compatible with most Unix-based terminals and compatible environments.
- 🔗 **Open Source**: Licensed under the MIT License.

---

## 📥 Installation

Install `shellcolorize` from PyPI:

```bash
pip install shellcolorize
```

---

## 🛠 Usage

`shellcolorize` makes it easy to color your terminal text. Import `Color` from `shellcolorize` and use the color attributes as shown below.

### Basic Usage
```python
from shellcolorize import Color

print(f"{Color.RED}This is red text{Color.RESET}")
print(f"{Color.GREEN}This is green text{Color.RESET}")
```

### Using Background Colors
```python
from shellcolorize import Color

print(f"{Color.BG_YELLOW}{Color.BLACK}Black text on yellow background{Color.RESET}")
print(f"{Color.BG_BLUE}{Color.WHITE}White text on blue background{Color.RESET}")
```

### Combining Text and Background Colors
```python
from shellcolorize import Color

print(f"{Color.BG_RED}{Color.CYAN}Cyan text on red background{Color.RESET}")
print(f"{Color.BG_GREEN}{Color.MAGENTA}Magenta text on green background{Color.RESET}")
```

---

## 🎨 Available Colors

### Text Colors

| Color | Usage Example               |
|-------|------------------------------|
| Black | `{Color.BLACK}Text{Color.RESET}` |
| Red   | `{Color.RED}Text{Color.RESET}`   |
| Green | `{Color.GREEN}Text{Color.RESET}` |
| Yellow| `{Color.YELLOW}Text{Color.RESET}` |
| Blue  | `{Color.BLUE}Text{Color.RESET}`   |
| Magenta | `{Color.MAGENTA}Text{Color.RESET}` |
| Cyan  | `{Color.CYAN}Text{Color.RESET}`   |
| White | `{Color.WHITE}Text{Color.RESET}`  |

### Background Colors

| Color       | Usage Example                         |
|-------------|--------------------------------------|
| Black       | `{Color.BG_BLACK}Text{Color.RESET}`  |
| Red         | `{Color.BG_RED}Text{Color.RESET}`    |
| Green       | `{Color.BG_GREEN}Text{Color.RESET}`  |
| Yellow      | `{Color.BG_YELLOW}Text{Color.RESET}` |
| Blue        | `{Color.BG_BLUE}Text{Color.RESET}`   |
| Magenta     | `{Color.BG_MAGENTA}Text{Color.RESET}`|
| Cyan        | `{Color.BG_CYAN}Text{Color.RESET}`   |
| White       | `{Color.BG_WHITE}Text{Color.RESET}`  |

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💬 Feedback

If you have any questions, issues, or suggestions, please feel free to open an issue in the repository or contact me directly via GitHub.

---

## 🌐 Connect with Me

[![GitHub](https://img.shields.io/badge/GitHub-@serber1990-181717?style=flat-square&logo=github)](https://github.com/serber1990)

---

### 🚀 Let's bring more color to the command line with `shellcolorize`!
