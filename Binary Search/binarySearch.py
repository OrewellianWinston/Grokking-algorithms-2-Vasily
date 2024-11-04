
class RoughSearch:
    def __init__(self,array = [1],search_val = 0):
        self.array = sorted(array)
        self.search_val = search_val

    def simple_search(self):
        for index, number in enumerate(self.array):
            try:
                if number == self.search_val:
                    print(f"Your variable is on {index} position")
                    break
            except ValueError:
                print("Not an int")
        else:
            print("NO VALUE")

    def binary_search(self):
        list = self.array
        item = self.search_val
        low = 0
        high = len(list)-1

        while low <= high:
            mid = (low+high) // 2
            guess = list[mid]
            if guess == item:
                print(f"Your value on {mid} position")
                return None
            elif guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return None

