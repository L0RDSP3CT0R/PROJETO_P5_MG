# repository.py

# GUARDA AS TAREFAS NUMA LISTA SIMPLES
class RepositorioTarefas:
    def __init__(self):
        self.tarefas = []

    # ADICIONA UMA NOVA
    def adicionar(self, tarefa):
        self.tarefas.append(tarefa)

    # MOSTRA TODAS
    def listar(self):
        return self.tarefas

    # BUSCA UMA TAREFA PELO ÍNDICE
    def buscar(self, indice):
        if 0 <= indice < len(self.tarefas):
            return self.tarefas[indice]
        return None