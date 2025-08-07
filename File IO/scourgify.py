import csv
import sys

students = []


def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")

        with open(sys.argv[1]) as file:
            if file.read().strip() == "":
                sys.exit(f"Could not read {sys.argv[1]}")

        read_file()
        write_file()

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


def read_file():
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for line in reader:
            last, first = line["name"].split(", ")
            students.append({"first": first, "last": last, "house": line["house"]})
    for student in students:
        print(f'"{student["first"]} {student["last"]}", {student["house"]}')


def write_file():
    with open(sys.argv[2], "w") as file:
        writer = csv.writer(file)
        writer.writerow(["first", "last", "house"])
        for student in students:
            writer.writerow([student["first"], student["last"], student["house"]])


if __name__ == "__main__":
    main()