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

##Part 2: Resolution Inference Engine (20 points)
For this part of the assignment, you'll implement a complete resolution inference engine. It should accept CNF sentences
in the same form as part 1 of this assignment, and answer queries by following the resolution algorithm. As a reminder, 
that means introducing the negation of the query and resolving until determining that the KB with inclusion of the query 
is either satisfiable (no new resolutions are possible) or contradictory.

###API
Implement the following functions:

>TELL :: accepts one argument, a sentence in CNF. Adds that sentence to the KB

>ASK :: accepts one argument, a singe proposition or negated proposition. Returns True (indicating that the query must be True)
>, of False (indicating that it cannot determine if the query is true)

>CLEAR :: Removes all sentences from the KB

###Demo
> \>>> TELL(['or', ['not', 'a'], 'b'])
>
> \>>> TELL(['or', ['not', 'b'], 'c'])
>
> \>>> TELL('a')
>
>\>>> ASK('c')
>True
>\>>> ASK('d')
>False

##Part 3: CNF Conversion (20 points)
For this part of the assignment, you'll augment your API's to allow sentences using the full set of propositional logic 
operators, so you will have to implement the routines to convert expressions to CNF. After this is implemented, both the 
TELL and ASK functions should allow the specification of arbitrary expressions in the full propositional logic syntax.
The values returned from ASK should not change, however.

###Demo
\>>> TELL(['implies', 'a', 'b'])

\>>> TELL(['implies', 'b', 'c'])

\>>> TELL('a')

True

\>>> ASK('d')

False

\>>> ASK(['implies', 'c', 'a'])

True

\>>> ASK(['implies', 'd', 'a'])

True

###Testing
In order to facilitate automated testing, all tests that you provide should be using the naming pattern:





