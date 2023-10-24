from __future__ import annotations
import math
from typing import Any
from collections import deque

# task_1

class File:
    def __init__(self, path: str) -> None:
        self.path = path

    def __enter__(self) -> File:
        file = open(self.path, 'w+')
        self.file = file
        return self
    
    def __exit__(self, exc_type: Exception, exc_val: Exception, exc_tb: Any) -> None:
        self.file.close()

    def write(self, str: str) -> None:
        try:
            self.file.write(f'{str}\n')
        except Exception as e:
            self.__exit__(Exception, e, e.__traceback__)

# task_2


class MyMath:
    """
    static class for math calculations
    """
    def __new__(cls) :
        raise TypeError(f'{MyMath.__name__} is static class')
    
    @staticmethod 
    def circle_len(radius: float | int) -> float | int:
        """
        returns length of circumference of circle
        """
        if radius < 0:
            raise ValueError
        return radius * 2 * math.pi
    
    @staticmethod
    def circle_sq(radius: float | int) -> float | int:
        """
        returns square of circle
        """
        if radius < 0:
            raise ValueError
        return math.pi * radius ** 2
    
    @staticmethod
    def cube_vl(length: float | int) -> float | int:
        """
        returns volume of cube
        """
        if length < 0:
            raise ValueError
        return length ** 3
    
    @staticmethod
    def sphere_sur_area(radius):
        """
        returns surface area of sphere
        """
        if radius < 0:
            raise ValueError
        return 4 * math.pi * radius ** 2

# task_3

class Date:
    """
    static class for date
    """
    def __new__(cls) :
        raise TypeError(f'{MyMath.__name__} is static class')
    
    @staticmethod
    def is_date_valid(str: str) -> bool:
        """
        checks if str is in "DD-MM-YYYY" format
        """
        dates = str.split('-')

        if len(dates) != 3:
            return False
        day, month, year = map(lambda date: int(date), dates)
        if day < 0 or day > 31:
            return False
        if month < 0 or month > 12:
            return False
        if year < 0:
            return False
        
        return True
    
    @staticmethod
    def from_string(str: str) -> str:
        """
        returns simplified string
        """
        if not Date.is_date_valid(str):
            raise ValueError
        
        dates = str.split('-')
        day, month, year = dates
        return f'День: {day}    Месяц: {month}    Год: {year}'
    
# task_4

class LRUCache:
    def __init__(self, capacity) -> None:
        self.values = dict()
        self.sequence = deque(maxlen=capacity)
        self.capacity = capacity

    def get(self, key):
        if key in self.values:
            return self.values[key]
        raise KeyError
    
    @property
    def cache(self):
        return self.values[self.sequence[0]]

    @cache.setter
    def cache(self, kv):
        key, value = kv
        if key in self.values:
            self.sequence.remove(key)
        elif self.capacity == len(self.values):
            del self.values[self.sequence.popleft()]
        self.sequence.append(key)
        self.values[key] = value

    def print_cache(self):
        print(', '.join([": ".join(kv) for kv in self.values.items()]))