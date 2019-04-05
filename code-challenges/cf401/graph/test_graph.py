from .graph import Graph
import pytest


def test_class_exists():
    assert Graph


def test_graph_instance():
    assert Graph()


def test_add_one_vertex():
    g = Graph()
    g.add_vertex('potato')
    assert 'potato' in g._table


def test_add_two_vertices():
    g = Graph()
    g.add_vertex('potato')
    g.add_vertex('salad')
    assert 'potato' in g._table
    assert 'salad' in g._table


def test_add_one_edge_without_weight():
    g = Graph()
    g.add_vertex('potato')
    g.add_vertex('salad')

    g.add_edge('potato', 'salad')

    assert g._table['potato'] == {'salad': 0}
    assert g._table['salad'] == {'potato': 0}


def test_add_one_edge_with_weight():
    g = Graph()
    g.add_vertex('potato')
    g.add_vertex('salad')

    g.add_edge('potato', 'salad', 12)

    assert g._table['potato'] == {'salad': 12}
    assert g._table['salad'] == {'potato': 12}


def test_add_two_edges():
    g = Graph()
    g.add_vertex('potato')
    g.add_vertex('salad')
    g.add_vertex('macaroni')

    g.add_edge('potato', 'salad', 12)
    g.add_edge('potato', 'macaroni', 6)

    assert g._table['potato'] == {'salad': 12, 'macaroni': 6}
    assert g._table['salad'] == {'potato': 12}
    assert g._table['macaroni'] == {'potato': 6}
