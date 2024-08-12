'''
    this is a script to train using python
'''
from __future__ import annotations
import os
import sys
import urllib3

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.genfunctions.utensils import print_results


def main():
    '''
        main function
    '''
    url_data = "http://earthquake.usgs.gov/earthquakes/"\
               "feed/v1.0/summary/2.5_day.geojson"

    # Open the URL and read the data
    http = urllib3.PoolManager()
    web_url = http.request('GET', url_data)
    print_results(web_url.data)


if __name__ == '__main__':
    main()
