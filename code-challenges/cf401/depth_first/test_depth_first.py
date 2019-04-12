from .depth_first import DepthFirstGraph
import pytest


def test_exists():
    assert DepthFirstGraph.depth_first


def test_empty_graph():
    g = DepthFirstGraph()
    assert g.depth_first('smoke') == []


def test_one_vertex():
    g = DepthFirstGraph()
    g.add_vertex('smoke')
    assert g.depth_first('smoke') == ['smoke']


def test_two_vertices_no_edge():
    g = DepthFirstGraph()
    g.add_vertex('smoke')
    g.add_vertex('mirrors')
    assert g.depth_first('smoke') == ['smoke']


def test_two_vertices_with_edge():
    g = DepthFirstGraph()
    g.add_vertex('smoke')
    g.add_vertex('mirrors')
    g.add_edge('smoke', 'mirrors')
    assert g.depth_first('smoke') == ['smoke', 'mirrors']


def test_three_vertices_with_edge_between_two():
    g = DepthFirstGraph()
    g.add_vertex('smoke')
    g.add_vertex('mirrors')
    g.add_vertex('burgers')
    g.add_edge('smoke', 'mirrors')
    assert g.depth_first('mirrors') == ['mirrors', 'smoke']
    assert g.depth_first('burgers') == ['burgers']


def test_several_vertices_with_edges():
    g = DepthFirstGraph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')
    g.add_vertex('E')
    g.add_vertex('F')
    g.add_vertex('G')
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('A', 'D')
    g.add_edge('E', 'C')
    g.add_edge('E', 'F')
    g.add_edge('G', 'C')
    g.add_edge('F', 'D')
    g.add_edge('G', 'B')
    assert g.depth_first('C') == ['C', 'A', 'B', 'G', 'D', 'F', 'E']

# graph._table dict found in test_several_vertices_with_edges()
#
# {
#     'A': {
#         'visited': True,
#         'neighbors': {'B': 0, 'C': 0, 'D': 0}
#     },
#     'B': {
#         'visited': True,
#         'neighbors': {'A': 0, 'G': 0}
#     },
#     'C': {
#         'visited': True,
#         'neighbors': {'A': 0, 'E': 0, 'G': 0}
#     },
#     'D': {
#         'visited': True,
#         'neighbors': {'A': 0, 'F': 0}
#     },
#     'E': {
#         'visited': True,
#         'neighbors': {'C': 0, 'F': 0}
#     },
#     'F': {
#         'visited': True,
#         'neighbors': {'E': 0, 'D': 0}
#     },
#     'G': {
#         'visited': True,
#         'neighbors': {'C': 0, 'B': 0}
#     },
# }
