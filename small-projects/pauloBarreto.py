class Cliente():
    """Cliente"""

    def __init__(self, nome, cpf, *contas):
        self.__nome = nome
        self.__cpf = cpf
        self.__contas = contas
    def get_nome(self):
        return self.__nome
    def get_listaContas(self):
        return self.__contas


class ContaBancaria():
    """ContaBancaria"""

    def __init__(self, *args):
        self.__agencia = args[0]
        self.__conta = args[1]
        self.__saldo = args[2]
    def get_saldo(self):
        return self.__saldo

conta1 = ContaBancaria(*[1, 11111, 2000])
conta2 = ContaBancaria(*[2, 22222, 1500])

cliente1 = Cliente('Paulo', 123123213, *[conta1, conta2])

somaContasC1 = 0

for contasC1 in cliente1.get_listaContas():
    somaContasC1 += contasC1.get_saldo()

print(somaContasC1)
