from ..graph.graph import Graph
from .get_edge import get_edge
import pytest


def test_exists():
    assert get_edge


def test_works_with_empty_list():
    g = Graph()
    g.add_vertex('Sydney')
    g.add_vertex('Melbourne')
    g.add_edge('Sydney', 'Melbourne')
    assert get_edge(g, []) is (False, 0)


def test_works_with_single_item_in_list():
    g = Graph()
    g.add_vertex('Sydney')
    g.add_vertex('Melbourne')
    g.add_edge('Sydney', 'Melbourne')
    assert get_edge(g, ['Sydney']) is (False, 0)
