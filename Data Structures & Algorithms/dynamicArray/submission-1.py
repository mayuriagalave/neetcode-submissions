class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [0] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity


# Main function
if __name__ == "__main__":
    arr = DynamicArray(2)

    arr.pushback(10)
    arr.pushback(20)

    print("Array size:", arr.getSize())
    print("Array capacity:", arr.getCapacity())

    arr.pushback(30)  # Automatically doubles capacity

    print("Element at index 2:", arr.get(2))
    print("Array size:", arr.getSize())
    print("Array capacity:", arr.getCapacity())

    arr.set(1, 25)
    print("Updated element at index 1:", arr.get(1))

    print("Removed element:", arr.popback())
    print("Final size:", arr.getSize())
    print("Final capacity:", arr.getCapacity())
