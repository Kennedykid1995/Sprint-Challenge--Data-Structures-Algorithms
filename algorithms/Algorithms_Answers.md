Add your answers to the Algorithms exercises here.
-- Exercise 1

a) O(log N)

b)O(n ^ 2)

c)O(n)


--Exercise 2
def egg_building(n, f):
    if f > n:
        print("That building doesn't exist")
    elif f > n // 2:
        print ("Your eggs are gonna break")
    else:
        print("The chances are slim for broken eggs")

