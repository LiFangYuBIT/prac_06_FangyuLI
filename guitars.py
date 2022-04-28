from guitar import Guitar


def main():
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name.strip() != "":
        a = []
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        a.append(name)
        a.append(year)
        a.append(cost)
        other_guitar = Guitar(a[0], a[1], a[2])
        guitars.append(Guitar(a[0], a[1], a[2]))
        print(other_guitar.__str__(), "added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars: ")
    for i, guitar in enumerate(guitars):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
