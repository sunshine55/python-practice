from datetime import datetime
import argparse, urllib2, sqlite3, sys, os

def download(url, fileName):    
    success = True
    req = urllib2.Request(url)
    existSize = 0
    openType = "wb"
    if os.path.exists(fileName):
        existSize = os.path.getsize(fileName)
        req.add_header("Range", "bytes=%s-" % existSize)
        openType = "ab"
    try:
        res = urllib2.urlopen(req)
    except Exception as e:
        print e.reason
        success = False
    else:
        with open(fileName, openType) as f:
            total = int(res.info().getheaders("Content-Length")[0])
            if total == existSize:
                print "File is completely downloaded"
                sys.exit()
            else:
                chunkDownload = 0
                chunkSize = 8192
                while True:
                    buffer = res.read(chunkSize)
                    if not buffer:
                        sys.stdout.write("\n")
                        break
                    chunkDownload += len(buffer)
                    f.write(buffer)            
                    sys.stdout.write("Downloaded %10d of %s bytes (%3.2f%%)\r" % (chunkDownload, total, (chunkDownload*100.)/total))
    finally:
        with sqlite3.connect("history.db3") as conn:
            cur = conn.cursor()
            if success:
                cur.execute("INSERT INTO Download (File,Date,Status) VALUES (?,?,?)", (fileName, datetime.now().replace(microsecond=0), "OK"))
            else:
                cur.execute("INSERT INTO Download (File,Date,Status) VALUES (?,?,?)", (fileName, datetime.now().replace(microsecond=0), "FAIL"))        

def show_history():
    print "DOWNLOAD HISTORY"        
    with sqlite3.connect("history.db3") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Download")
        col_names = [cn[0] for cn in cur.description]
        rows = cur.fetchall()
        print "%s %-35s %-20s %s" % (col_names[0], col_names[1], col_names[2], col_names[3])
        for row in rows:
            print "%2s %-35s %-20s %s" % row

def main():
    # Test URL
    # http://docs.python.org/archives/python-2.7.5-docs-pdf-letter.zip
    # http://docs.python.org/2/library/sqlite3.html
    # http://docs.python.org/2/library/blahla.zip
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--url',help="download link")
    parser.add_argument('-l','--list',action='store_true',help="list download history")
    args = parser.parse_args()
    url = args.url
    list = args.list
    if url:
        fileName = url.split('/')[-1]
        download(url, fileName)
    if list:
        show_history()

if __name__ == '__main__':
    main()