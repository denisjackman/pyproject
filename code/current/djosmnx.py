''' sample map from python
    reference :
https://github.com/gboeing/osmnx-examples/blob/main/notebooks/00-osmnx-features-demo.ipynb
'''
import osmnx as ox


def main():
    ''' this is the main function '''

    # download/model a street network for some city then visualize it
    G = ox.graph_from_place("Piedmont, California, USA", network_type="drive")
    fig, ax = ox.plot_graph(G)


if __name__ == "__main__":
    main()
