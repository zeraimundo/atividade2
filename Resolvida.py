from abc import ABC, abstractmethod


class Vacina(ABC):
    def __init__(self, numDoses, tecnologia):
        self.__numDoses = numDoses
        self.__aprovada = False
        self.__preço = 0.0  # preço por dose
        self.__tecnologia = tecnologia  # tecnologia por trás da produção da vacina

    @property
    def numDoses(self):
        return self.__numDoses

    @numDoses.setter
    def numDoses(self, novaDose):
        self.__numDoses = novaDose

    @property
    def aprovada(self):
        return self.__aprovada

    @aprovada.setter
    def aprovada(self, status):
        self.__aprovada = status

    @property
    def preço(self):
        return self.__preço

    @preço.setter
    def preço(self, novoPreço):
        assert novoPreço >= 0
        self.__preço = novoPreço

    @property
    def tecnologia(self):
        return self.__tecnologia

    @tecnologia.setter
    def tecnologia(self, novaTecnologia):
        self.__tecnologia = novaTecnologia

    @abstractmethod
    def country(self):
        pass


class Oxford(Vacina):
    __LABORATORIO = 'AstraZeneca     '

    def __init__(self, numDoses, intervalo, tecnologia, eficacia):
        super().__init__(numDoses, tecnologia)
        self.__intervalo = intervalo  # intervalo mínimo para aplicar a próxima dose
        self.__eficaciaGlobal = eficacia  # após as n doses

    @property
    def intervalo(self):
        return self.__intervalo

    @intervalo.setter
    def intervalo(self, novoIntervalo):
        self.__intervalo = novoIntervalo

    @property
    def eficacia(self):
        return self.__eficaciaGlobal

    @eficacia.setter
    def eficacia(self, novaEficacia):
        self.__eficaciaGlobal = novaEficacia

    def country(self):  # implementação do metodo abstrado
        return 'England'

    @classmethod
    def laboratorio(cls):
        return cls.__LABORATORIO

    def __str__(self):
        return f'''
Vacina {Oxford.__name__},
Laboratório: {self.laboratorio()},
Numero de Doses = {self.numDoses},
Tecnologia: {self.tecnologia},
Intervalo mínimo para aplicação da próxima dose: {self.intervalo},
Eficacia: {self.eficacia}%'''


class Sinovac(Vacina):
    __LABORATORIO = 'Sinovac BioTech  '

    def __init__(self, numDoses, intervalo, tecnologia, voluntários):
        super().__init__(numDoses, tecnologia)
        self.__intervalo = intervalo  # intervalo mínimo para a próxima dose
        self.__voluntários = voluntários  # voluntários em ensaios clínicos no Brasil

    @property
    def intervalo(self):
        return self.__intervalo

    @intervalo.setter
    def intervalo(self, novoIntervalo):
        self.__intervalo = novoIntervalo

    @property
    def voluntários(self):
        return self.__voluntários

    @voluntários.setter
    def volutários(self, novoNumero):
        self.__voluntários = novoNumero

    def country(self):  # implementação do metodo abstrado
        return 'China'

    @classmethod
    def laboratorio(cls):
        return cls.__LABORATORIO

    def __str__(self):
        return f'''
Vacina {Sinovac.__name__}, 
Laboratório: {self.laboratorio()},
Numero de Doses = {self.numDoses}, 
Tecnologia: {self.tecnologia},
Intervalo mínimo para aplicação da próxima dose: {self.intervalo}, 
Voluntários nos ensaios clínicos (BR): {self.voluntários}'''


class Janssen(Vacina):
    __LABORATORIO = 'Johnson & Johnson'

    def __init__(self, numDoses, tecnologia, armazenamento):
        super().__init__(numDoses, tecnologia)
        self.__armazenamento = armazenamento

    @property
    def armazenamento(self):
        return self.__armazenamento

    @armazenamento.setter
    def armazenamento(self, novoArmazenamento):
        self.__armazenamento = novoArmazenamento

    def country(self):  # implementação do metodo abstrado
        return 'EUA'

    @classmethod
    def laboratorio(cls):
        return cls.__LABORATORIO

    def __str__(self):
        return f'''
Vacina {Janssen.__name__}, 
Laboratório: {self.laboratorio()}, 
Numero de Doses = {self.numDoses}, 
Tecnologia: {self.tecnologia}, 
Armazenamento: {self.armazenamento}'''


class OMS:
    def __init__(self):
        self.__vacinas = []

    def cadastrarVacina(self, vacina):
        self.__vacinas.append(vacina)

    @property
    def vacinas(self):
        return self.__vacinas

    def listarVacinasAprovadas(self):
        # imprime cabeçalho
        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        print('{:<15}{:<20}{:<15}{:<20}'.format("VACINA", "LABORATORIO", "PAÍS", "TECNOLOGIA"))
        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        # imprime vacinas aprovadas pela OMS
        for v in self.vacinas:
            if (v.aprovada == True):
                print('{:<15}{:<20}{:<15}{:<20}'.format(type(v).__name__, v.laboratorio(), v.country(), v.tecnologia))


o = Oxford(2, 14, 'Vetor Viral (adenovirus)', 77)
o.aprovada = True
''' TESTE IMPRESSÃO
print(o)
print(o.country())
print()
'''

s = Sinovac(2, 20, 'Virus inativado (morto)', 12000)
s.aprovada = True
''' TESTE IMPRESSÃO
print(s)
print(s.country())
print()
'''

j = Janssen(1, 'Vetor Viral (adenovirus)', 'De 2 a 8 graus Celcius')
j.aprovada = True
''' TESTE IMPRESSÃO
print(j)
print(j.country())
'''

oms = OMS()
oms.cadastrarVacina(o)
oms.cadastrarVacina(s)
oms.cadastrarVacina(j)

''' TESTE IMPRESSÃO
print("teste impresão da lista por index")
print(oms.vacinas[0])
'''

print('\n\nListagem por polimorfismo')
print('--------------------------')
print()
oms.listarVacinasAprovadas()
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
Loading complete
