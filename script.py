import csv

def main():
    with open('empty.tsv', newline='') as tsv:
        reader = csv.reader(tsv, delimiter='\t')
        comment = []
        id = []
        translated = []
        for row in reader:
            comment.append(row[0])
            id.append(row[2])
            translated.append(row[5])


if __name__ == '__main__':
    main()
