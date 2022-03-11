import re


def is_valid_timestamp(timestamp):
    """Example timestamp:
    2022-03-04-18-18-14-991
    Args:
        timestamp (string)

    Returns Boolean
    """
    regex = r"\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}-\d{3}"
    if re.fullmatch(regex, timestamp):
        return True
    else:
        return False


def write_timestamp_to_file(txt):
    """Writes timestamp to queue one line at a time.
    Args:
        txt (string): timestamp
    """
    if is_valid_timestamp(txt):
        with open("timestamp_queue.txt", "a") as f:
            f.write(f"{txt}\n")

    # TODO give deefback to user on succes or incorrect timestamp.
