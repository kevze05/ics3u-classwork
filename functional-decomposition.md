# functional deocmposition

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

Fixing: To fix the problem, you need to figure out the diameter of the glass, as well as the diameter of the cookie. Then, you know how to split the cookie so that the diameter of the smaller parts fit within the diameter of the cup.

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

## People who can't park

Fixing: To fix the problem, you can send an alert if someone's car is parked improperly, and if no one answers the alert, tow the car. To check if someone is parked improperly, you can install sensors in the gridlines, and if too much of the sensors is covered for too long, that means someone has parked improperly. 
		
Prevention: To prevent the problem, you can simply implement the function for fixing immediately after a car has parked.

- if sensors become covered for 30 seconds //fair amount of time, don't want to trigger everytime someone accidently crosses a line
	- trigger fix 

fix()
- loop
	- wait (predefined x) amount of time //this is so that you don't waste power by checking every second
	- check sensors
	- if covered amount > (predefined threshold)
		- trigger alert
		- scan car model, colour and license plate.
		- broadcast alert warning for a (colour) car of (model) with (license plate)
		- wait (predefined y amount of time) // give them time to fix their parking
		- if covered amount > (predefined threshold) // if true they still didn't respond
		- tow_the_car() // call function - I didn't implement it though
	
## People hogging seats with bags/sitting where they're not supposed to

Fixing: To fix the problem, set a scanner on the seat to look for a certain barcode on a ticket. If there is weight on the seat but no scan, it means someone is illegally using the seat. 

Prevention: To prevent the problem, you can preset the seats to be "down" until someone scans the proper ticket. 

- define flag as false for each seat
- loop 
	- if scanner reads barcode
		- if correct barcode
			- set flag to true
			- display valid code
			- engage seat supports if not already up 
		- else
			- display incorrect code
	- wait (predefined x) amount of time //this is so that you don't waste power by checking every second
	- check seat weight and flag
	- if seat weight true (someone/something is occupying seat)
		- if flag true
			- do nothing (paid)
			- do not check this seat until flag becomes false again
		- if flag false
			- trigger warning
			- display seat stealer
			- wait (predefined y) amount of time //fair warning
			- drop seat supports
	- else
		- do nothing //no one is sitting 
	- if time up or trip finished
		- set flag to false
		- drop seat supports (prevention, not necessary)
		
