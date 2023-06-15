import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(0, len(instance)):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            return

    lines = txt_importer(path_file)
    instance.enqueue({
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    })

    processed_file = instance.search(len(instance) - 1)
    print(processed_file)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
        return

    removed_file = instance.dequeue()
    print(f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        file_info = instance.search(position)
        print(file_info)
    except IndexError:
        sys.stderr.write("Posição inválida\n")
