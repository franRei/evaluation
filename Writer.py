import csv
class Writer:
    def __init__(self):
        pass

    def write_csv(self, aux, filename):
        with open(filename, mode='w') as csv_results:
            result_writer = csv.writer(csv_results, delimiter='\t')
            result_writer.writerow(['status', 'ID_1', 'cognate_1', 'language_1', 'cognateID_results_1', 'cognateID_wiki_1',
                                    'borrowed_1', 'pgmc_forms_results_1', 'pgmc_forms_wiki_1', '',
                                    'ID_2', 'cognate_2', 'language_2', 'cognateID_results_2', 'cognateID_wiki_2',
                                    'borrowed_2', 'pgmc_forms_results_2', 'pgmc_forms_wiki_2'])
            #tp
            for words in aux[0]:
                result_writer.writerow(["tp", words[0]["id"], words[0]["cognate"], words[0]["language"], words[0]["cog_ID_results"], words[0]["cog_ID_wiki"],
                                        words[0]["borrowed"], words[0]["pgmc_results"], words[0]["pgmc_wiki"], '',
                                        words[1]["id"], words[1]["cognate"], words[1]["language"], words[1]["cog_ID_results"], words[1]["cog_ID_wiki"],
                                        words[1]["borrowed"], words[1]["pgmc_results"], words[1]["pgmc_wiki"]])
            #fp
            for words in aux[1]:
                result_writer.writerow(["fp", words[0]["id"], words[0]["cognate"], words[0]["language"], words[0]["cog_ID_results"], words[0]["cog_ID_wiki"],
                                        words[0]["borrowed"], words[0]["pgmc_results"], words[0]["pgmc_wiki"], '',
                                        words[1]["id"], words[1]["cognate"], words[1]["language"], words[1]["cog_ID_results"], words[1]["cog_ID_wiki"],
                                        words[1]["borrowed"], words[1]["pgmc_results"], words[1]["pgmc_wiki"]])
            #fn
            for words in aux[2]:
                result_writer.writerow(["fn", words[0]["id"], words[0]["cognate"], words[0]["language"], words[0]["cog_ID_results"], words[0]["cog_ID_wiki"],
                                        words[0]["borrowed"], words[0]["pgmc_results"], words[0]["pgmc_wiki"], '',
                                        words[1]["id"], words[1]["cognate"], words[1]["language"], words[1]["cog_ID_results"], words[1]["cog_ID_wiki"],
                                        words[1]["borrowed"], words[1]["pgmc_results"], words[1]["pgmc_wiki"]])
        csv_results.close()


    def write_csv_by_status(self, aux, filename):
        with open(filename, mode='w') as csv_results:
            result_writer = csv.writer(csv_results, delimiter='\t')
            result_writer.writerow(['ID_1', 'cognate_1', 'language_1', 'cognateID_results_1', 'cognateID_wiki_1',
                                    'borrowed_1', 'pgmc_forms_results_1', 'pgmc_forms_wiki_1', '',
                                    'ID_2', 'cognate_2', 'language_2', 'cognateID_results_2', 'cognateID_wiki_2',
                                    'borrowed_2', 'pgmc_forms_results_2', 'pgmc_forms_wiki_2'])

            for words in aux:
                result_writer.writerow([words[0]["id"], words[0]["cognate"], words[0]["language"], words[0]["cog_ID_results"],words[0]["cog_ID_wiki"],
                                        words[0]["borrowed"], words[0]["pgmc_results"], words[0]["pgmc_wiki"], '', words[1]["id"], words[1]["cognate"],
                                        words[1]["language"], words[1]["cog_ID_results"], words[1]["cog_ID_wiki"], words[1]["borrowed"], words[1]["pgmc_results"], words[1]["pgmc_wiki"]])
        csv_results.close()

    def write_csv_by_status_only_short(self, aux, filename):
        with open(filename, mode='w') as csv_results:
            result_writer = csv.writer(csv_results, delimiter='\t')
            result_writer.writerow(['ID_1', 'cognate_1', 'language_1','cognateID_results_1', 'cognateID_wiki_1', '',
                                    'ID_2', 'cognate_2','language_2', 'cognateID_results_2', 'cognateID_wiki_2'])

            for words in aux:
                result_writer.writerow([words[0]["id"], words[0]["cognate"], words[0]["language"], words[0]["cog_ID_results"], words[0]["cog_ID_wiki"],
                                        '', words[1]["id"], words[1]["cognate"], words[1]["language"], words[1]["cog_ID_results"], words[1]["cog_ID_wiki"]])
        csv_results.close()


    def write_csv_only_short(self, aux, filename):
        with open(filename, mode='w') as csv_results:
            result_writer = csv.writer(csv_results, delimiter='\t')
            result_writer.writerow(['status', 'ID_1', 'cognate_1', 'language_1','cognateID_results_1', 'cognateID_wiki_1', '',
                                    'ID_2', 'cognate_2','language_2', 'cognateID_results_2', 'cognateID_wiki_2'])
            #tp
            for words in aux[0]:
                result_writer.writerow(["tp", words[0]["id"], words[0]["cognate"], words[0]["language"], words[0]["cog_ID_results"], words[0]["cog_ID_wiki"],
                                        '', words[1]["id"], words[1]["cognate"], words[1]["language"], words[1]["cog_ID_results"], words[1]["cog_ID_wiki"]])
            #fp
            for words in aux[1]:
                result_writer.writerow(["fp", words[0]["id"], words[0]["cognate"], words[0]["language"], words[0]["cog_ID_results"], words[0]["cog_ID_wiki"],
                                        '', words[1]["id"], words[1]["cognate"], words[1]["language"], words[1]["cog_ID_results"], words[1]["cog_ID_wiki"]])
            #fn
            for words in aux[2]:
                result_writer.writerow(["fn", words[0]["id"], words[0]["cognate"], words[0]["language"], words[0]["cog_ID_results"], words[0]["cog_ID_wiki"],
                                        '', words[1]["id"], words[1]["cognate"], words[1]["language"], words[1]["cog_ID_results"], words[1]["cog_ID_wiki"]])
        csv_results.close()