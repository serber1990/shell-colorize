# Changelog

## 1.1.0

- New `supports_color()` public helper: honours `NO_COLOR`, `FORCE_COLOR` and TTY detection.
- New `Color.auto()`, `Color.disable()` and `Color.enable()` to switch every attribute on/off globally,
  so f-string based output is plain text when piped or redirected.
- License file is now MIT, matching the package metadata.
- Test suite and GitHub Actions CI.
- Requires Python 3.9+.

## 1.0.0

- Bright colors, text styles and `colorize()` helper.
