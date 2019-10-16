import csv

POFILE = 'plone.po'


def main():
    with open('empty.tsv', newline='') as tsv:
        reader = csv.reader(tsv, delimiter='\t')
        msgid = []
        msgstr = []
        for row in reader:
            msgid.append(row[2])
            msgstr.append(row[5])
        del(msgid[:1])
        del(msgstr[:1])

    with open(POFILE, mode='r') as f:
        target = []
        lines = f.readlines()
        for line in lines:
            if line.startswith(ID_PREFIX):
                for i in range(len(msgid)):
                    if line == f'msgid "{msgid[i]}"\n':
                        target.append(lines.index(line) + 1)
        for i in range(len(msgstr)):
            del lines[target[i]]
            lines.insert(target[i], f'msgstr "{msgstr[i]}"\n\n')
    with open(POFILE, mode='w') as f:
        for i in lines:
            f.write(i)


if __name__ == '__main__':
    main()
