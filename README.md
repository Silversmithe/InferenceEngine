# InferenceEngine
HW #2: Building an Inference Engine

###Overview
For this homework assignment, you will be implementing a propositional logic resolution-based inference engine. There 
are 3 distinct parts, and you are free to complete as much as you are confortable with, but please do not start a later
portion without completing all earlier ones.

##Part 1: Two-Statement Resolution (70 points)
For this part of the assignment, you will be implementing a simple resolution function that resolves two sentences that 
are already in CNF.

###Syntax
We'll use lists to represent sentences in propositional logic form. Each list will be represented as prefix operators
followed by operands. Operators and operands will both be represented by Python strings.
    
| **Boolean Operator** | **Python Representation** | **# of Operands** |
|----------------------|---------------------------|-------------------|
|          ¬           |            "not"          |        1          |
|          ^           |            "and"          |        ≥2         |
|          v           |            "or"           |        ≥2         |
|         -->          |            "implies"      |        2          |
|         <-->         |            "biconditional |        2          |

Here are some examples of boolean expressions and their Python representations

> IsRaining :: "IsRaining"

> Studying --> GoodGrades :: ["implies", "Studying", "GoodGrades"]

> (a v b) <--> ¬ (c ^ ¬d) :: ["biconditional", ["or", "a", "b"], ["not", ["and", "c", ["not", "d"]]]]

###API

Implement a single function:

> *resolve* Accepts two arguments, both sentences in CNF. Returns:
> * The resolution if the sentences can resolve against each other
> * An empty list if the sentences resolve to a contradiction
> * False if the two sentences cannot resolve

###Demo

> \>>> print resolve(["or", "a", "b", "c"], ["or", ["not", "b"]])

> ['or', 'a', 'c']

> \>>> print resolve(["or", "a", "b", "c"], ["or", "b" ["not", "c"]])

> ['or', 'a', 'b']

> \>>> print resolve(["or", ["not", "raining"], "wet ground"], ["raining"])

> 'wet ground'

> \>>> print resolve(["or", "a", "b"], "c")

> False

> print resolve("a", ["not", "a"])

> []

##Part 2: Resolution Inference Engine
