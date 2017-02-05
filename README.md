# CYK-Parser

This is a simple context-free grammar parser written in Python 3.
It includes a converter to bring a context-free grammar in chomsky normal form. It can't handle epsilon productions.
For the actual parsing the Cocke-Younger-Kasamai algorithm is used.

#

The code isn't by any means perfect and isn't supposed to.
**Feel free to use any piece of the code in your own projects.**

# Usage

To run the parser **Python 3.6** needs to be installed. There are two ways of running the parser: with or
without arguments. The File "GrammarConverter.py" needs to be either in the same directory or within a directory, in which
Python looks for modules to include. The program can be run as a module (`python3 -m Parser`), when
in the same directory, or as a normal python program.

`python3 Parser.py /home/Users/god/grammar.txt /home/Users/god/sentences/pajamas.txt`

> Using /home/Users/god/grammar.txt as path for the grammar and /home/Users/god/sentences/pajamas.txt
as path for the sentence.

Additionally the parser be called directly with the grammar in string representation and/or the sentence in string representation.

When the sentence is contained in the grammar, the parser will output the parsed tree in a
non-graphical string format.

`python3 Parser.py grammar.txt "I shot an elephant in my pajamas"`  
> Using grammar.txt as path for the grammar and sentence.txt as path for the sentence.  
The given sentence is contained in the language produced by the given grammar!

> Possible parse(s):  
[S [NP 'I'][VP [V 'shot'][NP [NP0 [Det 'an'][N 'elephant']][PP [P 'in'][NP [Det 'my'][N 'pajamas']]]]]]  
[S [NP 'I'][VP [VP [V 'shot'][NP [Det 'an'][N 'elephant']]][PP [P 'in'][NP [Det 'my'][N 'pajamas']]]]]

When the sentence is not contained in the grammar, the parser won't print out a tree.

`python3 Parser.py some_grammar.txt sentence.txt`

> Using some_grammar.txt as path for the grammar and sentence.txt as path for the sentence.  
The given sentence is not contained in the language produced by the given grammar!

# Example input
An example for a simple grammar is given below. Just paste it in an text file and run the parser with it and an input sentence file (it is assumed, that the whole input sentence is in the first line of that file).  

S -> NP VP  
PP -> P NP  
NP -> Det N  
NP -> Det N PP  
NP -> 'I'  
VP -> V NP  
VP -> VP PP  
Det -> 'an'  
Det -> 'my'  
N -> 'elephant'  
N -> 'pajamas'  
V -> 'shot'  
P -> 'in'  

