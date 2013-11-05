# LAB-04: ADVANCED OOP #
## Objectives ##
- Design patterns
	- Creational
	- Structural
	- Behavorial
- Python OOP

## Content ##
1. Create an image info inspector which supports popular formats (jpg, png, gif).
**Requirements:**
	- Screen #1: Display a welcome banner and instruct user what to do at first.

			WELCOME TO IMAGE INSPECTOR
			Please specify an image file:
			File location: D:\image.png_
		The system **must** ensure that the file path points to an accessible file. If the file is not accessible, reports the error:

			Error: THIS IS THE REASON WHY YOU CANNOT ACCESS [FILE] 
			
		and continues to prompt `File location: _` until the file path points to an accessible file or user issues a `Ctrl + C` 

		When the file path is accessible, display the following message so that user may know the system has successfully opened the file:

			Please wait, the process may take a few minutes
			Analyzing... 

	- Screen #2: If the binary content of the image file is valid according to the identified format. Display the content
	
			=[GENERAL INFO]========
			Name: image.png
			Location: D:\image.png
			Size: 300kb
			Format: PNG version 1.0
			=[DETAILS]=============
			Width:			200px
			Height: 		160px
			Color Depth:	32bpp
			
			
	_Hints:_
	+ Try not to use existing image libraries
	+ Use patterns: factory, module
	+ [PNG format documentation](http://www.libpng.org/pub/png/spec/ "PNG format documentation")
	+ [GIF format documentation](http://www.onicos.com/staff/iz/formats/gif.html)

2. WebFeed aggregator: Aggregate web feeds from multiple RSS or ATOM sources into a unified feed. The unified feed will then be served to interested clients in several possible formats (such as PlainText,HTML, JSON..)
	
	**Requirements:**
	- The syntax is:

			python webag.py [flags] URL [URL] [URL] [URL]
	
		The system displays a status indicator for each of the given URLs

			Checking URLs..
			www.gmail.com/a/b/feed.rss		OK
			www.esquire.com/rss				OK
			www.mashmagazine.com/site/atom	Could not reach

		If a URL is reachable, system displays an `OK` else system displays `Could not reach`

	- After all the given URLs are checked, if any of the given URLs is `OK`, the system becomes ready and displays this message

			WebFeed Aggregator is ready and running...

		If none of the URLs is `OK`, system quits after displays this message

			None of the given URLs is reachable. Exiting...

	- Feeds are refreshed every one minute. The number of new feed items from each URL are displayed:

			www.gmail.com/a/b/feed.rss		 	 1
			www.esquire.com/rss					20
			www.mashmagazine.com/site/atom		43

	- When user specifies option `--html 8080`, the unified feed is available at `localhost:8080`. User can use a HTTP protocol aware (web browsers such as Chrome, FF, Opera...). Sample HTML:

			<html>
				<body>
					<h1>Aggregated Feed</h1>
					<p>Last updated: Oct 04 2013 at 16:16</p>
					<section>
						<header><h2>Python 3.3 is released</h2></header>
						<p>Lorem ipsum sit amet consectuer</p>
						<a href="http://en.wikipedia.org/wiki/RSS">http://en.wikipedia.org/wiki/RSS</a>
					</section>
					<section>
						<header><h2>HTML5: Your choice... or theirs?</h2></header>
						<p>Lorem ipsum sit amet consectuer</p>
						<a href="http://en.wikipedia.org/wiki/RSS">http://en.wikipedia.org/wiki/RSS</a>
					</section>
				</body>
			</html>
	- When user specifies option `--plain 8081`, the unified feed is available in text format at `localhost:8081`. Sample text:
	
			Aggregated Feed
			Last updated: Oct 04 2013 at 16:16

			1. Python 3.3 is released
				Lorem ipsum sit amet consectuer
				Link at: http://en.wikipedia.org/wiki/RSS
			2. HTML5: Your choice... or theirs?
				Lorem ipsum sit amet consectuer
				Link at: http://en.wikipedia.org/wiki/RSS
	
	- Other than HTML and PlainText, it is also planned that other formats will be available soon, such as PNG image, PDF..
	- It is also planned that SMTP (email prototol) will be used to send emails to a list of subscribers using option `--email e1.mail@address.com e2.mail@address.com`. None-text based content such as PNG image and PDF must be attached to emails properly.
	
	_Hints:_
	+ Expect and Design for multiple web feed formats and multiple services (HTTP, SMTP)
	+ Useful patterns: Factory, Module, Observer, Adapter, Chain of responsibility
	+ Use module argparse, wsgiref, urllib2, xml
	+ [How to make a HTTP server with Python](http://webpython.codepoint.net/wsgi_request_parsing_get)