from ..graph.graph import Graph
from .breadth_first import breadth_first
import pytest


def test_exists():
    assert breadth_first


def test_empty_graph():
    g = Graph()
    assert breadth_first(g, 'smoke') == []


def test_one_vertex():
    g = Graph()
    g.add_vertex('smoke')
    assert breadth_first(g, 'smoke') == ['smoke']


def test_two_vertices_no_edge():
    g = Graph()
    g.add_vertex('smoke')
    g.add_vertex('mirrors')
    assert breadth_first(g, 'smoke') == ['smoke']


def test_two_vertices_with_edge():
    g = Graph()
    g.add_vertex('smoke')
    g.add_vertex('mirrors')
    g.add_edge('smoke', 'mirrors')
    assert breadth_first(g, 'smoke') == ['smoke', 'mirrors']


def test_three_vertices_with_edge_between_two():
    g = Graph()
    g.add_vertex('smoke')
    g.add_vertex('mirrors')
    g.add_vertex('burgers')
    g.add_edge('smoke', 'mirrors')
    assert breadth_first(g, 'mirrors') == ['mirrors', 'smoke']
    assert breadth_first(g, 'burgers') == ['burgers']


def test_several_vertices_with_edges():
    g = Graph()
    g.add_vertex('smoke')
    g.add_vertex('mirrors')
    g.add_vertex('burgers')
    g.add_vertex('hot dog')
    g.add_vertex('potato')
    g.add_vertex('llama')
    g.add_vertex('pickle')
    g.add_edge('smoke', 'mirrors')
    g.add_edge('smoke', 'burgers')
    g.add_edge('smoke', 'hot dog')
    g.add_edge('potato', 'burgers')
    g.add_edge('potato', 'llama')
    g.add_edge('pickle', 'burgers')
    g.add_edge('llama', 'hot dog')
    g.add_edge('pickle', 'mirrors')
    assert breadth_first(g, 'burgers') == ['burgers', 'smoke', 'potato', 'pickle', 'mirrors', 'hot dog', 'llama']
