# CYK-Parser

This is a simple context-free grammar parser written in Python 3.
It includes a converter to transform a context-free grammar to chomsky normal form. The converter can't handle epsilon productions, though. For the actual parsing the Cocke-Younger-Kasamai algorithm is used.

#

The code isn't by any means perfect and isn't supposed to.
**Feel free to use any piece of the code in your own projects.**

# Usage
### As a standalone program
To run the parser **Python 3.6** needs to be installed. The file "GrammarConverter.py" needs to be either in the same directory or within a directory, in which Python looks for modules to include. The program can be run as a module (`python3 -m Parser`), when
in the same directory, or as a normal python script. If the parser is run as a standalone program it expects two arguments. The first one is a file containing the grammar (see below for an example) and the second one a file containing the input sentence.

`python3 cyk_parser.py /home/Users/god/grammar.txt /home/Users/god/sentences/pajamas.txt`

> Using /home/Users/god/grammar.txt as path for the grammar and /home/Users/god/sentences/pajamas.txt
as path for the sentence.

When the sentence is contained in the language produced by the grammar, the parser will output the parsed tree in a non-graphical string format.

`python3 cyk_parser.py grammar.txt "I shot an elephant in my pajamas"`  
> Using grammar.txt as path for the grammar and sentence.txt as path for the sentence.  
The given sentence is contained in the language produced by the given grammar!

> Possible parse(s):  
[S [NP 'I'][VP [V 'shot'][NP [NP0 [Det 'an'][N 'elephant']][PP [P 'in'][NP [Det 'my'][N 'pajamas']]]]]]  
[S [NP 'I'][VP [VP [V 'shot'][NP [Det 'an'][N 'elephant']]][PP [P 'in'][NP [Det 'my'][N 'pajamas']]]]]

When the sentence is not contained in the grammar, the parser won't print out a tree.

`python3 cyk_parser.py some_grammar.txt sentence.txt`

> Using some_grammar.txt as path for the grammar and sentence.txt as path for the sentence.  
The given sentence is not contained in the language produced by the given grammar!

### As imported module
Alternatively the parser can be imported into other python scripts. The constructor expects a grammar which will be converted to CNF, so any CFG is fine, and some input to parse. Both of the arguments can either be file paths or just a string. Parser objects are callable and expect new input which by default just will be stored in the object and not directly parsed.

# Example input
An example for a simple grammar is given below. Just paste it in a text file and run the parser with it and an input sentence file (it is assumed, that the whole input sentence is in the first line of that file) or pass it as a string to the parser.  

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

