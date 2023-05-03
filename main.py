#!/usr/bin/env python3
import csv
import genetics


def main():
    males=[]
    females=[]
    with open("./config.csv", 'r') as config_file:
        csvrows = csv.reader(config_file)
        next(csvrows)
        for row in csvrows:
            if row[2] == "male":
                males.append(genetics.Monster(row[0],row[1],int(row[3])))
            elif row[2] == "female":
                females.append(genetics.Monster(row[0],row[1],int(row[3])))
            else:
                raise ValueError(f"Gender unspecified: {row}")

    for m in males:
        for f in females:
            print(f"{m} + {f} = {m.breed(f)}")
            print(f"{f} + {m} = {f.breed(m)}")

if __name__ == "__main__":
    main()
