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
    assert get_edge(g, []) == (False, 0)


@pytest.mark.skip
def test_works_with_single_item_in_list():
    g = Graph()
    g.add_vertex('Sydney')
    g.add_vertex('Melbourne')
    g.add_edge('Sydney', 'Melbourne', 150)
    assert get_edge(g, ['Sydney']) == (False, 1)


@pytest.mark.skip
def test_works_with_two_list_items():
    g = Graph()
    g.add_vertex('Sydney')
    g.add_vertex('Melbourne')
    g.add_edge('Sydney', 'Melbourne', 150)
    assert get_edge(g, ['Sydney, Melbourne']) == (True, 151)


@pytest.mark.skip
def test_works_with_multiple_list_items_false():
    g = Graph()
    g.add_vertex('Sydney')
    g.add_vertex('Melbourne')
    g.add_vertex('London')
    g.add_vertex('New York')
    g.add_edge('Sydney', 'Melbourne', 150)
    g.add_edge('London', 'Melbourne', 800)
    g.add_edge('London', 'New York', 600)
    assert get_edge(g, ['Sydney, Melbourne', 'New York']) == (False, 1)


@pytest.mark.skip
def test_works_with_multiple_list_items_true():
    g = Graph()
    g.add_vertex('Sydney')
    g.add_vertex('Melbourne')
    g.add_vertex('London')
    g.add_vertex('New York')
    g.add_edge('Sydney', 'Melbourne', 150)
    g.add_edge('London', 'Melbourne', 800)
    g.add_edge('London', 'New York', 600)
    assert get_edge(g, ['Sydney, Melbourne', 'London', 'New York']) == (True, 1551)
