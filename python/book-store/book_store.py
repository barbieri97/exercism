""" calculate the discont for books """
from collections import Counter

POR_BOOK = 800.00
POR_GROUP = {
    1: 1 * POR_BOOK * 1.00,
    2: 2 * POR_BOOK * 0.95,
    3: 3 * POR_BOOK * 0.90,
    4: 4 * POR_BOOK * 0.80,
    5: 5 * POR_BOOK * 0.75,
}

def total(basket):
    """ calculate the best combination to discount and return the best value """
    # identifica quantos livros tem de cada serie
    volumes = Counter(basket)
    # preço sem nenhum desconto
    price = len(basket) * POR_BOOK
    # looping para verificar o preço que cada combinação gera
    for size in range(len(volumes), 1, -1):
        # retira um grupo dado o size do grupo que esta sendo testado
        group =  volumes - Counter(k for k, _ in volumes.most_common(size))
        # grupo sem o grupo retirado para add ao valor do grupo ja retirado
        group_books = sorted(group.elements())
        # verifica qual preço é menor, o ja dado (price) ou a nova combinação
        # (POR_GROUP[size] + total(group_books))
        price = min(price, POR_GROUP[size] + total(group_books))
    return price
