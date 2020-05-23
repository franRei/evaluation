from Reader import Reader
from Mapping import Mapping
from Compare import Compare
from Writer import Writer

#gold standard
filename_wiktionary = "files/wiki_output_with_pgmc_forms.csv"
#test languages
filename_results = "files/results.csv"
#validation languages
filename_extend = "files/results_kroonen_northeuralex.csv"

if __name__ == '__main__':
    Reader = Reader()
    Mapping = Mapping()
    Compare = Compare()
    Writer = Writer()

    #reads files
    results = Reader.read_csv(filename_results)
    wiki = Reader.read_csv(filename_wiktionary)
    validation_set = Reader.read_csv(filename_extend)

    #maps wiki to test set
    all_words, wiki_words, res_words, id_lst = Mapping.maps(wiki, results)

    print("all words common between both lists:", len(all_words))
    print("wiktionary cognate sets", len(wiki_words))
    print("results cognate sets", len(res_words))

    #compares data and outputs results
    aux_test = Compare.compare(wiki_words, res_words, all_words)

    #numbers borrowed to wiktionary
    print("Borrowed whole wiki:")
    Compare.get_frequency_of_borrowed(wiki)

    #writes tsv separated for tp, fp, fn
    Writer.write_csv(aux_test, "res/results_case.tsv")

    #validation set
    print("\nVALIDATION STARTS HERE:\n")
    #maps wiki to validation set
    all_val, wiki_val, res_words_val = Mapping.maps_val(wiki, validation_set, id_lst)
    print("all words common between both lists:", len(all_val))
    print("wiktionary cognate sets", len(wiki_val))
    print("results cognate sets", len(res_words_val))

    #compares data and outputs tp, fp, fn
    aux_val = Compare.compare(wiki_val, res_words_val, all_val)

    #precision, recall, f1 for test and validation set
    Compare.validation(aux_test, aux_val)

    Writer.write_csv_by_status(aux_val[1], "val/results_fp_val.tsv")
