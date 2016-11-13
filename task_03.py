#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """Class for logs."""

    def __init__(self, logfilename):
        """Constructor for CustomLogger class."""
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """Function to track logs."""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """Function to open files and record logs."""
        handled = []
        try:
            fhandler = open(self.logfilename, 'a')
        except self.log('Cannot open file'):
            raise
        except self.log(IOError):
            pass
        for index, entry in enumerate(self.msgs):
            try:
                fhandler.write(str(entry) + '\n')
                handled.append(index)
            except self.log(IOError):
                raise IOError
            finally:
                fhandler.close()

            for index in handled[::-1]:
                if self.msgs[index] in handled.append(index):
                    del self.msgs[index]
