# Projeto Tribe Is Not Google (Vigésimo sétimo projeto desenvolvido)

Neste projeto foi implementado um programa que simule um algoritmo de indexação de documentos similar ao do Google. O programa é capaz de identificar ocorrências de termos em arquivos TXT. Para isso, o programa desenvolvido possui dois módulos:

- Módulo de gerenciamento de arquivos que permite anexar arquivos de texto (formato TXT) e;
- Módulo de buscas que permite operar funções de busca sobre os arquivos anexados.

## Habilidades desenvolvidas

- Lógica;
- Capacidade de interpretação do problema;
- Capacidade de interpretação de um código legado;
- Capacidade de resolução do problema, de forma otimizada;
- Resolver o problemas/Otimizar algoritmos mesmo sob pressão.

## O que foi desenvolvido pelo autor

Todo o conteúdo e elementos presentes nas pastas "ting_file_management" e "ting_word_searches" foram desenvolvidos exclusivamente por mim, representando minha contribuição integral a este projeto. É importante mencionar que os demais arquivos foram elaborados pela equipe da Trybe como parte do contexto mais amplo do projeto.

## Requisitos do projeto

### Pacote ting_file_management

1. Implementar uma fila para armazenar os arquivos que serão lidos;
2. Implementar uma função txt_importer dentro do módulo file_management capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador;
3. Implementar a função process no módulo file_process. Essa função deverá ser capaz de transformar o conteúdo da lista gerada pela função txt_importer em um dicionário que será armazenado dentro da Queue;
4. Implementar uma função remove dentro do módulo file_process capaz de remover o primeiro arquivo processado;
5. Implementar uma função file_metadata dentro do módulo file_process capaz de apresentar as informações superficiais de um arquivo processado;
6. Implementar os testes para a classe PriorityQueue capaz de armazenar arquivos pequenos de forma prioritária;

### Pacote ting_word_searches

7. Implementar uma função exists_word, dentro do módulo word_search, que verifique a existência de uma palavra em todos os arquivos processados;
8. Implementar uma função search_by_word dentro do módulo word_search, que busque uma palavra em todos os arquivos processados.