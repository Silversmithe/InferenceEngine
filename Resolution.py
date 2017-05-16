"""
FILE:   Resolution.py

AUTHOR: Alexander S. Adranly

A simple resolution function that resolves two sentences that are already in CNF - Conjunctive Normal Form-

CNF -Conjunctive Normal Form-
: a conjunction of disjunctions -aka- and AND of ORs
: 

"""
KEY_WORDS = ['not', 'and', 'or', 'implies', 'biconditional']


# HELPER FUNCTIONS
def mark(literal, dictionary, inv=False):
    # put value in literal list
    score = -1 if inv is True else 1

    if literal in dictionary:
        # then all we have to do is increment or decrement
        dictionary[literal] += score
    else:
        # otherwise we have to add it to the list
        dictionary[literal] = score


def count(sentence, dictionary, invert_flag=False):
    """
    :param sentence: 
    :param dictionary: 
    :param invert_flag: 
    :return: 
    """
    if len(sentence) == 0:
        # dictionary is marked and ready to go
        return
    else:
        flag = invert_flag
        if type(sentence[0]) == list:
            count(sentence[0], dictionary, invert_flag)
        else:
            if sentence[0] == 'not':
                flag = not invert_flag
            else:
                mark(sentence[0], dictionary, invert_flag)
                # if the invert flag is on, it will be turned off now
                flag = False

        count(sentence[1:], dictionary, flag)


# RESOLVE FUNCTION
def resolve(sentence_1, sentence_2):
    """

    NOTE: 
    - under the impression that the sentences coming in are correct and in CNF form
    - assume CNF form has no repetition of values
        ex:
        [ ... , 'b', ... ] [ ..., 'b', ...]

    :param sentence_1: [ str, str, ... ] : first sentence to resolve against
    :param sentence_2: [ str, str, ... ] : second sentence to resolve against the first sentence
    :return: 
    : [ str, str, ... ] : the resolution if the sentences can resolve against each other
    : [ ] : an empty list if the sentences resolve to a contradiction
    : False : if the two sentences cannot resolve
    """
    print "resolving ", sentence_1, " and ", sentence_2

    resolvent = []  # clause produced by a resolution rule

    # CHECK IF TWO SENTENCES CANNOT RESOLVE
    # not val = -1
    # val = 1
    # store the count in a dictionary
    literal_count = {}

    # convert into lists if not lists
    sent1 = list(sentence_1) if type(sentence_1) is not list else sentence_1
    sent2 = list(sentence_2) if type(sentence_2) is not list else sentence_2

    count(sentence=sent1, dictionary=literal_count)
    count(sentence=sent2, dictionary=literal_count)

    literal_to_resolve = [x for x in literal_count.keys() if literal_count[x] == 0]

    if len(literal_count.keys()) == 0 and literal_to_resolve is not None:
        # if there is only one literal counted
        # if the literal to resolve is not empty
        # !!! Contradiction !!!
        return []
    elif len(literal_to_resolve) != 1:
        # if there are multiple literals to resolve
        # or no literals to resolve
        # then these two sentences cannot resolve !!!
        return False
    else:
        # resolve the values
        # remove the resolved value from the NOT section
        inner_list1 = [x for x in sent1 if type(x) is list and x[0] == 'not' and x[1] != literal_to_resolve[0]]
        inner_list2 = [x for x in sent2 if type(x) is list and x[0] == 'not' and x[1] != literal_to_resolve[0] and x not in inner_list1]

        # filter out all literals that are not negated
        filtered_sent1 = [x for x in sent1 if type(x) is not list and x != literal_to_resolve[0] and x not in KEY_WORDS]
        filtered_sent2 = [x for x in sent2 if type(x) is not list and x != literal_to_resolve[0] and x not in KEY_WORDS and x not in filtered_sent1]

        if len(filtered_sent1) != 0:
            resolvent.extend(list(filtered_sent1))

        if len(filtered_sent2) != 0:
            resolvent.extend(list(filtered_sent2))

        if len(inner_list1) != 0:
            resolvent.extend(list(inner_list1))

        if len(inner_list2) != 0:
            resolvent.extend(list(inner_list2))

        if len(resolvent) > 1:
            resolvent.insert(0, 'or')

        print resolvent
        return resolvent


# TESTING
if __name__ == '__main__':
    sent1 = ['or', 'a', 'b', 'c']
    sent2 = ['not', 'b']

    # sent1 = ['or', 'a', 'b', 'c']
    # sent2 = ['or', 'b', ['not', 'c']]

    # sent1 = ['or', ['not', 'raining'], 'wet ground']
    # sent2 = ['raining']
    #
    # sent1 = ['or', 'a', 'b']
    # sent2 = ['c']

    # sent1 = ['a']
    # sent2 = ['not', 'a']

    # sent1 = ['or', 'alex is happy', 'alex is stressed']
    # sent2 = ['not', 'alex is happy']

    print resolve(sentence_1=sent1, sentence_2=sent2)
