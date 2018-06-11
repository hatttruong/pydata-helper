"""Summary
"""
import progressbar
from time import sleep
import sys


def advanced_progressbar():
    """Summary
    """
    max_iterations = 150
    bar = progressbar.ProgressBar(
        maxval=max_iterations,
        widgets=[progressbar.Bar('=', '[', ']'),
                 ' ',
                 progressbar.Percentage()])
    bar.start()
    for i in range(max_iterations):
        # do your main task here
        sleep(0.1)
        bar.update(i + 1)
    bar.finish()


def simple_progressbar():
    """
    The progressbar has maximum 20 equal signs which represents the percentage of
    progress.
    If we want to change the maximum equal signs, update "20" in the following
    line:
        sys.stdout.write("[%-20s] %d%%" % ('=' * int(frac / 5), frac))
    """
    total = 150
    max_length = 30
    pattern = "[%-30s] %d%%"
    for i in range(total):
        # do your main task here
        sleep(0.1)

        sys.stdout.write('\r')
        # the exact output you're looking for
        frac = int((i + 1) * 100. / total)
        cur_length = int(frac * max_length * 1. / 100)
        sys.stdout.write(pattern % ('=' * cur_length, frac))
        sys.stdout.flush()
