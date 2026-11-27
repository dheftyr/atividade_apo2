# Sistema Escolar com Python e SQLite

Script didático em Python que cria e manipula um banco de dados relacional simples (`escola.db`) usando **SQLite** na biblioteca padrão do Python.

## O que este projeto demonstra

* Criação de tabelas relacionadas com chave primária (`PRIMARY KEY`) e chave estrangeira (`FOREIGN KEY`).
* Ativação de integridade referencial no SQLite via `PRAGMA foreign_keys = ON;`.
* Inserção de múltiplos registros com segurança usando parâmetros (`?`).
* Consulta combinando `estudantes` e `cursos` com `INNER JOIN`.
* Atualização (`UPDATE`) e remoção (`DELETE`) de registros filtrados com `WHERE`.
* Encerramento seguro da conexão com `try...finally`.

## Pré-requisitos

* **Python 3.10+** instalado na máquina (o módulo `sqlite3` e `pathlib` já vêm embutidos no Python).

## Como executar

1. Salve o código em um arquivo, por exemplo `escola.py`.
2. Abra o terminal na pasta do arquivo e execute:

```bash
python escola.py
