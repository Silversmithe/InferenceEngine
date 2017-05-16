"""
FILE:   InferenceEngine.py

AUTHOR: Alexander S. Adranly

A simple resolution function that resolves two sentences that are already in CNF - Conjunctive Normal Form-

CNF -Conjunctive Normal Form-
: a conjunction of disjunctions -aka- and AND of ORs
: 

"""
import Resolution as Resolver


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
        self.knowledge_base.append(cnf_sentence)

    def ask(self, cnf_query):
        """
        
        :param cnf_query: 
        :return: 
        """
        negation = ['not', cnf_query]
        self.inference_scratch_pad.append(negation)
        self.inference_scratch_pad.extend(self.knowledge_base)
        conclusions = list()

        # keep on resolving until satisfiable ( no new resolutions are possible)
        # or there is a contradiction
        satisfied_count = 0  # the number of combinations that are satisfiable

        for sent1 in self.inference_scratch_pad:

            for sent2 in self.inference_scratch_pad:
                if sent1 != sent2:
                    # if they are not equal, resolve and add at the end
                    result = Resolver.resolve(sent1, sent2)
                    if type(result) is list:
                        # either [] <- contradiction
                        # or [....] <- not a contradiction
                        if len(result) == 0:
                            # contradiction
                            return True
                        else:
                            # longer than 0, meaning that it is a result
                            conclusions.append(result)
                    else:
                        # type must be false
                        # does not resolve
                        satisfied_count += 1

        # add conclusions to the scratchpad
        if len(conclusions) > 0:
            self.inference_scratch_pad.extend(conclusions)

        self.display_progress()

        # clear all the inference scratch work
        del self.inference_scratch_pad[:]
        return False

    def clear(self):
        """
        
        :return: 
        """
        del self.knowledge_base[:]

    # HELPER FUNCTIONS

    def summation(self, num):
        """
        
        :param num: 
        :return: 
        """
        if int(num) == 0:
            return 0
        else:
            return num + self.summation(num-1)

    def is_cnf_sentence(self, sentence):
        """
        Determine if the given sentence is in a valid CNF form or not
        
        :param sentence: 
        :return: 
        """
        pass

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