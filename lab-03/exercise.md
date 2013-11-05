# LAB-03: DOWNLOADER #
## Objectives ##
- Networking with HTTP protocol/FTP protocol
- Integration with MySQL/SQLite Database
- File IO
- Passing variables from command line
- Exception handling

## Content ##
Script a resumable downloader which can be executed in a CLI environment. For example, when user issues:

	 python download.py http://www.gigafile.com/f/abc.zip d:\abc.zip 
	
the system will download file [abc.zip](http://www.gigafile.com/f/abc.zip) and store in D: drive as abc.zip. 

**Requirements**:

1. The system must download the file at a given URL and save to a given local file. The syntax is:

		python download.py URL LOCAL_FILE

	The system must display a progress indicator:

		Downloading: 35% (30 seconds remaining)

	In case of any error (network access, disk full, file already exists...), the system must display a proper message to the user. For example:

		Download failed: Network problem

2. If the system can resume a previously interrupted download, the download process must resume and display

		Continuing to download at 45%
		Downloading: 45% (50 minutes remaining)

3. To restart a previously interrupted download, user must specify an `-r` or `--restart` flag from the command line
	
		python download.py URL LOCAL_FILE -r
		# OR #
		python download.py URL LOCAL_FILE --restart

4. The default storage is Sqlite3. To enable MySQL storage, database related options must be set from the command line

		python download.py URL LOCAL_FILE --db localhost;database;username;password

	Without the database related options, download information is stored in a Sqlite3 file.

5. User can review a list of successful downloads by specifying `-h` or `--history` flag

		python download.py -h
		# OR #
		python download.py --history
		DOWNLOAD HISTORY
		1. www.files.com/f/abc.zip		2013-02-11 22:30	STATUS:OK
		2. lol.free.com/~/mysql.db		2013-03-13 12:50	STATUS:FAIL
		3. lol.free.com/~/mssql.db		2013-03-14 21:10	STATUS:OK

	If there's no entry, display

		DOWNLOAD HISTORY
		(empty)

	The default storage is Sqlite3. To look up a MySQL storage, database related options must be set from the command line

6. General behaviors:
	+ The name of the Sqlite3 file is `download.db`, stored at the same directory as the `download.py` module
	+ The system must terminate when user issues `Ctrl + C`
	+ Bonus features could be: download rate, estimated time remaining..

#BONUS: 
I will offer you **a free drink** if you can make the command `python download http://www.gigafile.com/f/abc.zip d:\abc.zip` more friendly (look more native) to the host operating system. For example:

	download http://www.gigafile.com/f/abc.zip d:\abc.zip 
	download --history
	download URL LOCAL_FILE --db localhost;database;username;password

The solution must be available for *Windows* and *Linux (Ubuntu)*.

_Hints:_

- Refer to *Linux* GNU's `curl` utility for common behaviors 
- To print the download progress, consider the snippet

		sys.stdout.write("Download progress: %d%%   \r" % percent )
- Download history can be store in a Sqlite db or MySQL. To use MySQL, package MySQLdb must be installed. See [how](https://pypi.python.org/pypi/MySQL-python/1.2.4),