#
# Recieving data from the internet
#
import urllib.request

def main():
    # retrieve data from 
    webUrl = urllib.request.urlopen("http://www.google.com")
    print("Result code: " + str(webUrl.getcode()))
    data = webUrl.read()
    print(data)


if __name__ == "__main__":
    main()