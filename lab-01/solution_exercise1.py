def quit():
	print 'Thank you for choosing Python as your developing tool!'
	exit()

def choose(choices=[]):
	while True:
		choice = raw_input('Please choose: ')
		if len(choices)==0:
			return choice
		elif choice in choices:
			return choice
		else:
			print 'You must choose from one of the following: ', sorted(choices)

def main():
	choice = '0'	
	screen_data = screens[choice]
	while True:
		display_output = screen_data[0]
		print display_output
		print '========================'
		choice = choose(screen_data[1].keys())
		action = screen_data[1][choice]
		if type(action) is str:
			# action is a string (a key)
			screen_data = screens[action]
		else:
			# Execute action
			action()
	

# keyed by the selection path
screens = {
	'0':('''
WELCOME TO SIMPLE PYTHON MANUAL 1.0
Please choose a category:
1. Data types and related operations
2. Statement and syntax
3. Modules
q: Exit
''',{	'1':'2-1',
		'2':'2-2',
		'3':'2-3',
		'q':quit
	}),
	'2-1':('''
1. Data types and related operations:
Which data type would you like to know more about?
a.String	b.Int	c.Float		d.Complex	e.Bool		
f.FronzenSet		g.Tuple		h.Bytes
i.Bytearray	i.List	j.Set		k.Dict	l.Object

1:BACK TO MAIN MENU
q: Exit
''',{	'1':'0',
		'q':quit,
		'a':'2-1-a',
		'b':'2-1-b'
	}),
	'2-2':('''
2. Statement and syntax
Which syntax would you like to know more about?
a.Assignment	b.Conditional	c.Loops
d.Function		e.Class			f.Method
g.Exception

1:BACK TO MAIN MENU
q: Exit
''',{	'1':'0',
		'q':quit,
		'a':'2-1-a',
		'b':'2-1-b'
	}),
	'2-3':('''
3. Modules
// Content under development
// Please checkback later
1:BACK TO MAIN MENU
q: Exit
''',{	'1':'0',
		'q':quit
	}),
	'2-1-a':('''
Data types and related operations:
String:
// Content under development
// Please checkback later
1:BACK TO MAIN MENU
2:BACK TO "Data types and related operations"
q: Exit
''',{	'1':'0',
		'2':'2-1',
		'q':quit
	}),
	'2-1-b':('''
Data types and related operations:
Int:
// Content under development
// Please checkback later
1:BACK TO MAIN MENU
2:BACK TO "Data types and related operations"
q: Exit
''',{	'1':'0',
		'2':'2-1',
		'q':quit
	})
}

if __name__ == '__main__':
	main()
