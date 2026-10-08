#!/usr/bin/env python3

from pathlib import Path
import re
import json

ROOT = Path(__file__).resolve().parent.parent
BANKS_DIR = ROOT / "banks"

MAX_VOICES = 16
MAX_SAMPLES = 32

pattern = re.compile(r"^(\d+)\.(\d+)\.(wav|WAV)$")


def scan_bank(bank_dir):
    voices = {str(i): [] for i in range(1, MAX_VOICES + 1)}
    invalid = []

    for path in sorted(bank_dir.iterdir()):
        if not path.is_file():
            continue

        match = pattern.match(path.name)
        if not match:
            if path.suffix.lower() == ".wav":
                invalid.append(path.name)
            continue

        voice = int(match.group(1))
        sample = int(match.group(2))

        if not 1 <= voice <= MAX_VOICES:
            invalid.append(path.name)
            continue

        if not 1 <= sample <= MAX_SAMPLES:
            invalid.append(path.name)
            continue

        voices[str(voice)].append({
            "sample": sample,
            "file": path.name,
        })

    for voice in voices:
        voices[voice].sort(key=lambda item: item["sample"])

    return {
        "bank": bank_dir.name,
        "voices": voices,
        "invalid_files": invalid,
    }


def main():
    BANKS_DIR.mkdir(parents=True, exist_ok=True)
    banks = []

    for bank_dir in sorted(BANKS_DIR.iterdir()):
        if not bank_dir.is_dir() or bank_dir.name.startswith("."):
            continue

        data = scan_bank(bank_dir)
        manifest = bank_dir / "manifest.json"
        manifest.write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

        count = sum(len(samples) for samples in data["voices"].values())
        banks.append({
            "name": bank_dir.name,
            "samples": count,
        })

        print(f"{bank_dir.name}: {count} samples")

        if data["invalid_files"]:
            print("  Archivos WAV ignorados:")
            for name in data["invalid_files"]:
                print(f"    {name}")

    (BANKS_DIR / "index.json").write_text(
        json.dumps(banks, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    if not banks:
        print("No hay bancos todavía. Crea una carpeta dentro de banks/.")


if __name__ == "__main__":
    main()
