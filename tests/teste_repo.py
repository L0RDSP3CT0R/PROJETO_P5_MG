import unittest
from repositorio_tarefas import RepositorioTarefas
from models import Tarefa

class TestRepo(unittest.TestCase):
    def setUp(self):
        self.repo = RepositorioTarefas()  # cria um repositório limpo antes de cada teste

    def test_adicionar_tarefa(self):
        nova_tarefa = Tarefa("Teste", "Descrição da tarefa de exemplo", 3)  # criar uma tarefa para adicionar
        self.repo.adicionar(nova_tarefa)  # adiciona no repositório
        tarefas_atual = self.repo.listar()  # verifica que agora temos pelo menos uma tarefa
        self.assertGreater(len(tarefas_atual), 0, "DEVERIA HAVER PELO MENOS UMA TAREFA APÓS ADICIONAR")

    def test_buscar_tarefa_invalida_retorn_none(self):
        resultado = self.repo.buscar(99999)  # buscar por um id que não existe
        self.assertIsNone(resultado, "BUSCAR POR ID INEXISTENTE DEVE RETORNAR None")  # deve retornar None quando não encontra

    def test_listar_converte_para_lista(self):
        lista = self.repo.listar()  # pegar a lista de tarefas
        self.assertIsInstance(lista, list, "LISTAR DEVE RETORNAR UMA LISTA")  #  o retorno deve ser uma lista

if __name__ == "__main__":
    unittest.main()