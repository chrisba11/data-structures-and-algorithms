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


def test_add_two_edges_one_not_in_table():
    with pytest.raises(KeyError) as exc:
        g = Graph()
        g.add_vertex('potato')
        g.add_vertex('salad')

        g.add_edge('potato', 'salad', 12)
        g.add_edge('potato', 'macaroni', 6)

    assert 'macaroni was not found' in str(exc.value)


def test_get_vertices():
    g = Graph()
    g.add_vertex('potato')
    g.add_vertex('salad')
    g.add_vertex('macaroni')

    assert g.get_vertices() == ['potato', 'salad', 'macaroni']


def test_get_vertices_none():
    g = Graph()
    assert g.get_vertices() is None


def test_get_neighbors():
    g = Graph()
    g.add_vertex('potato')
    g.add_vertex('salad')
    g.add_vertex('macaroni')

    g.add_edge('potato', 'salad', 12)
    g.add_edge('potato', 'macaroni', 6)

    assert g.get_neighbors('potato') == {'salad': 12, 'macaroni': 6}


def test_get_neighbors_not_in_graph():
    with pytest.raises(KeyError) as exc:
        g = Graph()
        g.get_neighbors('macaroni')
    assert 'macaroni was not found' in str(exc.value)


def test_size():
    g = Graph()
    g.add_vertex('potato')
    g.add_vertex('salad')
    g.add_vertex('macaroni')
    assert g.size() is 3


def test_size_empty():
    g = Graph()
    assert g.size() is 0
