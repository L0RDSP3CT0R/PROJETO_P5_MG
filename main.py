from models import Tarefa
from patterns import OrdenarPorData, OrdenarPorPrioridade, OrdenarPorStatus
from repositorio_tarefas import RepositorioTarefas

# GERENCIA AS TAREFAS (SINGLETON)
class GerenciadorDeTarefas:
    _instancia = None

    def __new__(cls):
        if not cls._instancia:
            cls._instancia = super().__new__(cls)
            cls._instancia.repo = RepositorioTarefas()
            cls._instancia.estrategia = OrdenarPorData()
        return cls._instancia

    # ADICIONA TAREFA
    def adicionar(self, tarefa):
        self.repo.adicionar(tarefa)

    # LISTA TAREFAS
    def listar(self):
        tarefas = self.estrategia.ordenar(self.repo.listar())
        if not tarefas:
            print("Nenhuma tarefa ainda.")
            return
        for t in tarefas:
            print(f"[{t.id}] {t}")

    # CONCLUI TAREFA PELO ID
    def concluir(self, indice):
        ok = self.repo.marcar_concluida(indice)
        if ok:
            print("Tarefa marcada como concluída!")
        else:
            print("Erro: tarefa não encontrada.")

    # MUDA O MODO DE ORDENAR
    def mudar_estrategia(self, nova):
        self.estrategia = nova


# FUNÇÃO PRINCIPAL
def menu():
    g = GerenciadorDeTarefas()

    while True:
        print("\n=== MENU DE TAREFAS ===")
        print("1 - Adicionar")
        print("2 - Listar")
        print("3 - Concluir")
        print("4 - Ordenação")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            t = input("Título: ")
            d = input("Descrição: ")

            # TRATAMENTO DE ERRO AQUI ↓↓↓
            try:
                p = int(input("Prioridade (1-5): "))
            except:
                print("Valor inválido, usando prioridade 1.")
                p = 1

            g.adicionar(Tarefa(t, d, p))
            print("Tarefa adicionada.")

        elif op == "2":
            g.listar()

        elif op == "3":
            # TRATAMENTO DE ERRO AQUI ↓↓↓
            try:
                i = int(input("Número da tarefa: "))
            except:
                print("ID inválido.")
                continue

            g.concluir(i)

        elif op == "4":
            print("1- Data  2- Prioridade  3- Status")
            esc = input("Escolha: ")
            if esc == "1": g.mudar_estrategia(OrdenarPorData())
            elif esc == "2": g.mudar_estrategia(OrdenarPorPrioridade())
            elif esc == "3": g.mudar_estrategia(OrdenarPorStatus())
            print("Modo de ordenação trocado.")

        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()