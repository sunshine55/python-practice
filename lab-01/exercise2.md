# LAB-01: EXTRA BASICS #
## Objectives ##
- String and String operations
- Data operations on structured data types
- Modules and built-in functions:
	+ argparse
	+ sys, os
	+ file

## Content ##
Tax calculator. Given a list of ordered items, tax calculator will show the amount of tax and total due  
	
- Screen #1: System prompts user for an item's price and quantity
	
		ORDERED ITEM DETAILS
		(Enter blank to start calculation)
		Item price: 	30
		Quantity [1]:	2
		Tax [10%]:		_
	System continues to show this screen until user enters a blank value for `Item price`. When user enters a non-blank valid value for `Item price`, prompts for `Quantity` and `Tax` must now appear.
		
	Default value in the square brackets is applied when a blank is entered for `Quantity` and `Tax` 

	User can only enter whole number for `Quantity`. For example: 1, 2, 3, 10, 30 but not 1.5, 2.3, 3.14159

	User can enter a `Tax` value using either percentage notation or decimal notation. For example:
		
		Tax [10%]:		5%

	OR

		Tax [10%]:		0.05

	If user enters an invalid value for `Item price` or `Quantity` or `Tax`, system continues to prompt user to re-enter until a valid value is entered.

- Screen #2: System lists the previously entered information in a grid grouped by tax rate. System displays the total due, tax due for each group and for the whole order
			
		ORDER DETAILS - CURRENCY: VND
		#	PRICE		Qty		Subtotal
				----- Tax: 05% -----
		1	15.000		2		30.000
		2	25.000		2		50.000
					Subtotal:	80.000
					Tax:		 4.000
				----- Tax: 10% -----
		3	155.000		2	   310.000
		4	500.000		2	 1.000.000
					Subtotal:1.310.000
					Tax:	   131.000
		==================================
		TOTAL without tax:	 1.390.000 VND
		TAX total		 :	   135.000 VND
		TOTAL plus tax   :	 1.525.000 VND

	When the currency is US dollar or British pound, the displayed currency must correspond and the number of decimal digits must be two.
		
		ORDER DETAILS - CURRENCY: USD
		#	PRICE		Qty		Subtotal
				----- Tax: 05% -----
		1	 5.39		2			10.78
		2	31.59		2			63.18
					Subtotal:		73.96
					Tax:		 	 3.70
				----- Tax: 10% -----
		3	55.99		2	   	   111.98
		4  361.15		2	 	   722.30
					Subtotal:	   834.28
					Tax:	   	    83.42
		==================================
		TOTAL without tax:	 	   908.24 USD 
		TAX due	 		 :	   		87.12 USD
		GRAND TOTAL		 :	 	   995.36 USD

- Screen #3: System prompts user whether or not to print the tax calculation

		Would you like to save the tax calculation? (Y/n)
	
	If user specifies Y or YES (case-insensitive), system prompts: 

		Where would you like to save the tax calculation?
		File location: D:\tax\output\reports\gifts.txt_

	The system **must** ensure that the file path points to an accessible file. If the file is not accessible, reports the error:

		Error: THIS IS THE REASON WHY YOU CANNOT ACCESS [FILE] 
			
	and continues to prompt `File location: _` until the file path points to an accessible file or user issues a `Ctrl + C` 

	When the file path is accessible, display the following message so that user may know the system has successfully opened the file:

		Tax calculation file has been successfully written

	System terminates normally after **Screen #3**

### Options
Tax calculator allows the following options to alter the appearance or the behavior. Options are to be specified using Unix style.
		
	python taxc.py [-t TAX] [-c CURRENCY] [-r rounding]
	
- -t/-tax: overrides the system's default tax rate of 10% 
- -c/--currency: Default to be `VND`. Specifies the display currency symbol. Supported symbols are US dollar, British pound, Euro and Vietnam Dong. Vietnam Dong supports only 2 digits of precision; the other three support 2 digits of precision
- -r/--rounding: Default to be `Even`. Specifies how decimals should be rounded. Supports two methods of rounding:
	+ Away from zero: numbers will be rounded to the nearest value away from zero having the number of decimal places. For example:
		
			# Division with all the decimal places
			a. 30 / 31 = 0.96774193548
			b. 28 / 31 = 0.90322580645
			# Round to the nearest two decimal digit number away from zero
			a. 0.96774193548 => 0.97
			b. 0.90322580645 => 0.91

	+ Even: numbers will be rounded to the nearest value having an even number as the least significant digit. For example:
		
			# Division with all the decimal places
			a. 30 / 31 = 0.96774193548
			b. 28 / 31 = 0.90322580645
			# Round to the nearest two decimal digit number with an even number as the least significant digit
			a. 0.96774193548 => 0.96
			b. 0.90322580645 => 0.90

## Hints:
- Use string format method
- Use list and dict data structure
- Use annotation to wrap functions which prompts users for domain restricted data
- Built-in functions `round` and `floor` may not satisfy rounding requirements