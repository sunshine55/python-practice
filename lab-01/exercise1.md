# LAB-01: BASICS #
## Objectives ##
- Basic language contruct
- User input
- Flow control
    + Conditional
    + Loops
    + Exception handling

## Content ##
Create a simple help manual for Python base on the book 
*Learning Python Fourth Edition*. 
	
**Requirements**:

- Screen #1: Display a welcome banner and instruct user what to do at first. Move to next screen (#2-1,#2-2 or #2-3 depending on user's choice)

			WELCOME TO SIMPLE PYTHON MANUAL 1.0
			Please choose a category:
			1. Data types and related operations
			2. Statement and syntax
			3. Modules
			q: Exit
			Your choice: _

- Screen #2-1: If user hits `1`, display the following screen:

			1. Data types and related operations:
			Which data type would you like to know more about?
			a.String	b.Int	c.Float		d.Complex	e.Bool		
			f.FronzenSet		g.Tuple		h.Bytes
			i.Bytearray	i.List	j.Set		k.Dict	l.Object
			
			1:BACK TO MAIN MENU
			q: Exit
			========================  
			Your choice: _

	User is navigated to screen #2-1-a...#2-1-l depending on user's choice  

- Screen #2-2: If user hits `2`, display the following screen:
			
			2. Statement and syntax
			Which syntax would you like to know more about?
			a.Assignment	b.Conditional	c.Loops
			d.Function		e.Class			f.Method
			g.Exception
			
			1:BACK TO MAIN MENU
			q: Exit
			========================
			Your choice: _

- Screen #2-3: If user hits `3`, display the following screen:
			
			3. Modules
			// Content under development
			// Please checkback later


	Let's create two sample screens #2-1-a and #2-1-b:
	
- Screen #2-1-a:
	
			Data types and related operations:
			String:
			// Content under development
			// Please checkback later
			1:BACK TO MAIN MENU
			2:BACK TO "Data types and related operations"
			q: Exit
			
			========================
			Your choice: _

- Screen #2-1-b:
	
			Data types and related operations:
			Int:
			// Content under development
			// Please checkback later
			1:BACK TO MAIN MENU
			2:BACK TO "Data types and related operations"
			q: Exit
			========================
			Your choice: _

	User is navigated back to **screen #1** when hitting `1`, **screen#2-1** when hitting `2`.

- General behaviors:
	+ System exits when user hits `q`
	+ System must only accept  

_Hints:_

- control flow constructs: if..elif..else.. and while ..
- User input:

	    name = raw_input('Your name:')

Gives you the following prompt on the console and waits for user input:

	Your name: _
