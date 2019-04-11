from .breadth_first import BreadthFirstGraph
import pytest


def test_exists():
    assert BreadthFirstGraph.breadth_first


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
    assert g.breadth_first('burgers') == [
        'burgers',
        'smoke',
        'potato',
        'pickle',
        'mirrors',
        'hot dog',
        'llama'
        ]
