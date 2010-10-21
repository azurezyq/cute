from parallel import parallel_map

timeout = 3 
import socket
socket.setdefaulttimeout(timeout)

def _do_crawl(url, args):
    try:
        import urllib2
        data = urllib2.urlopen(url).read()
        return True, data
    except:
        return False, None

def callback(url, ret, args, data):
    if ret:
        fp = args['output']
        data = ' '.join(data.split('\n'))
        print >>fp, url + '\t' + data

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 4:
        print 'usage: prog urllist outputfile threadnum'
        sys.exit(1)
    urllist = sys.argv[1]
    outputfile = sys.argv[2]
    threadnum = int(sys.argv[3])
    l = [x.strip() for x in open(urllist)]
    fp = open(outputfile, 'w')
    args = {}
    args['output'] = fp
    parallel_map(l, _do_crawl, callback, args, threadnum)
    fp.close()
