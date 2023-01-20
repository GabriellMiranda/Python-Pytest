from code.bytebank import Funcionario


def teste_idade():
    funcionario_test = Funcionario("test", "13/03/2000", 1111)
    print(f'Teste = {funcionario_test.idade()}')


teste_idade()