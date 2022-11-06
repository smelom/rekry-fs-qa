import logging
from argparse import ArgumentParser
from time import sleep

import requests
import toml


def main():
    config = toml.load("config.toml")

    parser = ArgumentParser(
        description="Monitor a list of websites given in config.toml"
    )
    parser.add_argument(
        "-s",
        "--sleep",
        default=config["sleep"],
        help="Time to sleep (in seconds) between checks",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        default=False,
        help="Log progress also to stdout",
    )
    args = parser.parse_args()

    # TODO: Wipe the log file at the start of every run or leave it be?
    logging_handlers = [logging.FileHandler(config["log_file"])]
    if args.verbose:
        logging_handlers.append(logging.StreamHandler())
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=logging_handlers,
    )

    try:
        while True:
            for website in config["websites"]:
                try:
                    response = requests.get(website["url"])
                    status_code = response.status_code
                    content_check_ok = website["content"] in response.text
                    elapsed_time = response.elapsed

                    message = (
                        f'{website["url"]} - Status code: {status_code} - Content check passed: {content_check_ok}'
                        f" - Time elapsed: {elapsed_time}"
                    )

                    # Everything OK
                    if status_code == requests.codes.ok and content_check_ok:
                        logging.info(message)
                    # Status not OK
                    elif status_code != requests.codes.ok:
                        logging.error(message)
                    # Status OK but content check did not pass
                    elif not content_check_ok:
                        logging.warning(message)
                except requests.exceptions.RequestException as e:
                    message = f'{website["url"]} - Request failed: {e}'
                    logging.error(message)

            sleep(int(args.sleep))
    except KeyboardInterrupt:
        print("Program terminated manually.")
        raise SystemExit


if __name__ == "__main__":
    main()
