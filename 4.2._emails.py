filename = input("Enter a file name: ")
counts = {}
with open(filename) as f:
    for line in f:
        if line.startswith("From "):
            words = line.split()
            email = words[1]
            domain = email.split("@")[1]
            counts[domain] = counts.get(domain, 0) + 1

sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
for domain, count in sorted_counts:
    print(f"{domain:20s}: {count:2d} {'*' * count}")
