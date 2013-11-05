# LAB-02: MAGENTO CONFIG VALIDATION #
## Objectives ##
- XML processing
- File IO
- User interaction
- Exception handling
- To know the structure of Magento modules

## Content ##
Magento relies heavily on XML config files. Create a Python script that:

- Reads Magento module XML config file
- Validates the config file (well-formed and Magento-compatible)
- Verifies that files exist as per specified in the config
  
**Notice:** Please carefully refer to Chapter 4 of the book *Magento Developer's Guide*
	
**Requirements**:

- Screen #1: Display a welcome banner and instruct user what to do at first.

		WELCOME TO MAGENTO MODULE VALIDATOR
		Please specify a Magento module config file
		File location: D:\magento\app\etc\modules\Mdg_Giftregistry.xml_
	The system **must** ensure that the file path points to an accessible file. If the file is not accessible, reports the error:

		Error: THIS IS THE REASON WHY YOU CANNOT ACCESS [FILE] 
			
	and continues to prompt `File location: _` until the file path points to an accessible file or user issues a `Ctrl + C` 

	When the file path is accessible, display the following message so that user may know the system has successfully opened the file:

		Please wait, the process may take a few minutes
		Analyzing... 

- Screen #2-a: If the XML config is well-form
		
		Modules:
		- Mdg_Giftregistry
		- Mdg_GoodModule
		
		Module details:
		- Mdg_Giftregistry
			+ Models: 
					Mdg_Giftregistry_Model: OK
					NameSpaceModuleName_ClassTypeB: Invalid name
					NameSpace_ModuleName_ClassTypeX: Class def not found
			+ Blocks
					Mdg_Giftregistry_BlockA: OK
			+ Helpers
					Mdg_Giftregistry_HelperA: OK
			+ Resources
					Mdg_Giftregistry_ResA: OK
			+ StrangeEntry
					Error: Magento does not support 'StrangeEntry'

		Would you like to save this report? (Y/n) _
	
	User is navigated to screen #3-a when answering `Y` or `Yes` otherwise user is naviated back to **Screen #1**

	**Notice**: Please refer to **page 90** of the book *Magento Developer's Guide* for further details on folder structure of module components

- Screen #2-b: If the XML config is NOT well-form

		Error: 
		Config file D:\magento\app\etc\modules\Mdg_Giftregistry.xml 
				is not well-formed
		Please double check

	User is immediately navigated back to **Screen #1**

- Screen #3-a: Prompts user for the location of report file

		Where would you like to save the report?
		File location: D:\magento\deploy\reports\mdg_gif.txt_

	The system **must** ensure that the file path points to an accessible file. If the file is not accessible, reports the error:

		Error: THIS IS THE REASON WHY YOU CANNOT ACCESS [FILE] 
			
	and continues to prompt `File location: _` until the file path points to an accessible file or user issues a `Ctrl + C` 

	When the file path is accessible, display the following message so that user may know the system has successfully opened the file:

		Report file has been successfully written

	User is immediately navigated back to **Screen #1**

- General behaviors:
	+ System exits when user issues `Ctrl + C` 

_Hints:_

- Use package `xml.etree` to read XML
- Group the file accessibility logic into a function
- Handle file IO related exceptions
- Use string format operations
- Consider this snippet `print 'a'*5` which prints:
		
		aaaaa
- Dict, List, Tuple, Set may involve
- Regular Expression is highly recommended. To use Regex:
		
		import re 