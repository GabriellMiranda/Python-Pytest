import pytest
from code.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_o_valor_de_22(self):
        funcionario = Funcionario("Gabriel", "13/03/2000", 1000)
        esperado = 23
        assert esperado == funcionario.idade()

    def test_quando_o_nome_recebe_lucar_carvalho_deve_retornar_apenas_carvalho(self):
        funcionario = Funcionario("Lucas Carvalho", "13/03/2000", 1000)
        esperado = 'Carvalho'
        assert esperado == funcionario.sobrenome()

    def test_quando_decrescimo_salario_recebe_100000_deve_retonar_90000(self):
        entrada_salario = 100000
        esperado = 90000
        funcionario_teste = Funcionario('Bragança', '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario
        assert resultado == esperado