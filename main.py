
def style(pattern):
    columns = int(input("Enter Pattern columns: "))
    for pattern in range(1, columns):
        for internal in range(pattern-1):
            print("\t", "*", end=" ")

        print("\t", "*")
    for reverse in range(columns, 0, -1):
        for internal in range(reverse-1):
            print("\t", "*", end=" ")

        print("\t", "*")

    return style


style("*")