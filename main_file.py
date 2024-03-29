import re

from bs4 import BeautifulSoup
from pre_commit_test.local_lib import LocalLibClass

GLOBAL_VARIABLE = 10


# change for tests
class MainClass(object):
    def __init__(self):

        self.first_variable = 1
        self.second_variable = [
            value for value in range(10, 1000, 2) if value % 10 == 3
        ]
        self.third_variable = (
            'This is a very very very long string that shouldn\'t be in one '
            'line only because it has more than 80 characters')

        self.local_lib_reference = LocalLibClass()
        self.fourth_variable = self.local_lib_reference.sum(
            self.first_variable, self.first_variable)
        self.regex = re.compile(r'\d+')
        self.soup = BeautifulSoup()
