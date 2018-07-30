import re
import sys


class Matcher:

    def __init__(self, pattern, flags=0):
        self._pattern = re.compile(pattern, flags)
        self._lastOne = None
        self._match = None
        self._search = None

    def match(self, line):

        self._match = re.match(self._pattern, line)
        self._lastOne = 'Match'
        return self._match

    def search(self, line):

        self._search = re.search(self._pattern, line)
        self._lastOne = 'Search'
        return self._search

    def group(self, idx):

        if self._lastOne == 'Match':
            return self._match.group(idx)
        elif self._lastOne == 'Search':
            return self._search.group(idx)
        else:
            print('I dun goofed')

    def groups(self):

        if self._lastOne == 'Match':
            return self._match.groups()
        elif self._lastOne == 'Search':
            return self._search.groups()
        else:
            print('I dun goofed')
