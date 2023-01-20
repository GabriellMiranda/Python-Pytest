from datetime import date


class Funcionario:
    def __init__(self, nome: str, data_nascimento: str, salario: float) -> None:
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def salario(self) -> float:
        return self._salario

    def idade(self):
        data_nascimento_quebrada = self._data_nascimento.split('/')
        ano_nascimento = data_nascimento_quebrada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def sobrenome(self):
        nome_completo = self.nome.strip()
        nome_quebrado = nome_completo.split(' ')
        return nome_quebrado[-1]

    def calcular_bonus(self):
        valor = self._salario * 1.0
        if valor > 1000:
            valor = 0
        return valor

    def _eh_socio(self):
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return (self._salario >= 100000) and (self.sobrenome() in sobrenomes)

    def decrescimo_salario(self):
        if self._eh_socio():
            self._salario = self._salario * 0.9

    def __str__(self) -> str:
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'
