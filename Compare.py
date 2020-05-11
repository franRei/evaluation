class Compare:
    def __init__(self):
        pass

    def compare(self, wiki, result, all):
        """

        :param wiki: dict cognates, sorted by wiki set id
        :param result: dict cognates, sorted by result set id
        :param all: all common cognates
        :return: tp, fp, fn lists of pairs
        """
        true_positives = 0
        false_positives = 0
        false_negatives = 0
        tp_wikitionary = 0
        tp_lst = []
        fn_lst = []
        fp_lst = []
        for ids, words in wiki.items():
            words_combinations = Compare.get_combinations(self, words)

            tp, fn, aux = Compare.count_values(self, words_combinations, "cog_ID_results")

            true_positives += tp
            false_negatives += fn
            tp_lst.extend(aux[0])
            fn_lst.extend(aux[1])

        for ids_2, words in result.items():
            words_wiki_combination = Compare.get_combinations(self, words)
            tp_wi, fp, aux = Compare.count_values(self, words_wiki_combination, "cog_ID_wiki")
            tp_wikitionary += tp_wi
            false_positives += fp
            fp_lst.extend(aux[1])


        print("true positives: ",true_positives)
        print("false positives: ", false_positives)
        print("false negatives: ", false_negatives)
        #print("res tp: ", tp_wikitionary)

        false_positives = false_positives
        precision = true_positives / (true_positives + false_positives)
        recall = true_positives / (true_positives + false_negatives)
        f1 = 2 * ((precision * recall) / (precision + recall))

        print("Precision: ", precision)
        print("Recall: ", recall)
        print("F1-Score: ", f1)

        jaccard = Compare.jaccard(self, true_positives, false_positives, false_negatives)
        print("Jaccard-Index: ", jaccard[0])
        print("Jaccard-Distance: ", jaccard[1])

        print("Borrowed with combined set:")
        Compare.get_frequency_of_borrowed(self, all)
        print(tp_lst)
        return tp_lst, fp_lst, fn_lst


    def get_combinations(self, lst):
        """
        creates pairs of every entry in lst
        :param lst: list of cognates
        :return: list of pairs
        """
        result = []
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                result.append([lst[i], lst[j]])
        return result

    def count_values(self, word_pairs, key_id):
        """
        counts tp, fp, fn
        :param word_pairs: pairs of words
        :param key_id: in which key to check
        :return: tp, fn
        """
        tp = 0
        fn = 0
        lst_tp = []
        lst_fn = []

        for words in word_pairs:
            if not words == []:
                if words[0][key_id] == words[1][key_id]:
                    tp += 1
                    lst_tp.append((words[0], words[1]))
                elif words[0][key_id] != words[1][key_id]:
                    fn +=1
                    lst_fn.append((words[0], words[1]))
        return tp, fn, [lst_tp, lst_fn]


    def jaccard(self,  tp, fp, fn):
        """
        calculates jaccard coeff and distance
        :return: jaccard coeff, jaccard distance
        """
        similarity = tp/(tp + fp + fn)
        return similarity, 1-similarity


    def get_frequency_of_borrowed(self, wiki):
        """
        calculates frequency of borrowed
        :param wiki: set of all entries
        :return: count of borrowed cognates
        """
        borrowed = 0
        for words in wiki:
            if words["borrowed"] == "true":
                borrowed += 1
        all = len(wiki)

        relative = borrowed/all
        print("absolute borrowed: ", borrowed)
        print("relative borrowed: ", relative)
        print("all: ", all)

        return borrowed