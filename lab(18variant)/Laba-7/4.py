class Shuttle:
    def __init__(self, name, capacity, speed, fuel):
        self.name = name
        self.capacity = capacity
        self.speed = speed
        self.fuel = fuel
        self._attributes = [self.name, self.capacity, self.speed, self.fuel]
        self._index = 0

    def __lt__(self, other):
        return self.capacity < other.capacity

    def __le__(self, other):
        return self.capacity <= other.capacity

    def __gt__(self, other):
        return self.capacity > other.capacity

    def __ge__(self, other):
        return self.capacity >= other.capacity

    def __eq__(self, other):
        return self.capacity == other.capacity

    def __ne__(self, other):
        return self.capacity != other.capacity

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self._attributes):
            result = self._attributes[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __repr__(self):
        return f"Shuttle(name={self.name}, capacity={self.capacity}, speed={self.speed}, fuel={self.fuel})"


shuttle1 = Shuttle("Apollo", 100, 5000, 1000)
shuttle2 = Shuttle("Atlantis", 120, 5500, 1200)
shuttle3 = Shuttle("Challenger", 90, 4800, 950)

print(f"shuttle1 < shuttle2 -> {shuttle1 < shuttle2}")
print(f"shuttle1 > shuttle3 -> {shuttle1 > shuttle3}")

for attribute in shuttle1:
    print(attribute)

shuttles = [shuttle1, shuttle2, shuttle3]
shuttles.sort()
print(shuttles)
