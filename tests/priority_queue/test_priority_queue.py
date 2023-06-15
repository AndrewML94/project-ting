from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue = PriorityQueue()
    queue.enqueue({"nome_do_arquivo": "arquivo1.txt", "qtd_linhas": 10})
    queue.enqueue({"nome_do_arquivo": "arquivo2.txt", "qtd_linhas": 3})
    queue.enqueue({"nome_do_arquivo": "arquivo3.txt", "qtd_linhas": 7})

    assert len(queue.high_priority) == 1
    assert len(queue.regular_priority) == 2

    assert queue.dequeue() == {"nome_do_arquivo": "arquivo2.txt",
                               "qtd_linhas": 3}
    assert queue.dequeue() == {"nome_do_arquivo": "arquivo1.txt",
                               "qtd_linhas": 10}
    assert queue.dequeue() == {"nome_do_arquivo": "arquivo3.txt",
                               "qtd_linhas": 7}
    assert len(queue) == 0

    queue.enqueue({"nome_do_arquivo": "arquivo1.txt", "qtd_linhas": 10})
    queue.enqueue({"nome_do_arquivo": "arquivo2.txt", "qtd_linhas": 3})
    queue.enqueue({"nome_do_arquivo": "arquivo3.txt", "qtd_linhas": 7})

    assert queue.search(0) == {"nome_do_arquivo": "arquivo2.txt",
                               "qtd_linhas": 3}
    assert queue.search(2) == {"nome_do_arquivo": "arquivo3.txt",
                               "qtd_linhas": 7}
    assert queue.search(1) == {"nome_do_arquivo": "arquivo1.txt",
                               "qtd_linhas": 10}

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(-19)
