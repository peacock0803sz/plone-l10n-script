import csv

POFILE = 'empty.po'

def main():
    with open('empty.tsv', newline='') as tsv:
        reader = csv.reader(tsv, delimiter='\t')
        comment = []
        msgid = []
        msgstr = []
        for row in reader:
            comment.append(row[0])
            msgid.append(row[2])
            msgstr.append(row[5])

    length = len(msgid)
    with open(POFILE, mode='w') as f:
        for i in range(1, length):
            f.write(f'#: {comment[i]}\nmsgid "{msgid[i]}"\nmsgstr "{msgstr[i]}"\n\n')

if __name__ == '__main__':
    main()
