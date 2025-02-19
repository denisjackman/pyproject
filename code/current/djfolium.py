'''
    this is a test script
    reference : https://www.youtube.com/watch?v=FdqDgoG-SFM
    pip install folium
'''
import folium


def main():
    ''' this is the main function '''
    print("this is the main function")


if __name__ == "__main__":
    main()
    mymap = folium.Map(location=[38.58, -99.09],
                       zoom_start=6, control_scale=True)
    mymap.save("Z:/Resources/Data/test.html")
