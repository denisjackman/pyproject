'''
    this is a script to train using python
'''
import json
import urllib3


def print_results(data):
    '''
        print the results function
    '''
    the_json = json.loads(data)
    if "title" in the_json["metadata"]:
        print(the_json["metadata"]["title"])
    count = the_json["metadata"]["count"]
    print(str(count) + " events recorded ")


def main():
    '''
        main function
    '''
    url_data = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # Open the URL and read the data
    http = urllib3.PoolManager()
    web_url = http.request('GET',url_data)
    print_results(web_url.data)


if __name__ == '__main__':
    main()
