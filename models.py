#MODELS
from datetime import datetime
#CLASSE PARA GUARDAR TAREFAS
class Tarefa:
    def __init__(self, titulo, descricao, prioridade):
        self._titulo = titulo
        self._descricao = descricao
        self._prioridade = prioridade
        self._concluida = False
        self._data_criacao = datetime.now()
#FUNÇÃO CONCLUIR TAREFA
    def concluir(self):
        self._concluida = True
#SAIDA
    def __str__(self):
        status = "Concluída" if self._concluida else "Pendente"
        return f"{self._titulo} | {status} | Prioridade: {self._prioridade} | Criada em: {self._data_criacao.strftime('%d/%m/%Y %H:%M')}"