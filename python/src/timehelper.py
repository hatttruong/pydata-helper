"""
There are 2 packages to calculate different between 2 dates:
- timedelta:
    datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0,
                        minutes=0, hours=0, weeks=0)

- relativedelta:
    relativedelta.relativedelta(self, dt1=None, dt2=None, years=0, months=0,
            days=0, leapdays=0, weeks=0, hours=0, minutes=0, seconds=0,
            microseconds=0, year=None, month=None, day=None, weekday=None,
            yearday=None, nlyearday=None, hour=None, minute=None, second=None,
            microsecond=None)
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


def duration(start, end, mode='h'):
    """
    Calculate the time interval between start & end

    Args:
        start (TYPE): datetime.datetime object
        end (TYPE): datetime.datetime object
        mode (str, optional):
            'd' means days, 'h' means hours, 'm' means minutes,
            's' means seconds, 'micro' = microseconds, 'mili' = milliseconds
    """
    elapsed = end - start
    print(type(elapsed))
    # use timedelta
    if mode == 's':
        return elapsed.total_seconds


def datetime2str(dt, format='%d:%m:%Y %H:%M:%S'):
    """
    Format datetime object to string

    Args:
        dt (TYPE): Description
    """
    # TODO
    pass


def str2datetime(str):
    """
    Convert datetime in string to datetime object

    Args:
        str (TYPE): Description
    """
    # TODO
    pass


def str2time(str):
    """
    Convert time in string to time object

    Args:
        str (TYPE): Description
    """
    # TODO
    pass
