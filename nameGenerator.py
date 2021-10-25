import random
from typing import List

class NameGenerator:
    def __init__(self, names_list: List[str], surnames_list: List[str]) -> None:
        self.__fullnames = list()
        for name in names_list:
            for surname in surnames_list:
                self.__fullnames.append("{} {}".format(name,  surname))
        self.__start = 0
        self.__end = len(self.__fullnames) - 1

    def __iter__(self):
        return self

    def get_size(self) -> int:
        return len(self.__fullnames) - self.__start

    def generate_name(self) -> str:
        size = self.get_size()
        if (size > 0):
            id = random.randint(self.__start, self.__end)
            name = self.__fullnames[id]
            self.__fullnames[self.__start], self.__fullnames[id] = self.__fullnames[id], self.__fullnames[self.__start]
            self.__start += 1
            return name
        raise StopIteration

    def __next__(self):
        return self.generate_name()
