"""
Sig gen

This was made by AI, edited by me to function properly, I take no credit.
The purpose is to simply development in the main file by having a list of
every signature to change.
"""
import json
import re
from itertools import product


def parse_range_token(token: str) -> list[str]:
    match = re.fullmatch(r'([0-9A-Fa-f]?)\|([0-9A-Fa-f])\+\+(\d+)\|', token)
    if not match:
        return [token]
    prefix = match.group(1).upper()
    start = int(match.group(2), 16)
    count = int(match.group(3))

    results = []
    for i in range(count):
        val = start + i
        high = int(prefix, 16) + (val >> 4) if prefix else (val >> 4)
        low = val & 0xF
        if high > 0:
            results.append(f"{high:X}{low:X}")
        else:
            results.append(f"{low:X}")
    return results


def expand_aob(pattern: str) -> list[str]:
    token_options = [parse_range_token(t) for t in pattern.split()]
    return [' '.join(combo) for combo in product(*token_options)]


def process_signatures(input_path: str, output_path: str):
    with open(input_path, 'r') as f:
        data = json.load(f)

    results = []

    for category_dict in data["all_sigs"]:
        for sigs in category_dict.values():
            for pattern, value in sigs.values():
                for aob in expand_aob(pattern):
                    results.append([aob, value])

    with open(output_path, 'w') as f:
        json.dump(results, f, separators=(',', ':'))

    print(f"Processed {input_path} -> {output_path} ({len(results)} entries)")


if __name__ == "__main__":
    import sys

    input_file = sys.argv[1] if len(sys.argv) > 1 else "raw_sigs.json"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "all_sigs.json"

    process_signatures(input_file, output_file)