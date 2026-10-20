import networkx as nx
from pyvis.network import Network


class GraphVisualizer:
    @staticmethod
    def render_to_html(
        nx_graph: nx.DiGraph, output_filename: str = "graph.html"
    ) -> str:
        """Renders the NetworkX graph into an interactive HTML visualization using PyVis."""
        net = Network(height="600px", width="100%", notebook=False, directed=True)
        net.from_nx(nx_graph)

        # Customize aesthetic properties
        net.repulsion(node_distance=120, central_gravity=0.2, spring_length=100)

        for node in net.nodes:
            node["color"] = "#4A90E2"
            node["shape"] = "dot"
            node["size"] = 15

        net.save_graph(output_filename)
        return output_filename
