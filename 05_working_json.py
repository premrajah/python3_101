#
# Working with JSON
#
import urllib.request
import json

## 
def printResults(data):
    ## use json module to load the string data into a disctionary
    theJSON = json.loads(data)

    ## now we can access the contents of the json like any other python object
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    ## output number of events
    count = theJSON["metadata"]["count"]
    print(str(count) + " events recorded.")

    print("--")

    ## for each event, print the place fo the event
    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print("------------\n")

    ## magitude of each event 
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
    
    print("------------\n")

    ## events that were felt 
    print("Events that were felt: ")
    
    for i in theJSON["features"]:
        feltreports = i["properties"]["felt"]

        if feltreports != None:
            if feltreports > 0:
                print("%2.1f" % i["properties"]["mag"], i["properties"]["place"],
                "Reported " + str(feltreports) + " times.")
            



def main():
    # url data feed
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    ## open the url and read the data
    webUrl = urllib.request.urlopen(urlData)
    print("Result code: " + str(webUrl.getcode()))

    if(webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Error: cannot parse results")


if __name__ == "__main__":
    main()