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
