"""
Resolution.py

Alexander S. Adranly

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


def literal_mark(index, sentence, literal_dict, invert_flag=False):
    """
    Iterates through the sentence and marks all the literals    
    
    :param index: 
    :param sentence: 
    :param literal_dict: 
    :param invert_flag:
    :return: 
    """
    if index >= len(sentence):
        # dictionary is marked and ready to go
        return
    else:
        flag = invert_flag
        if type(sentence[index]) == list:
            literal_mark(0, sentence[index], literal_dict, invert_flag)
        else:
            if sentence[index] == 'not':
                flag = not invert_flag
            else:
                mark(sentence[index], literal_dict, invert_flag)
                # if the invert flag is on, it will be turned off now
                flag = False

        literal_mark(index + 1, sentence, literal_dict, flag)


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
    literal_list = {}

    literal_mark(0, sentence_1, literal_list, False)
    literal_mark(0, sentence_2, literal_list, False)

    # CHECK NUMBER OF LITERALS THAT ARE RESOLVABLE
    literals_to_resolve = []
    for key in literal_list.keys():
        if literal_list[key] == 0:
            literals_to_resolve.append(key)

    # RESOLVABLE CHECK
    if len(literals_to_resolve) != 1:
        # there has to be only one instance to resolve
        # otherwise it will not five us useful information
        # or .. it actually just has nothing to resolve against
        return False

    # CONTRADICTION CHECK
    # filter out all key words from the list of keys
    literal_filter = [x for x in literal_list.keys() if x not in KEY_WORDS]

    if len(literal_filter) == 1:
        # if there is only one literal here
        # then there must have been only one type of literal
        # if that literal has a count of zero
        # there is a contradiction
        return []

    # TRY RESOLVING SENTENCES AGAINST EACH OTHER
    literal_to_resolve = literals_to_resolve[0]

    # remove the literal from each sentence
    # combine the two sentences together
    lit_to_remove = None
    for item in sentence_1:
        if item == literal_to_resolve:
            lit_to_remove = item
        if type(item) == list:
            if item[0] == 'not':
                if item[1] == literal_to_resolve:
                    lit_to_remove = item
    else:
        sentence_1.remove(lit_to_remove)

    for item in sentence_2:
        if item == literal_to_resolve:
            lit_to_remove = item
        if type(item) == list:
            if item[0] == 'not':
                if item[1] == literal_to_resolve:
                    lit_to_remove = item
    else:
        sentence_2.remove(lit_to_remove)

    # get rid of the first or's
    for keyword in KEY_WORDS:
        try:
            sentence_1.remove(keyword)
        except ValueError:
            pass

        try:
            sentence_2.remove(keyword)
        except ValueError:
            pass

    # stitch together both sentences
    if len(sentence_1) + len(sentence_2) > 1:
        resolvent.append('or')

    for item in sentence_1:
        if item not in resolvent:
            if type(item) is list:
                resolvent.extend(item)
            else:
                resolvent.append(item)

    for item in sentence_2:
        if item not in resolvent:
            if type(item) is list:
                resolvent.extend(item)
            else:
                resolvent.append(item)

    return resolvent


# TESTING
if __name__ == '__main__':
    # sent1 = ['or', 'a', 'b', 'c']
    # sent2 = ['or', ['not', 'b']]
    #
    # sent1 = ['or', 'a', 'b', 'c']
    # sent2 = ['or', 'b', ['not', 'c']]

    # sent1 = ['or', ['not', 'raining'], 'wet ground']
    # sent2 = ['raining']

    # sent1 = ['or', 'a', 'b']
    # sent2 = ['c']

    # sent1 = ['a']
    # sent2 = ['not', 'a']

    sent1 = ['or', 'alex is happy', 'alex is stressed']
    sent2 = ['not', 'alex is happy']

    print resolve(sentence_1=sent1, sentence_2=sent2)
