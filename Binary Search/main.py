from randomArrayGenerator import RandomArrayGenerator
from binarySearch import RoughSearch

Variable_1 = RandomArrayGenerator(1_000_0000)
Search_1 = RoughSearch(Variable_1.array,1024)
#Search_1.simple_search()
Search_1.binary_search()
