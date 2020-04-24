class Compare:
    def __init__(self):
        pass

    def compare(self, wiki, result, all):
        true_positives = 0
        false_positives = 0
        false_negatives = 0
        borrowed = 0
        for ids, words in wiki.items():
            words_combinations = Compare.get_combinations(self, words)

            #print(words_combinations)
            tp, fn = Compare.count_values(self, words_combinations, "cog_ID_results")

            true_positives += tp

            false_negatives += fn
        for ids_2, words in result.items():
            words_wiki_combination = Compare.get_combinations(self, words)
            tp_wi, fp = Compare.count_values(self, words_wiki_combination, "cog_ID_wiki")
            false_positives += fp


        print(true_positives, false_positives, false_negatives)

        false_positives = false_positives / 2
        print(false_positives)
        precision = true_positives / (true_positives + false_positives)
        recall = true_positives / (true_positives + false_negatives)
        f1 = 2 * ((precision * recall) / (precision + recall))

        print("Precision: ", precision)
        print("Recall: ", recall)
        print("F1-Score: ", f1)
        jaccard = Compare.jaccard(self, true_positives, false_positives, false_negatives)
        print("Jaccard-Index: ", jaccard[0])
        print("Jaccard-Distancce: ", jaccard[1])
        Compare.get_frequency_of_borrowed(self, all)

    def get_combinations(self, lst):
        result = []
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                result.append([lst[i], lst[j]])
        return result

    def count_values(self, word_pairs, id_string):
        """
              counts tp, fp, fn
              """
        lang_dict = {'english': 'en', 'dutch': 'nl', 'swedish': 'sv', 'german': 'de', 'norwegianbokmal': 'nb',
                     'icelandic': 'is', 'danish': 'da'}
        tp = 0
        fn = 0
        fp = 0

        for words in word_pairs:
            if not words == []:
                if words[0][id_string] == words[1][id_string]:
                    tp += 1
                elif words[0][id_string] != words[1][id_string]:
                    fn +=1

        return tp, fn


    def jaccard(self,  tp, fp, fn):
        similarity = tp/(tp + fp + fn)
        return similarity, 1-similarity


    def get_frequency_of_borrowed(self, borr_wiki):
        borrowed = 0
        borr2 = 0
        for words in borr_wiki:
            if words["borrowed"] == "true":
                borrowed += 1
            elif words["borrowed"] == "false":
                borr2 +=1
        all = len(borr_wiki)

        relative = borrowed/all
        print("absolute borrowed: ", borrowed)
        print("relative borrowed: ", relative)
        print("all: ", all)
        print("false: ", borr2)
        return borrowed