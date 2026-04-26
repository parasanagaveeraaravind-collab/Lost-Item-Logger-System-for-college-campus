import matplotlib.pyplot as plt
from collections import Counter

# ---------------------------
# Sample Data
# ---------------------------
lost_items = [
    {"item": "ID Card", "location": "Library"},
    {"item": "Wallet", "location": "Canteen"},
    {"item": "Mobile", "location": "Classroom"},
    {"item": "Keys", "location": "Hostel"},
    {"item": "ID Card", "location": "Playground"},
]

found_items = [
    {"item": "Wallet", "location": "Canteen"},
    {"item": "Mobile", "location": "Classroom"},
    {"item": "Bag", "location": "Library"},
    {"item": "Keys", "location": "Hostel"},
]

# ---------------------------
# Matching Function
# ---------------------------
def match_items(lost, found):
    matched = []
    unmatched = []

    for l in lost:
        found_match = False
        for f in found:
            if l["item"] == f["item"] and l["location"] == f["location"]:
                matched.append(l)
                found_match = True
                break
        if not found_match:
            unmatched.append(l)

    return matched, unmatched

matched, unmatched = match_items(lost_items, found_items)

# ---------------------------
# GRAPH 1: Item Frequency (Bar)
# ---------------------------
item_names = [i["item"] for i in lost_items]
item_count = Counter(item_names)

plt.figure()
plt.bar(list(item_count.keys()), list(item_count.values()))
plt.title("Lost Items Frequency")
plt.xlabel("Items")
plt.ylabel("Count")
plt.xticks(rotation=30)
plt.show()

# ---------------------------
# GRAPH 2: Match Analysis (Bar)
# ---------------------------
labels_bar = ["Matched", "Unmatched"]
values_bar = [len(matched), len(unmatched)]

plt.figure()
plt.bar(labels_bar, values_bar)
plt.title("Match Analysis (Bar Graph)")
plt.xlabel("Status")
plt.ylabel("Number of Items")
plt.show()

# ---------------------------
# GRAPH 3: Match Analysis (Pie)
# ---------------------------
plt.figure()
plt.pie(values_bar, labels=labels_bar, autopct="%1.1f%%")
plt.title("Match Analysis (Pie Chart)")
plt.show()

# ---------------------------
# GRAPH 4: Location Analysis (Bar)
# ---------------------------
locations = [i["location"] for i in lost_items]
location_count = Counter(locations)

plt.figure()
plt.bar(list(location_count.keys()), list(location_count.values()))
plt.title("Lost Items by Location")
plt.xlabel("Location")
plt.ylabel("Count")
plt.xticks(rotation=30)
plt.show()