# 🧠 Aim:
# To count how many times each word appears in the given text input
# using a simple MapReduce simulation in Python.

from collections import defaultdict

# --- Map Step ---
# Splits each line into words and maps them as (word, 1)
def map_step(lines):
    mapped = []
    for line in lines:
        for word in line.strip().split():
            mapped.append((word.lower(), 1))
    return mapped


# --- Shuffle Step ---
# Groups all values (1s) by word
def shuffle_step(mapped_data):
    shuffled = defaultdict(list)
    for key, value in mapped_data:
        shuffled[key].append(value)
    return shuffled


# --- Reduce Step ---
# Sums up the counts for each word
def reduce_step(shuffled_data):
    reduced = {}
    for key, values in shuffled_data.items():
        reduced[key] = sum(values)
    return reduced


# --- Main Program ---
if __name__ == "__main__":
    print("Enter text lines (type 'DONE' to finish):")
    lines = []
    
    while True:
        line = input()
        if line.strip().upper() == "DONE":
            break
        lines.append(line)
    
    # Map, Shuffle, Reduce Phases
    mapped = map_step(lines)
    shuffled = shuffle_step(mapped)
    reduced = reduce_step(shuffled)
    
    # Final Output
    print("\n=== Word Count Result ===")
    for word, count in sorted(reduced.items()):
        print(f"{word}: {count}")
