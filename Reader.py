import csv
class Reader:
    def __init__(self):
        pass

    def read_csv(self, filename):
        with open(filename) as csv_data:
            reader = csv.DictReader(csv_data)
            line_count = 0
            list_of_dict = []

            for lines in reader:
                word_group = {"id": lines['ID'].strip(), "cognate": lines['cognate'].strip(), "language": lines['lang'].strip(), \
                             "cog_ID":lines['cognateID'].strip(), "borrowed":lines['borrowed'].strip(), "pgmc":lines['pgmc_forms'].strip()}
                line_count += 1
                list_of_dict.append(word_group)

                print(word_group)

            print(line_count)
            return list_of_dict

