

import sqlite3
from models import Tarefa
from datetime import datetime

class RepositorioTarefas:
    def __init__(self):
        # TENTEI CONECTAR NO BANCO (ELE CRIA SE NÃO TIVER)
        self.conn = sqlite3.connect("tarefas.db")
        self.cursor = self.conn.cursor()

        print("conectado no banco (acho)")

        # CRIANDO A TABELA (SE TIVER JA NÃO FAZ NADA)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            descricao TEXT,
            prioridade INTEGER,
            concluida INTEGER,
            data TEXT
        )
        """)
        self.conn.commit()

    # ADICIONAR TAREFA
    def adicionar(self, tarefa):
        try:
            self.cursor.execute("""
                INSERT INTO tarefas (titulo, descricao, prioridade, concluida, data)
                VALUES (?, ?, ?, ?, ?)
            """, (
                tarefa.titulo,
                tarefa.descricao,
                tarefa.prioridade,
                1 if tarefa.concluida else 0,
                tarefa.data_criacao.isoformat()
            ))

            self.conn.commit()
            print("adicionei uma tarefa ai")
        except Exception as erro:
            print("deu erro pra adicionar:", erro)

    # LISTAR TODAS
    def listar(self):
        self.cursor.execute("SELECT * FROM tarefas")
        dados = self.cursor.fetchall()

        lista = []

        # CRIANDO OS OBJETOS DE VOLTA
        for l in dados:
            t = Tarefa(l[1], l[2], l[3])
            t._concluida = bool(l[4])

            # SÓ PRA NÃO QUEBRAR CASO A DATA VENHA ZOADA
            try:
                t._data_criacao = datetime.fromisoformat(l[5])
            except:
                t._data_criacao = datetime.now()

            lista.append(t)

        return lista

    # BUSCAR UMA POR ID
    def buscar(self, id):
        self.cursor.execute("SELECT * FROM tarefas WHERE id = ?", (id,))
        dado = self.cursor.fetchone()

        if not dado:
            return None  # NÃO ACHEI NADA

        # RECRIANDO A TAREFA
        t = Tarefa(dado[1], dado[2], dado[3])
        t._concluida = bool(dado[4])

        try:
            t._data_criacao = datetime.fromisoformat(dado[5])
        except:
            t._data_criacao = datetime.now()

        return t
