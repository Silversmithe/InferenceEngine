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
        self.knowledge_base = list()
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

        # keep on resolving until satisfiable ( no new resolutions are possible)
        # or there is a contradiction
        pass

    def clear(self):
        """
        
        :return: 
        """
        del self.knowledge_base[:]

    # HELPER FUNCTIONS
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