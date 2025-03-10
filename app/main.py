import argparse

from app.yeet import Yeeter


def main():
    args = parse_args()
    yeeter = Yeeter(args.colorize)
    yeeter.yeet(args.filepath, args.header)


def parse_args():
    """
    Parse command-line arguments.

    This function sets up an argument parser with the following options:
    - `-f` or `--filepath`: A required string argument that specifies the request filepath in .json, .yaml, or .yml format.
    - `-c` or `--colorize`: An optional flag that, when set, will colorize stdout and stderr.

    Returns:
        argparse.Namespace: An object containing the parsed command-line arguments.
    """
    # Create an ArgumentParser object with no abbreviation allowed for arguments
    # Add a required argument for the filepath
    # Add an optional flag for colorizing output
    # Parse and return the command-line arguments
    ap = argparse.ArgumentParser(allow_abbrev=False)
    ap.add_argument(
        "-f",
        "--filepath",
        type=str,
        required=True,
        help="Request filepath in .json or .yaml or .yml format",
    )
    ap.add_argument(
        "-H",
        "--header",
        action="append",
        help="Specify custom HTTP headers (use multiple times for multiple headers)",
    )
    ap.add_argument(
        "-c", "--colorize", action="store_true", help="colorize stdout and stderr"
    )
    return ap.parse_args()


if __name__ == "__main__":
    main()

