"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Return a non-negative integer quantity parsed from *value*.

    Raises
    ------
    ValueError
        If *value* cannot be converted to an integer, or if the resulting
        integer is negative.
    """
    qty = int(value.strip())
    if qty < 0:
        raise ValueError(f"quantity must be non-negative, got {qty}")
    return qty
