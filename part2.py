"""
FILE:   InferenceEngine.py

AUTHOR: Alexander S. Adranly

A simple resolution function that resolves two sentences that are already in CNF - Conjunctive Normal Form-

CNF -Conjunctive Normal Form-
: a conjunction of disjunctions -aka- and AND of ORs
: 

"""
import part1 as resolver


class InferenceEngine(object):
    """
    Description of the resolution inference engine
    """
    def __init__(self):
        # anything that we know is actually true and given in our kb
        self.knowledge_base = list()
        # anything that we do not know is given or true in our kb, since it is just
        # apart of the inference process
        self.inference_scratch_pad = list()

    # API FUNCTIONS
    def tell(self, cnf_sentence):
        """
        
        :param cnf_sentence: 
        :return: 
        """
        for item in self.knowledge_base:
            if cmp(cnf_sentence, item) == 0:
                break
        else:
            # add to scratch pad
            self.knowledge_base.append(cnf_sentence)

    def ask(self, cnf_query):
        """
        Yes, for part 2 it should accept any CNF clause. 
        For example ["or", "a", "b", ["not", "c"]] is OK, but ["and", "a", "b"] is not.
        
        :param cnf_query: 
        :return: 
        """
        # make sure that query is in CNF
        if self.__is_cnf__(s=cnf_query) is False:
            print "not cnf form!!"
            return False

        # evaluate CNF QUERY
        query = cnf_query if type(cnf_query) is list else list(cnf_query)
        negation = self.__not__(query)

        self.inference_scratch_pad.append(negation)
        for info in self.knowledge_base:
            self.append_to_scratch(info)

        # keep on resolving until satisfiable ( no new resolutions are possible)
        #   a way of saying that is if the new number of propositions is the same as the old number of
        #   propositions
        # or there is a contradiction
        last_proposition_count = 0
        current_proposition_count = len(self.inference_scratch_pad)
        self.display_scratch()
        print "\n"
        conclusions = list()

        while last_proposition_count != current_proposition_count:
            self.display_scratch()
            last_proposition_count = current_proposition_count
            # resolve all information in the scratch pad
            for select in self.inference_scratch_pad:
                for resolvee in self.inference_scratch_pad:
                    result = resolver.resolve(select, resolvee)
                    if result is False:
                        # !!! Do NOT resolve !!!
                        continue
                    elif len(result) == 0:
                        # !!! contradiction !!!
                        # means that the proposed solution is true
                        return True
                    else:
                        # !!! there is an actual resolution answer !!!
                        conclusions.append(result)

            for item in conclusions:
                self.append_to_scratch(item)

            del conclusions[:]  # clean conclusion list for next time
            current_proposition_count = len(self.inference_scratch_pad)
            # self.display_scratch()
            # raw_input('press enter to continue')

        self.display_scratch()
        # add conclusions to the scratchpad
        # clear all the inference scratch work
        del self.inference_scratch_pad[:]
        return False

    def clear(self):
        """
        
        :return: 
        """
        del self.knowledge_base[:]

    # HELPER FUNCTIONS

    def append_to_scratch(self, sentence):
        """
        
        :param sentence: 
        :return: 
        """
        # print sentence
        # check if the item is in the list or not
        for item in self.inference_scratch_pad:
            if cmp(sentence, item) == 0:
                break
        else:
            # add to scratch pad
            self.inference_scratch_pad.append(sentence)

    def summation(self, num):
        """
        
        :param num: 
        :return: 
        """
        if int(num) == 0:
            return 0
        else:
            return num + self.summation(num-1)

    def __not__(self, sentence):
        """
        
        :param sentence: 
        :return: 
        """
        result = []

        if len(sentence) == 1:
            # only one literal
            result.append('not')
            result.append(sentence[0])
        elif sentence[0] == 'not':
            # it is already a negated literal
            result = list(sentence[1])

        elif sentence[0] == 'or':
            # result would have or in it
            # an OR of literals
            result.append('and')
            for item in sentence[1:]:
                result.append(self.__not__(item))

        return result

    @staticmethod
    def __is_cnf__(s):
        """
        Determine if the given sentence is in a valid CNF form or not
        
        :param s: 
        :return: 
        """
        sentence = s if type(s) is list else list(s)

        if type(sentence) is not list:
            return False
        elif len(sentence) == 0:
            return False
        elif len(sentence) == 1:
            if sentence[0] in resolver.KEY_WORDS:
                return False
        else:
            # len(sentence) > 1
            if sentence[0] == 'or':
                for item in sentence[1:]:
                    if type(item) is list:
                        # process as list (should have not)
                        if item[0] != 'not':
                            return False
                        elif len(item) != 2:
                            return False

                    else:
                        # item is not a list
                        if type(item) is not str:
                            return False

                        if item in resolver.KEY_WORDS:
                            return False

            elif sentence[0] == 'not':
                if len(sentence) != 2:
                    return False
                if sentence[1] in resolver.KEY_WORDS:
                    return False
            else:
                return False

        return True

    def display_progress(self):
        """
        
        :return: 
        """
        self.display_kb()
        print "\n", '_'*10
        print "SCRATCH\n_______"
        for sentence in self.inference_scratch_pad:
            print str(sentence)

    def display_kb(self):
        """
        
        :return: 
        """
        print "KB\n______"
        for sentence in self.knowledge_base:
            print str(sentence)

    def display_scratch(self):
        print "SCRATCH\n_______"
        for sentence in self.inference_scratch_pad:
            print str(sentence)