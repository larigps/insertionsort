def insertion_sort(elements):
    # Caso tenha 1 ou nenhum elemento, já esteja ordenada então retorna a lista
    if len(elements) <= 1:
        return elements

    for i in range(1, len(elements)):
        j = i - 1  # j representa o indice dos itens à esquerda a serem comparados
        key = elements[i]

        # Enquanto a lista não estiver no começo ou a chave é menor que os elementos já ordenados
        while j >= 0 and key < elements[j]:
            elements[j + 1] = elements[j]  # desloca elemento para a direita
            j = j - 1  # Compara o proximo item a esquerda
            elements[j + 1] = key  # insere a chave no seu lugar correspondente

    return elements  # Retorna a lista com os elementos ordenados


arr = ['B','R','Y','Q','A','C','T','F']
print('Resultado:',insertion_sort(arr))