class Mapping:
    def __init__(self):
        pass

    def maps(self, wik, res):
        word_count = 0
        combined = []
        combined_sort_by_wiki_cog_id = {}
        combined_sort_by_res_cog_id = {}

        for word_res in res:
            for word_wiki in wik:
                if word_res["cognate"] == word_wiki["cognate"] and word_res["language"] == word_wiki["language"]:
                    word_count += 1
                    word_group = {"id": word_res['id'], "cognate": word_res['cognate'],\
                                  "language": word_res['language'], "borrowed": word_wiki['borrowed'],\
                                  "cog_ID_wiki": word_wiki['cog_ID'], "cog_ID_results": word_res['cog_ID'],\
                                  "pgmc_wiki": word_wiki['pgmc'], "pgmc_results": word_res['pgmc']}
                    combined.append(word_group)
                    if word_group["cog_ID_wiki"] in combined_sort_by_wiki_cog_id:
                        combined_sort_by_wiki_cog_id[word_group["cog_ID_wiki"]].append(word_group)
                    else:
                        combined_sort_by_wiki_cog_id[word_group["cog_ID_wiki"]] = [word_group]

                    if word_group["cog_ID_results"] in combined_sort_by_res_cog_id:
                        combined_sort_by_res_cog_id[word_group["cog_ID_results"]].append(word_group)
                    else:
                        combined_sort_by_res_cog_id[word_group["cog_ID_results"]] = [word_group]

        return combined, combined_sort_by_wiki_cog_id, combined_sort_by_res_cog_id
