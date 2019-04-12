from .breadth_first import BreadthFirstGraph
import pytest


def test_exists():
    assert BreadthFirstGraph().breadth_first


def test_empty_graph():
    g = BreadthFirstGraph()
    assert g.breadth_first('smoke') == []


def test_one_vertex():
    g = BreadthFirstGraph()
    g.add_vertex('smoke')
    assert g.breadth_first('smoke') == ['smoke']


def test_two_vertices_no_edge():
    g = BreadthFirstGraph()
    g.add_vertex('smoke')
    g.add_vertex('mirrors')
    assert g.breadth_first('smoke') == ['smoke']


def test_two_vertices_with_edge():
    g = BreadthFirstGraph()
    g.add_vertex('smoke')
    g.add_vertex('mirrors')
    g.add_edge('smoke', 'mirrors')
    assert g.breadth_first('smoke') == ['smoke', 'mirrors']


def test_three_vertices_with_edge_between_two():
    g = BreadthFirstGraph()
    g.add_vertex('smoke')
    g.add_vertex('mirrors')
    g.add_vertex('burgers')
    g.add_edge('smoke', 'mirrors')
    assert g.breadth_first('mirrors') == ['mirrors', 'smoke']
    assert g.breadth_first('burgers') == ['burgers']


def test_several_vertices_with_edges():
    g = BreadthFirstGraph()
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
    assert g.breadth_first('C') == ['C', 'A', 'E', 'G', 'B', 'D', 'F']
