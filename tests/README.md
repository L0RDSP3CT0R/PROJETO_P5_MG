RF01 — Adicionar Tarefa
precisa permitir criar uma nova tarefa passando título, descrição e prioridade.

RF02 — Listar Tarefas
Mostrar todas as tarefas cadastradas, incluindo status (pendente/concluída), prioridade e data de criação.

RF03 — Concluir Tarefa
Permitir marcar uma tarefa como concluída.

RF04 — Filtrar/Ordenar Tarefas
Permitir listar as tarefas com base em critérios de ordenação definidos por estratégias (Strategy Pattern):

Por data de criação
Por prioridade
Por status (pendentes ou concluídas)
RF05 — Uso de Padrões de Projeto

Strategy: para definir diferentes modos de ordem das tarefas.
Singleton: para garantir uma unica instancia do gerenciador de tarefas.

+---------------------+
| Tarefa |
+---------------------+
| - titulo: str |
| - descricao: str |
| - prioridade: int |
| - concluida: bool |
| - data_criacao: date|
+---------------------+
| +concluir() |
+---------------------+

+-------------------------+
| GerenciadorDeTarefas |
+-------------------------+
| - tarefas: list[ Tarefa ] |
| - estrategia: EstrategiaOrdenacao |
+-------------------------+
| +adicionar(tarefa) |
| +listar() |
| +concluir(id) |
| +setEstrategia(e) |
+-------------------------+ 


+---------------------------------+
| EstrategiaOrdenacao (interface) |
+---------------------------------+
| +ordenar(tarefas): list |
+---------------------------------+

+----------------+ +------------------+ +-----------------+
| OrdenarPorData | | OrdenarPorPrioridade | | OrdenarPorStatus |
+----------------+ +------------------+ +-----------------+
| +ordenar() | | +ordenar() | | +ordenar() |
+----------------+ +------------------+ +-----------------+

projeto_tarefas/
│
├── models.py
├── patterns.py
├── repository.py
├── main.py
├── README.md
└── tests/
└── test_basic.py

Diagrama de Classes
[Diagrama de Classes](https://drive.google.com/file/d/1HZtNrspCazUbyUYHR2VsJvM8-2e_AMsF/view?usp=drive_link)


+------------------+
 banco de dados 
+------------------+

-cria a tabela se não existir
-salva cada tarefa nova
-puxa todas as tarefas do banco
-busca tarefa pelo ID
-converte os dados do banco de volta pros objetos Tarefa

Tabela:
-id chave primaria
-titulo
-descricao
-prioridade
-concluida 
-data



