concept in view: import & modules

explanation:
Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter.
 Such a file is called a module; definitions from a module can be imported into other modules or into the main module
(the collection of variables that you have access to in a script executed at the top level and in calculator mode).

A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py
 appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__.
For instance, use your favorite text editor to create a file called fibo.py in the current directory with the following contents: 

0-add.py - a program that imports the function def add(a, b): from the file add_0.py and prints
the result of the addition 1 + 2 = 3

1-calculation.py - a program that imports functions from the file calculator_1.py, does some Maths,
		 and prints the result
2-args.py - a program that prints the number of and the list of its arguments.

3-infinite_add.py -  a program that prints the result of the addition of all arguments 

4-hidden_discovery.py -  a program that prints all the names defined by the compiled module
			 hidden_4.pyc (please download it locally)

5-variable_load.py - a program that imports the variable a from the file variable_load_5.py and
		     prints its value.
100-my_calculator.py - a program that imports all functions from the file calculator_1.py and
		       handles basic operations.
101-easy_print.py - a program that prints #pythoniscool, followed by a new line, in the standard output.

102-magic_calculation.py - the Python function def magic_calculation(a, b): that does exactly the same as the Python bytecode given

103-fast_alphabet.py -  a program that prints the alphabet in uppercase, followed by a new line
