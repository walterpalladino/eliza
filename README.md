# Eliza Python implementation
#### Video Demo:  https://youtu.be/8SRySozR49M

#### Description:
This is a Python implementation of one of the most know chatbots.

I first played with Eliza en a C64 many years ago and coded on C and later CPP and Java but to be honest, Python is really powerful to handle data make things easier.

In the docs folder there are other implementations as reference so it is possible to compare how much you get using the right tool for the right job.


#### References

This are some references to Eliza history and some implementations.

https://en.wikipedia.org/wiki/ELIZA
https://everything2.com/title/ELIZA+source+code+in+BASIC
http://www.vintagecomputer.net/commodore/64/TOK64/ELIZA.txt
https://github.com/dettore/eliza/blob/master/eliza.py
https://github.com/jeffshrager/elizagen.org

## The CS50 Final Project

Being this the deliverable for the Final Project, lets complete the requirements:

### What will your software do? What features will it have? How will it be executed?

This is an implementation of the Eliza chatbot. It simulates the interaction with a psychoanalyst so, the bot do questions and you will answer.

The bot will try to identify keywords on your input to create a contextual dialogue.
To execute it be sure you have a valid Python installation on your computer and run:

`python eliza.py`

or

`python3 eliza.py`

depending on how you configured your environment on the root folder.


### What new skills will you need to acquire? What topics will you need to research?

I never coded much on Python and the main challenge was to identify the language features to allow me a cleaner implementation.
So it was required to research about other Eliza implementations and lot about Python and how to use for the best the tools at hand specially for creating and manipulation data structures. Lists, Dictionaries, Strings and how to manipulate them.




### If working with one or two classmates, who will do what?

Just me.


### In the world of software, most everything takes longer to implement than you expect. And so it’s not uncommon to accomplish less in a fixed amount of time than you hope. What might you consider to be a good outcome for your project? A better outcome? The best outcome?

I needed to work on a tight schedule so I needed to balance the scope of the deliverable.



### Sample run

~~~~
*** ELIZA / DOCTOR ***
CREATED BY JOSEPH WEIZENBAUM
This Python version was ported by Walter Palladino
On December 2022 inspired on several implementations on BASICs, C and Python

You can stop the program using words like BYE, SHUT UP or just Ctrl + C :)

HI! I'M ELIZA. WHAT'S YOUR PROBLEM?

< I'M AFRAID OF THE DARK
> DO YOU BELIEVE IT IS NORMAL TO BE AFRAID OF THE DARK?
< NO, I DON'T THINK SO
> DOES THAT TROUBLE YOU?
< YES, THATS TROUBLE ME A LOT
> ARE YOU SURE?
< COMPLETELY     
> SAY, DO YOU HAVE ANY PSYCHOLOGICAL PROBLEMS?
< A LOT, I WROTE THIS COMPUTER PROGRAM AND IT IS DRIVING ME CRAZY
> HOW DO YOU DO .,. PLEASE STATE YOUR PROBLEM.
< COMPUTER
> ARE YOU TALKING ABOUT ME IN PARTICULAR?
~~~~





### Still curious?

Ok. Let me explain a bit more in detail the implementation.
There are two big groups: Data and logic.

#### Data
Data includes a dictionary of keywords that Eliza will try to identify in the user input.
Based on that will choose one reply from the available related list.

The other set of data include words used to create a more natural dialog by swapping some verbs and prepositions between first and third person.


#### Logic
There are three steps: Get the user Input, Generate a reply and Output tje reply.

In the first part we get the user input and cleaning some characters to make easier the next step.

In the second part of the process, we try to identify a valid keyword in the input. If it is not possible then a generic reply will be selected.
After that based on the reply some will require some composition to again create e more natural interaction and from the original input some words will be swapped from our swap list like verbs and prepositions.

The last and final step will print in a fancy way the generated reply to simulate keyboard typing.
