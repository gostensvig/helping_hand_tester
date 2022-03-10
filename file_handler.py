def write_timestamp_to_file(txt):
    """Writes timestamp to queue one line at a time.
    Args:
        txt (string): timestamp
    """
    # TODO: Add a check to see if the entered string is actually a valid timestamp.
    with open("timestamp_queue.txt", "a") as f:
        f.write(f"{txt}\n")