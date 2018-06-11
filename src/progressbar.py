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
    """Summary
    """
    total = 150
    for i in range(total):
        # do your main task here
        sleep(0.1)

        sys.stdout.write('\r')
        # the exact output you're looking for
        frac = int((i + 1) * 100. / total)
        sys.stdout.write("[%-20s] %d%%" % ('=' * int(frac / 5), frac))
        sys.stdout.flush()
