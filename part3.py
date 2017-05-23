"""
FILE:   CNF Conversion

AUTHOR: Alexander S. Adranly

A group of functions that help convert any type of propositional logic into CNF form

CNF -Conjunctive Normal Form-
: a conjunction of disjunctions -aka- and AND of ORs
: 

CONVERTING TO CNF
1. Biconditional Elimination
2. Implication Elimination
3. Move negation inwards (double-negation elimination, DeMorgan)
4. Distributivity ( v over ^ )

"""
import part2 as inference

KEY_WORDS = ['not', 'and', 'or', 'implies', 'biconditional']


def __to_cnf__(sentence):
    """
    STAGE:
    1. biconditional elimination
    2. implication elimination
    
    :param sentence: 
    :return: 
    """
    result = []
    # Biconditional Elimination
    result = __search_and_convert__(sentence, __biconditional_elimination__)

    # Implication Elimination
    result = __search_and_convert__(result, __implication_elimination__)

    # Move negation inwards (double-negation elimination, DeMorgan)
    # handled in my __not__ function in part2

    # Distributivity ( v over ^ )
    result = __search_and_convert__(result, __distributivity__)

    return result


def __search_and_convert__(sentence, fxn):
    """
    
    :param sentence: 
    :param result:
    :param function:
    :return: 
    """
    for i in range(0, len(sentence)):
        if type(sentence[i]) is list:
            value = __search_and_convert__(sentence[i], fxn)
            sentence[i] = value if value is not None else sentence[i]

    return fxn(sentence)


def __implication_elimination__(sentence):
    """
    A -> B = !A v B
    assuming implies was written correctly
    :param sentence: 
    :return: 
    """
    if sentence[0] == 'implies':
        result = ['or', inference.__not__(sentence[1]), sentence[2]]
        return result
    return sentence


def __biconditional_elimination__(sentence):
    """
    A <-> B = ((A -> B) ^ (B -> A))
    
    :param sentence: 
    :return: 
    """
    if sentence[0] == 'biconditional':
        result = ['and', ['implies', sentence[1], sentence[2]], ['implies', sentence[2], sentence[1]]]
        return result
    return sentence


def __double_negation_elimination__(sentence):
    """
    !(!A) = A
    
    :param sentence:
    :return: 
    """
    sent = sentence if type(sentence) is list else list(sentence)
    assert(len(sentence) == 2 and sentence[0] == 'not' and sentence[1][0] == 'not')

    result = inference.__not__(sentence[1])
    return result


def __demorgan__(sentence):
    """
    !(A ^ B) = !A v !B
    !(A v B) = !A ^ !B
    
    :param sentence: 
    :return: 
    """
    sent = sentence if type(sentence) is list else list(sentence)
    assert(len(sent) > 1 and sent[0] == 'not' and type(sent[1]) is list)

    result = ['and'] if sent[1][0] == 'or' else ['or']

    for item in sent[1][1:]:
        result.append(inference.__not__(item))

    return result


def __distributivity__(sentence):
    """
    A ^ (B V C) = (A ^ B) v (A ^ C)
    A v (B ^ C) = (A v B) ^ (A v C)
    
    note:
    (A ^ B) ^ (B v C) ?? Does this work??
    
    :param sentence: 
    :return: 
    """
    if len(sentence) == 3:
        groups = [x for x in sentence if type(x) is list and (x[0] == 'and' or x[0] == 'or')]
        literal = [x for x in sentence if type(x) is str and x not in KEY_WORDS]
        logic = sentence[0]

        if len(groups) == 0 and len(literal) == 0:
            return sentence

        elif len(groups) == 0 and len(literal) == 1:
            return sentence

        elif len(groups) == 1 and len(literal) == 0:
            return sentence

        elif len(literal) == 1:
            # groups must be one
            result = [groups[0][0], [logic, literal[0], groups[0][1]], [logic, literal[0], groups[0][2]]]

        else:
            # groups are two
            result = [groups[0][0], [logic, groups[0], groups[1][1]], [logic, groups[0], groups[1][2]]]

        return result

    return sentence
