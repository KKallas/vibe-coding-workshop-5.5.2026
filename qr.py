#!/usr/bin/env python3
"""
Make a QR code PNG from text or a URL.

Setup once:
    pip install "qrcode[pil]"

Run:
    python qr.py
"""

from datetime import datetime
from pathlib import Path

import qrcode


def main() -> None:
    text = input("Text or link: ").strip()
    if not text:
        print("Nothing entered.")
        return

    img = qrcode.make(text)
    out = Path(f"qr_{datetime.now():%Y%m%d_%H%M%S}.png")
    img.save(out)
    print(f"Saved {out.resolve()}")


if __name__ == "__main__":
    main()
