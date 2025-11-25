import argparse
from pathlib import Path


def parsing_args():
    parser = argparse.ArgumentParser(
        prog="sira",
        description="Automate CV tailoring with local LLMs."
    )

    parser.add_argument(
        "-cv", "--cv",
        type=Path,
        metavar="PATH",
        help="Path to CV JSON file (uses stored config if not provided)"
    )

    parser.add_argument(
        "-m", "--model",
        metavar="NAME",
        help="Ollama model name (uses stored config if not provided)"
    )

    parser.add_argument(
        "-s", "--store",
        action="store_true",
        help="Save CV path and model choice for future runs"
    )
  

    return parser.parse_args()