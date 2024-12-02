import argparse
import osmnx as ox
import os

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-o", "--output", type=str, required=True,
                        help="Output filepath including the filename.")

    parser.add_argument("-p", "--preview", type=bool, required=False,
                        help="Preview the map data.")

    parser.add_argument("-a", "--airport", type=str, required=False,
                        default='LFBO',
                        help="Airport ICAO code")

    parser.add_argument("-f", "--filter", type=str, required=False,
                        default='["aeroway"~"runway|taxiway|apron|control_tower|control_center|gate|hangar|helipad|heliport|navigationaid|taxilane|terminal|windsock|highway_strip|parking_position|holding_position|airstrip|stopway|tower"]',
                        help="Custom OSM filter")

    parser.add_argument("-g", "--geojson", type=bool, required=False,
                        default=False,
                        help="GeoJson Output only")

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    G = ox.graph_from_place(
        args.airport,
        simplify=False,
        retain_all=True,
        truncate_by_edge=True,
        buffer_dist=1000,
        custom_filter=args.filter,
    )

    gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)

    if args.geojson:
        gdf_edges['geometry'].to_file(args.output, driver='GeoJSON')
    else:
        directory = os.path.dirname(args.output)
        filename = os.path.splitext(os.path.basename(args.output))[0]
        extension = os.path.splitext(os.path.basename(args.output))[1]
        gdf_nodes.to_file(os.path.join(directory, filename + '-nodes' + extension), driver='GeoJSON')
        gdf_edges.to_file(os.path.join(directory, filename + '-edges' + extension), driver='GeoJSON')

    if args.preview:
        f, ax = ox.plot_graph(
            G,
            figsize=(15, 15),
            bgcolor="black",
            edge_color="white",
            edge_linewidth=1,
            node_size=0,
            show=True,
        )

if __name__ == '__main__':
    main()
