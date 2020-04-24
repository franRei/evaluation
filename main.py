from Reader import Reader
from Mapping import Mapping
from Compare import Compare

filename_wiktionary = "files/wiki_output_with_pgmc_forms.csv"
filename_results = "files/results.csv"

if __name__ == '__main__':
    Reader = Reader()
    Mapping = Mapping()
    Compare = Compare()
    results = Reader.read_csv(filename_results)
    wiki = Reader.read_csv(filename_wiktionary)

    all_words, wiki_words, res_words = Mapping.maps(wiki, results)

    print(len(all_words))
    print(len(wiki_words))
    print(len(res_words))

    Compare.compare(wiki_words, res_words, all_words)