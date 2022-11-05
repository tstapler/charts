#!/usr/bin/env python
import pathlib
import random
from datetime import datetime, timedelta
from enum import Enum

from collections import defaultdict
import csv
import urllib3


class Era(Enum):
    EARLY = "1"
    MIDDLE = "2"
    LATE = "3"


class Difficulty(Enum):
    EASY = "easy"
    NORMAL = "norm"
    DIFFICULT = "diff"
    MIGHTY = "mighty"
    MASTER = "master"
    IMPOSSIBLE = "imp"


friendly_difficulty = {
    "easy": Difficulty.EASY,
    "normal": Difficulty.NORMAL,
    "difficult": Difficulty.DIFFICULT,
    "mighty": Difficulty.MASTER,
    "impossible": Difficulty.IMPOSSIBLE,
}

era_map = {"early": Era.EARLY, "middle": Era.MIDDLE, "late": Era.LATE}

underwater_nations = [
    '36',  # Atlantis EA
    '37',  # R'lyeah EA
    '39',  # Pelagia EA
    '76',  # Oceania MA
    '73',  # Atlantis MA
    '74',  # R'lyeh MA
    '75',  # Pelagia MA
    '76',  # Oceania MA
    '77',  # Ys MA
    '106',  # Atlantis LA
    '107',  # R'lyeah LA
]


def fetch_and_cache_csv(
    name: str, url: str,
    cache_length: timedelta = timedelta(days=1)) -> pathlib.Path:
    http = urllib3.PoolManager()
    cached_csv = pathlib.Path("f{name}.csv")
    if (not cached_csv.exists() or datetime.now() -
            datetime.fromtimestamp(cached_csv.stat().st_mtime) > cache_length):
        response = http.request('GET', url)
        if response:
            cached_csv.write_bytes(response.data)
        else:
            print(f"Failed to write csv {cached_csv}")
    return cached_csv


def dom5_nation_csv():
    return fetch_and_cache_csv(
        "dom5_nations",
        'https://raw.githubusercontent.com/larzm42/dom5inspector/gh-pages/gamedata/nations.csv'
    )


def dom5_nations_by_era():
    era = defaultdict(list)
    with open(dom5_nation_csv()) as file:
        for nation in csv.DictReader(file, delimiter="\t"):
            era[nation["era"]].append(nation)
        return era


def generate_arguments(era: Era,
                       num_randoms: int,
                       difficulty: Difficulty,
                       no_sea: bool = True) -> list:
    nations_by_era = dom5_nations_by_era()
    nations = nations_by_era[era.value]

    if no_sea:
        nations = [n for n in nations if n["id"] not in underwater_nations]

    arguments = []
    for _ in range(num_randoms):
        nation = random.choice(nations)
        arguments.extend([
            f"  # {nation['name']}", f"  - --{difficulty.value}ai",
            f"  - '{nation['id']}'"
        ])
        nations.remove(nation)

    return arguments


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description=
        "Generate helm chart arguments for the Dominions 5 helm chart.")
    parser.add_argument('--era',
                        dest="era",
                        choices=era_map.keys(),
                        required=True,
                        help="Start the server with this era")
    parser.add_argument(
        '--randoms',
        dest="randoms",
        required=True,
        type=int,
        help="Generate RANDOM number of computer controlled nations")
    parser.add_argument('--difficulty',
                        dest="difficulty",
                        choices=friendly_difficulty.keys(),
                        default="normal",
                        help="Configure the computer to use this DIFFICULTY")
    parser.add_argument('--no-sea',
                        dest="nosea",
                        action="store_true",
                        help="Do not generate ocean nations")

    args = parser.parse_args()

    print("\n".join(
        generate_arguments(era_map[args.era],
                           args.randoms,
                           friendly_difficulty[args.difficulty],
                           no_sea=args.nosea)))
