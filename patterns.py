#PATTERNS
from abc import ABC, abstractmethod
# CLASSE BASE PRA ORDENAR TAREFAS
class EstrategiaOrdenacao(ABC):
    @abstractmethod
    def ordenar(self, tarefas):
        pass


# ORDENA PELA DATA
class OrdenarPorData(EstrategiaOrdenacao):
    def ordenar(self, tarefas):
        return sorted(tarefas, key=lambda t: t._data_criacao)



# ORDENA PELA PRIORIDADE
class OrdenarPorPrioridade(EstrategiaOrdenacao):
    def ordenar(self, tarefas):
        return sorted(tarefas, key=lambda t: t._prioridade, reverse=True)



# ORDENA PELO STATUS
class OrdenarPorStatus(EstrategiaOrdenacao):
    def ordenar(self, tarefas):
        return sorted(tarefas, key=lambda t: t._concluida)