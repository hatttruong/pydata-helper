"""Summary
"""
from datetime import datetime, timedelta


def get_time(seconds):
    """
    Convert the number of seconds to day:hour:minute:second

    Args:
        seconds (int): number of seconds

    Returns:
        str: "dd:hh:mm:ss"
    """
    sec = timedelta(seconds=seconds)
    d = datetime(1, 1, 1) + sec
    return "%d:%d:%d:%d" % (d.day - 1, d.hour, d.minute, d.second)
