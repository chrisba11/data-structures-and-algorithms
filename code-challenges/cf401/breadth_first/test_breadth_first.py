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
