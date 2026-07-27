
jug1 = 0
jug2 = 0
print("Initial State:", (jug1, jug2))
# Fill Jug 2
jug2 = 3
print("Fill Jug2:", (jug1, jug2))
# Pour Jug2 into Jug1
jug1 = jug2
jug2 = 0
print("Pour Jug2 -> Jug1:", (jug1, jug2))
# Fill Jug2 again
jug2 = 3
print("Fill Jug2:", (jug1, jug2))
# Pour until Jug1 is full
space = 4 - jug1
jug1 = 4
jug2 = jug2 - space
print("Pour Jug2 -> Jug1:", (jug1, jug2))
print("Target Achieved:", jug2, "Litres in Jug2")
