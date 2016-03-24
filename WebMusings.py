import urllib;


def read(urlString):
    url = urlString;
    result = urllib.urlopen(url);
    if result.getcode() == 200:
        return result.read();
    else:
        print "Could not open URL: " + url;
        return "Could not open URL: " + url;

def writeToFile(file, content):
    output = open(file, 'w');
    output.write(content);
    output.close();

if __name__ == '__main__':
    page = 'http://nhl.com';
    print "Requesting: "+ page;
    writeToFile( 'log.txt' ,read(page));

