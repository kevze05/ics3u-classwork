# functional deocmposition

Note: I included the software/app within the actual fixing/preventing the problem.

## vending machine from the machine's perspective

- wait while (no buttons are pressed and no money is inserted)
- loop 
	- if money inserted
		- scan money and determine value
		- add value to total 
		- display current total
	- if button pressed
		- scan input button
		- if button is positional (letter/number)
			- if invalid
				- delete all values
				- display invalid location
				- go back to wait
			- else
				- store position
		- if button is x
			- delete all values
			- go back to wait
		- if button is ok
			- check if sum > cost[position]
			- if true
				- unlock item[position]
				- dispense item[position]
				- go back to wait
			- else
				- display insufficient funds
				- go back to wait

Some of the basic programming concepts used:
- loop is used to continuously read inputs until the user obtains their product or makes an invalid selection
- if/else branching conditionals to check whether conditions have been met (e.g sufficient funds, valid position, user input) and execute code accodringly
- nested structure: branches inside loops

## Cookie does not fit into glass

Fixing: to fix the problem, you need to figure out the diameter of the glass, as well as the diameter of the cookie. Then, you know how to split the cookie so that the diameter of the smaller parts fit within the diameter of the cup.

- scan cookie diameter 
- scan cup diameter 
- if cup diameter > cookie diameter by (predefined margin of error)
	- display no problem
- else
	- display need cup with at least (cookie diameter+predefined margin of error)
	- display OR
	- display split cookie into pieces of width (cup diameter-margin of error)

Prevention: To prevent the problem, you need to know beforehand the average diameter of cookies of a certain brand and type. Then you can use a cup with a bigger diameter (by a certain margin of error) to ensure that you can dunk your cookie. 

- scan cookie package
- find avg cookie diameter of this brand+package from stored data
- display avg diameter of cookie = (avg diameter)
- dispplay cup size needed: (avg diameter + predefined margin of error)

##
