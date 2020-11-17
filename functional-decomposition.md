# functional deocmposition

## vending machine from the machine's perspective

-wait while (no buttons are pressed and no money is inserted)
-loop 
	-if money inserted
		-scan money and determine value
		-add value to total 
		-display current total
	-if button pressed
		-scan input button
		-if button is positional (letter/number)
			-store position
		-if button is x
			-delete all values
			-restart loop
		-if button is ok
			-check if sum > cost[position]
			-if true
				-unlock item[position]
				-dispense item[position]
			-else
				-display insufficient funds
				-continue
				
		
