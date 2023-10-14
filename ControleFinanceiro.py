
class ControleFinanceiro:
    def __init__(self):
        self.renda = 0
        self.despesas = []

    def add_renda(self, montante):
        self.renda += montante

    def add_despesas(self, categoria, montante):
        self.despesas.append((categoria, montante))

    def calcular_balanco(self):
        total_despesas = sum(montante for _, montante in self.despesas)
        return self.renda - total_despesas

    def sumario(self):
        balanco = self.calcular_balanco()
        print(f"Renda: ${self.renda:.2f}")
        print("Despesas:")
        for categoria, montante in self.despesas:
            print(f"- {categoria}: ${montante:.2f}")
        print(f"Balanço: ${balanco:.2f}")


def main():
    admin = ControleFinanceiro()

    while True:
        print("\nControle Financeiro")
        print("1. Adicione Renda")
        print("2. Adicione Despesa")
        print("3. Sumário")
        print("4. Sair")

        escolha = input("Escreva sua escolha: ")

        if escolha == '1':
            montante = float(input("Coloque o montante da renda: $"))
            admin.add_renda(montante)
            print("Renda adicionada com êxito.")
        elif escolha == '2':
            categoria = input("Coloque a categoria da despesa: ")
            montante = float(input("Coloque o montante da despesa: $"))
            admin.add_despesas(categoria, montante)
            print("Despesa adicionada com êxito.")
        elif escolha == '3':
            admin.sumario()
        elif escolha == '4':
            print("Encerrando programa.")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    main()
