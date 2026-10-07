UNITS = ("B", "KB", "MB", "GB", "TB", "PB")


def format_bytes(num_bytes: int) -> str:
    if num_bytes < 0:
        raise ValueError(f"Byte count must be non-negative, got {num_bytes}")
    value = float(num_bytes)
    for unit in UNITS[:-1]:
        if value < 1024:
            return (
                f"{int(value)} {unit}" if value == int(value) else f"{value:.1f} {unit}"
            )
        value /= 1024
    return (
        f"{int(value)} {UNITS[-1]}"
        if value == int(value)
        else f"{value:.1f} {UNITS[-1]}"
    )


def parse_bytes(text: str) -> int:
    text = text.strip().upper()
    for i in range(len(UNITS) - 1, -1, -1):
        if text.endswith(UNITS[i]):
            number = text[: -len(UNITS[i])].strip()
            return int(float(number) * (1024**i))
    raise ValueError(f"Unknown byte format: {text!r}")
