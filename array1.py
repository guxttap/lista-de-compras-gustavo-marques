# Lista de compras com produtos, preços e quantidades
compras = [
    {"produto": "Arroz", "preco": 5.50, "quantidade": 2},
    {"produto": "Feijao", "preco": 7.80, "quantidade": 1},
    {"produto": "Macarrao", "preco": 4.20, "quantidade": 3},
    {"produto": "Oleo", "preco": 6.00, "quantidade": 1},
    {"produto": "Acucar", "preco": 2.50, "quantidade": 5}
]

def exibir_lista_compras(lista):
    """Exibe os itens da lista de compras de forma formatada."""
    print("Lista de Compras:")
    for item in lista:
        print(
            f"Produto: {item['produto']} | "
            f"Quantidade: {item['quantidade']} | "
            f"Preço Unitário: R${item['preco']:.2f}"
        )

def calcular_total(lista):
    """Calcula o valor total da compra."""
    return sum(item['quantidade'] * item['preco'] for item in lista)

def encontrar_produto_mais_caro(lista):
    """Retorna o produto com maior preço unitário."""
    return max(lista, key=lambda x: x['preco'])

def encontrar_produto_maior_quantidade(lista):
    """Retorna o produto com a maior quantidade comprada."""
    return max(lista, key=lambda x: x['quantidade'])

# --- Execução do programa ---
exibir_lista_compras(compras)

total = calcular_total(compras)
produto_mais_caro = encontrar_produto_mais_caro(compras)
produto_maior_quantidade = encontrar_produto_maior_quantidade(compras)

print("\nResumo da Compra:")
print(f"Total de itens diferentes: {len(compras)}")
print(f"Total gasto: R${total:.2f}")
print(f"Produto mais caro: {produto_mais_caro['produto']} - R${produto_mais_caro['preco']:.2f}")
print(f"Produto com maior quantidade: {produto_maior_quantidade['produto']} - Quantidade: {produto_maior_quantidade['quantidade']}")
