import hashlib

class BloomFilter:
    def __init__(self, size=20):
        self.size = size
        self.bits = [0] * size

    # Two hash functions (convert number → string for hashing)
    def h1(self, num):
        return int(hashlib.md5(str(num).encode()).hexdigest(), 16) % self.size

    def h2(self, num):
        return int(hashlib.sha1(str(num).encode()).hexdigest(), 16) % self.size

    # Insert number into Bloom Filter
    def insert(self, num):
        i1, i2 = self.h1(num), self.h2(num)
        self.bits[i1] = self.bits[i2] = 1
        print(f"Inserted {num} → bits {i1}, {i2}")

    # Check if number may exist
    def lookup(self, num):
        i1, i2 = self.h1(num), self.h2(num)
        if self.bits[i1] and self.bits[i2]:
            print(f"{num} → may be present")
        else:
            print(f"{num} → not present")

    def show(self):
        print("Bit Array:", self.bits)

# ---------------- DRIVER CODE ----------------
bf = BloomFilter(20)

# Insert numeric data
bf.insert(10)
bf.insert(25)
bf.insert(35)

bf.show()

print("\nLookup:")
for n in [10, 25, 35, 50, 75]:
    bf.lookup(n)
