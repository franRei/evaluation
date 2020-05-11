from Reader import Reader
from Mapping import Mapping
from Compare import Compare
from Writer import Writer

filename_wiktionary = "files/wiki_output_with_pgmc_forms.csv"
filename_results = "files/results.csv"

if __name__ == '__main__':
    Reader = Reader()
    Mapping = Mapping()
    Compare = Compare()
    Writer = Writer()
    results = Reader.read_csv(filename_results)
    wiki = Reader.read_csv(filename_wiktionary)

    all_words, wiki_words, res_words = Mapping.maps(wiki, results)

    print("all words common between both lists:", len(all_words))
    print("wiktionary cognate sets", len(wiki_words))
    print("results cognate sets", len(res_words))

    aux = Compare.compare(wiki_words, res_words, all_words)

    print("Borrowed whole wiki:")
    Compare.get_frequency_of_borrowed(wiki)

    Writer.write_csv(aux)
    Writer.write_csv_only_short(aux)

    Writer.write_csv_by_status("res/results_tp.tsv", aux[0])
    Writer.write_csv_by_status("res/results_fp.tsv", aux[1])
    Writer.write_csv_by_status("res/results_fn.tsv", aux[2])


    Writer.write_csv_by_status_only_short("res/results_tp_short.tsv", aux[0])
    Writer.write_csv_by_status_only_short("res/results_fp_short.tsv", aux[1])
    Writer.write_csv_by_status_only_short("res/results_fn_short.tsv", aux[2])

