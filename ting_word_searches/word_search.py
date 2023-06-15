def exists_word(word, instance):
    results = []

    for index in range(len(instance)):
        file_info = instance.search(index)
        file_name = file_info["nome_do_arquivo"]
        lines = file_info["linhas_do_arquivo"]

        occurrences = []

        for line_index, line in enumerate(lines, start=1):
            if word.lower() in line.lower():
                occurrences.append({"linha": line_index})

        if occurrences:
            results.append({
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences
            })

    return results


def search_by_word(word, instance):
    results = []

    for index in range(len(instance)):
        file_info = instance.search(index)
        file_name = file_info["nome_do_arquivo"]
        lines = file_info["linhas_do_arquivo"]

        occurrences = []

        for line_index, line_content in enumerate(lines, start=1):
            if word.lower() in line_content.lower():
                occurrences.append({
                    "linha": line_index,
                    "conteudo": line_content
                })

        if occurrences:
            results.append({
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences
            })

    return results
