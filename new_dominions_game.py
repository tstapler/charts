import random
import subprocess

import yaml
import re
from pathlib import Path
from typing import Iterable, List, Optional
from dominions5.args_generator import Era, dom5_nations_by_era

FILENAME_PATTERN = re.compile(r'(.*)_(\d+)\.yaml$')

NATIONS_BY_ERA = dom5_nations_by_era()


def extract_suffix(filename: Path) -> int:
    matches = FILENAME_PATTERN.match(str(filename))
    if not matches:
        return 0
    return int(matches.group(2))


def sorted_by_suffix(filenames: Iterable[Path]) -> List[Path]:
    return sorted(filenames, key=extract_suffix)


def get_last_game(directory: str, game_name: str) -> Path:
    games = Path(directory).glob(f"*{game_name}*.yaml")
    if not games:
        raise ValueError(f"Failed to find game {game_name} in {directory}")
    sorted_games = sorted_by_suffix(games)
    print(sorted_games)
    return sorted_games[-1]


GAME_NAME_PATTERN = re.compile(r"(.*)_(\d+)")


def increment_game_name(game_name: str) -> str:
    matches = GAME_NAME_PATTERN.match(game_name)
    if not matches:
        raise ValueError(f"The game_name {game_name} is in an invalid format")
    return f"{matches.group(1)}_{int(matches.group(2)) + 1}"


def increment_game_file(game_file: Path):
    matches = FILENAME_PATTERN.match(str(game_file))
    if not matches:
        raise ValueError(f"The game_file {game_file} is in an invalid format")
    return Path(f"{matches.group(1)}_{int(matches.group(2)) + 1}.yaml")


def new_ai_players(gameArgs: List[str], ignore: Optional[List[str]]=None) -> List[str]:
    if not ignore:
        ignore = []
    new_game_args = gameArgs.copy()
    ai_args = {}
    era = -1
    for i, arg in enumerate(gameArgs):
        if arg == "--era":
            era = int(gameArgs[i + 1])
        if arg.startswith("--") and arg.endswith("ai"):
            ai_args[i] = arg
    print(ai_args)

    for pos in ai_args:
        new_game_args[pos + 1] = pick_random_nation_from_era(era, ignore=ignore)

    return new_game_args


def pick_random_nation_from_era(era: int, ignore: Optional[List[str]]=None) -> int:
    if not ignore:
        ignore = []
    nation = random.choice(NATIONS_BY_ERA[str(era)])

    if int(nation["id"]) in ignore:
        return pick_random_nation_from_era(era, ignore=ignore)

    return nation["id"]


# Given a name search the .values directory for a values file in .yaml format.
# Load the yaml file, generate new dominions competitors and write the file
def main(game_name: str):
    last_game = get_last_game("values", game_name)
    new_game_file = increment_game_file(last_game)
    print(new_game_file)
    last_game_data = yaml.load(last_game.read_text(), yaml.Loader)
    last_game_data['gameName'] = increment_game_name(last_game_data['gameName'])
    # Ignore Pangea and Arc
    last_game_data['gameArgs'] = new_ai_players(last_game_data['gameArgs'], ignore=[80, 94])
    new_game_file.write_text(yaml.dump(last_game_data))
    subprocess.run(["helm", "install", "-f", str(new_game_file), new_game_file.stem.replace("_", "-"), './dominions5'])


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--game-name", required=True)
    args = parser.parse_args()
    main(args.game_name)
