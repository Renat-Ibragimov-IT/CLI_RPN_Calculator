# CLI_RPN_Calculator
Test task for creation the simple command-line reverse polish notation 
(CLI RPN) Calculator.

In reverse Polish notation, the operators follow their operands; 
for instance, to add 3 and 4 together, one would write 3 4 + rather than 3 + 4.
If there are multiple operations, operators are given immediately after their 
final operands (often an operator takes two operands, in which case the 
operator is written after the second operand); so the expression written 
3 − 4 + 5 in conventional notation would be written 3 4 − 5 + in reverse 
Polish notation: 4 is first subtracted from 3, then 5 is added to it. 
An advantage of reverse Polish notation is that it removes the need for 
parentheses that are required by infix notation. While 3 − 4 × 5 can also be 
written 3 − (4 × 5), that means something quite different from (3 − 4) × 5. 
In reverse Polish notation, the former could be written 3 4 5 × −, which 
unambiguously means 3 (4 5 ×) − which reduces to 3 20 − (which can further be
reduced to -17); the latter could be written 3 4 − 5 × (or 5 3 4 − ×, 
if keeping similar formatting), which unambiguously means (3 4 −) 5 ×.

# Explanation

In order to run CLI RPN calculator You can use command 
"python3 cli_rpn_calculator.py". After receiving a message: 
"Please enter Your expression: ", You can enter Your expression like "1 2 3 + -".
This program has an option to save results of previous calculations and inputs,
so You can enter Your expression separately like: Input: 5, Output: 5.0;
Input: 3, Output: 5.0, 3.0; Input: +, Output: 8.0. 
To end the program execution You can use the "q" command or an end of input 
indicator (EOF, CtrlD for Linux and MacOS or CtrlX for Windows).

# Details

I used lambda functions to create this calculator in order to be able to expand 
its functionality in the future by adding additional operators. In this case, 
minor code changes will be required. Also, I used exceptions to be able to test 
it and add new one if required.
Program tested with unittest. Coverage: 89% (checked with nosetests).