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


def __to_cnf__(sentence, result, stage):
    """
    STAGE:
    1. biconditional elimination
    2. implication elimination
    
    :param sentence: 
    :return: 
    """
    # Biconditional Elimination

    # Implication Elimination

    # Move negation inwards (double-negation elimination, DeMorgan)

    # Distributivity ( v over ^ )
    pass


def __search_and_convert__(sentence, function):
    """
    
    :param sentence: 
    :param function: 
    :return: 
    """
    pass

def __implication_elimination__(sentence):
    """
    A -> B = !A v B
    
    :param sentence: 
    :return: 
    """
    assert(sentence[0] == 'implies')
    assert(len(sentence) == 3)
    result = ['or', inference.__not__(sentence[1]), sentence[2]]
    return result


def __biconditional_elimination__(sentence):
    """
    A <-> B = ((A -> B) ^ (B -> A))
    
    :param sentence: 
    :return: 
    """
    assert(sentence[0] == 'biconditional')
    assert(len(sentence) == 3)

    result = ['and', ['implies', sentence[1], sentence[2]], ['implies', sentence[2], sentence[1]]]
    return result

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
    
    :param sentence: 
    :return: 
    """
    assert (len(sentence) == 3)
    group = sentence[1] if type(sentence[1]) is list else sentence[2]
    literal = sentence[1] if type(sentence[1]) is str else sentence[2]
    logic = sentence[0]

    result = [group[0], [logic, literal, group[1]], [logic, literal, group[2]]]

    return result
