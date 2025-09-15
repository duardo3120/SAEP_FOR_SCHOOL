📚 SAEP — Sistema Acadêmico de Ensino em Python
📝 Descrição

O SAEP é um sistema de gerenciamento escolar feito em Python que permite realizar operações de CRUD sobre alunos, turmas e disciplinas.
Ele funciona no terminal e armazena os dados em arquivo JSON, garantindo persistência entre execuções.

🚀 Funcionalidades

Turmas

Criar e remover turmas

Exibir turmas cadastradas (com vagas disponíveis, alunos e disciplinas associadas)

Alunos

Cadastrar, atualizar e remover alunos

Matricular aluno em turma

Registrar notas e faltas

Exibir todos os alunos cadastrados

Exibir resumo de desempenho (médias e faltas por disciplina)

Disciplinas

Cadastrar, atualizar e remover disciplinas

Associar disciplina a uma turma

Exibir disciplinas cadastradas

📂 Estrutura do Projeto
├── dados.json        # Base de dados persistida em JSON
├── main.py           # Arquivo principal com menu e execução do sistema
├── poo.py            # Classes e regras de negócio (Aluno, Turma, Disciplina, System)
└── README.md         # Documentação do projeto

▶️ Como Executar

Clone este repositório ou baixe os arquivos.

Certifique-se de ter o Python 3.x instalado.

Execute o arquivo principal:

python main.py


Navegue pelo menu digitando a opção desejada.

📋 Menu Principal
=== SAEP ===
1 - Criar Turma
2 - Cadastrar Aluno
3 - Cadastrar Disciplina
4 - Matricular Aluno em Turma
5 - Associar Disciplina à Turma
6 - Registrar Nota
7 - Registrar Falta
8 - Exibir Turmas
9 - Exibir Alunos
10 - Exibir Disciplinas
11 - Remover Aluno
12 - Remover Disciplina
13 - Remover Turma
14 - Atualizar Dados do Aluno
15 - Atualizar Dados da Disciplina
16 - Exibir Resumo do Aluno
0 - Sair

🗄️ Exemplo de Estrutura de Dados (dados.json)
{
    "alunos": {
        "1": {
            "nome": "Eduardo",
            "idade": "12",
            "desempenho": {
                "1": {
                    "notas": [10.0],
                    "faltas": 1
                }
            }
        }
    },
    "disciplinas": {
        "1": {
            "nome": "Português"
        }
    },
    "turmas": {
        "('Medio', '1', 'A')": {
            "tipo_ensino": "Medio",
            "ano": "1",
            "turma": "A",
            "capacidade": 20,
            "alunos": ["1"],
            "disciplinas": ["1"]
        }
    }
}

🔮 Possíveis Melhorias Futuras

Geração de relatórios automáticos (médias gerais, aprovados/reprovados)

Exportação de dados para CSV/Excel

Integração com Pandas para análises mais avançadas

Interface gráfica (Tkinter ou PyQt)
