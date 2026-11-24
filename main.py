"""Write one deterministic commit message for The 3 AM Commit Message."""

import os
from pathlib import Path


# 126 characters: CEO victim / empty account as recovery / false-success closer.
MESSAGE = (
    "fix(prod): dropped the database at 3 AM; restored the CEO's account. "
    'Sent "Welcome, you\'re our first user!" Recovery complete.'
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(MESSAGE, encoding="utf-8")


if __name__ == "__main__":
    main()
