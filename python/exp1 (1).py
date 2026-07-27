# 8 Puzzle Problem - Simple Manual Method

# Read initial state
print("Enter the Initial State (use 0 for blank):")
puzzle = []

for i in range(3):
    row = list(map(int, input().split()))
    puzzle.append(row)

# Goal state
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Function to display puzzle
def display():
    for row in puzzle:
        print(row)

# Find blank position
def find_blank():
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j

print("\nGoal State:")
for row in goal:
    print(row)

while puzzle != goal:

    print("\nCurrent State:")
    display()

    x, y = find_blank()

    print("\nMove Blank:")
    print("1. Up")
    print("2. Down")
    print("3. Left")
    print("4. Right")

    choice = int(input("Enter your choice: "))

    if choice == 1 and x > 0:
        puzzle[x][y], puzzle[x-1][y] = puzzle[x-1][y], puzzle[x][y]

    elif choice == 2 and x < 2:
        puzzle[x][y], puzzle[x+1][y] = puzzle[x+1][y], puzzle[x][y]

    elif choice == 3 and y > 0:
        puzzle[x][y], puzzle[x][y-1] = puzzle[x][y-1], puzzle[x][y]

    elif choice == 4 and y < 2:
        puzzle[x][y], puzzle[x][y+1] = puzzle[x][y+1], puzzle[x][y]

    else:
        print("Invalid Move!")

print("\nCongratulations!")
print("Goal State Reached:")
display()