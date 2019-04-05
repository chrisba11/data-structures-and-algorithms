from .graph import Graph
import pytest


def test_class_exists():
    assert Graph


def test_graph_instance():
    assert Graph()


def test_add_one_vertex():
    g = Graph()
    g.add_vertex('potato')
    assert 'potato' in g._graph


def test_add_two_vertices():
    g = Graph()
    g.add_vertex('potato')
    g.add_vertex('salad')
    assert 'potato' in g._graph
    assert 'salad' in g._graph
