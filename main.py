
# program for star pattern
def stars(pattern):
    for pattern in range(5, 0, -1):
        for lower_pattern in range(pattern-1):
            print("*", end=" ")
        print("*")
    return stars


stars(404)

print(stars(404))
