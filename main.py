from model import treinar_modelo, prever_preco

modelo = treinar_modelo()

valor = float(input("Digite o valor base para previsão: "))
previsao = prever_preco(modelo, valor)

print(f"Preço previsto: R$ {previsao:.2f}")
