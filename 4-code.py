register_number = int(input("Enter your register number:"))
D = register_number % 10
print("Register digit:", D)
n = int(input("How many scores do you want to enter?"))
scores = []
j=0
while j < n:
    value = int(input("Enter score:"))
    scores = scores + [value]
    j = j + 1
low = []
medium = []
high = []
critical = []

total = 0
ignored = 0
removed = 0

for s in scores:
    if s < 0:
        ignored = ignored + 1
    else:
        total = total + 1
        if s >= 0 and s <=30:
            low = low + [s]
        elif s >=31 and s <=60:
            medium = medium + [s]
        elif s >=61 and s <=100:
            high = high + [s]
        else:
            critical = critical + [s]
print("\nBefore Filtering:")
print("Low:", low)
print("Medium:", medium)
print("High:", high)
print("Critical:", critical)

if D % 2 == 0:
    for i in low:
        removed = removed + 1
    low = []
else:
    for i in critical:
        removed = removed + 1
    critical = []
print("\nAfter Filtering:")
print("Low:", low)
print("Medium:", medium)
print("High:", high)
print("Critical:", critical)

print("\nTotal Scores:", total)
print("\nIgnored Scores:", ignored)
print("\nRemoved Scores:", removed)
