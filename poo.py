# Classe Turma com parametros do tipo de ensino, ano, turma e capacidade
class Turma:
    def __init__(self, tipo_ensino, ano, turma, capacidade):
        self.tipo_ensino = tipo_ensino
        self.ano = ano
        self.turma = turma
        self.capacidade = capacidade
        self.lista_alunos = []          # começa vazia
        self.lista_disciplinas = []     # disciplinas associadas à turma

    def exibir_turma(self): #Metodo para exibir turmas ja cadastradas
        print(f"Turma: {self.ano} - {self.turma}, Capacidade: {self.capacidade}")
        print("Lista de alunos:", [aluno.nome for aluno in self.lista_alunos])
        print("Disciplinas:", [disc.nome for disc in self.lista_disciplinas])


# Classe Aluno com parametros de nome, matricula e idade
class Aluno:
    def __init__(self, nome, matricula, idade):
        self.nome = nome
        self.matricula = matricula
        self.idade = idade
        self.desempenho = {}  # {cod_disciplina: {"notas": [], "faltas": 0}}

    def exibir_aluno(self): #Metodo para exibir alunos ja cadastrados
        print(f"{self.nome}, Matricula: {self.matricula}, Idade: {self.idade}")
        for cod, dados in self.desempenho.items():
            print(f"  Disciplina {cod}: Notas {dados['notas']}, Faltas {dados['faltas']}")


# Classe Disciplina com parametros de nome e codigo
class Disciplina:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

    def exibir_disciplina(self): #Metodo para exibir disciplinas ja cadastradas
        print(f"Disciplina: {self.nome}, Codigo: {self.codigo}")


# Classe Sistema
class System:
    def __init__(self):
        self.turmas = []
        self.alunos = []
        self.disciplinas = []

    # Metodo para criar turmas
    def create_turma(self, tipo_ensino, ano, turma, capacidade):
        if self.find_turma(tipo_ensino, ano, turma): #Verifica se a turma/ano/turma existe, é necessário o if vir antes da criação da nova turma para validação
            print("Turma já existe, por favor incluir nova turma!")
            return
        new_turma = Turma(tipo_ensino, ano, turma, capacidade)
        self.turmas.append(new_turma)
        print(f"Turma criada com sucesso: {ano}-{turma} com capacidade: {capacidade}")

    # Metodo para cadastrar alunos
    def register_aluno(self, nome, matricula, idade):
        if self.find_aluno(matricula): #Verifica se o aluno/matricula existe, é necessário o if vir antes da criação do novo aluno para validação
            print("Aluno já existe, por favor incluir nova matricula!")
            return
        new_aluno = Aluno(nome, matricula, idade)
        self.alunos.append(new_aluno)
        print(f"Aluno cadastrado com sucesso: {nome}, Matricula: {matricula}, Idade: {idade}")

    #Metodo para registrar disciplinas
    def register_disciplina(self, nome, codigo):
        if self.find_disciplina(codigo): #Verifica se a disciplina/codigo existe, é necessário o if vir antes da criação da nova disciplina para validação
            print("Disciplina já existe, por favor incluir novo código!")
            return
        new_disciplina = Disciplina(nome, codigo)
        self.disciplinas.append(new_disciplina)
        print(f"Disciplina cadastrada com sucesso: {nome}, Codigo: {codigo}")

    #Metodo para procurar o aluno e realizar validações
    def find_aluno(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno
        return None

    #Metodo para realizar a busca de turmas
    def find_turma(self, tipo_ensino, ano, turma):
        for t in self.turmas:
            if t.tipo_ensino == tipo_ensino and t.ano == ano and t.turma == turma:
                return t
        return None

    #Metodo para realizar a busca de disciplinas
    def find_disciplina(self, codigo):
        for d in self.disciplinas:
            if d.codigo == codigo:
                return d
        return None

    #Metodo para matricular alunos em turmas
    def matricular_aluno(self, matricula, tipo_ensino, ano, turma):
        aluno = self.find_aluno(matricula)
        turma_obj = self.find_turma(tipo_ensino, ano, turma)
        if aluno and turma_obj:
            if len(turma_obj.lista_alunos) >= turma_obj.capacidade:
                print(f"Turma {turma_obj.ano}-{turma_obj.turma} cheia. Matrícula não realizada.")
                return
            turma_obj.lista_alunos.append(aluno)
            # inicializa desempenho do aluno para todas disciplinas da turma
            for disciplina in turma_obj.lista_disciplinas:
                aluno.desempenho[disciplina.codigo] = {"notas": [], "faltas": 0}
            print(f"Aluno {aluno.nome} matriculado com sucesso na turma {turma_obj.ano}-{turma_obj.turma}")
        else:
            print("Aluno ou turma não encontrada, por favor verificar!")

    def associate_disciplina(self, codigo, tipo_ensino, ano, turma):
        disciplina = self.find_disciplina(codigo)
        turma_obj = self.find_turma(tipo_ensino, ano, turma)
        if disciplina and turma_obj:
            if disciplina in turma_obj.lista_disciplinas:
                print("Disciplina já associada a esta turma.")
                return
            turma_obj.lista_disciplinas.append(disciplina)
            # inicializa desempenho para todos alunos já matriculados
            for aluno in turma_obj.lista_alunos:
                if codigo not in aluno.desempenho:
                    aluno.desempenho[codigo] = {"notas": [], "faltas": 0}
            print(f"Disciplina {disciplina.nome} associada com sucesso à turma {turma_obj.ano}-{turma_obj.turma}")
        else:
            print("Disciplina ou turma não encontrada, por favor verificar!")

    def register_nota(self, matricula, codigo, nota):
        aluno = self.find_aluno(matricula)
        if aluno:
            if codigo in aluno.desempenho:
                aluno.desempenho[codigo]["notas"].append(nota)
                print(f"Nota {nota} registrada na disciplina {codigo} para o aluno {aluno.nome}")
            else:
                print("Disciplina não encontrada para este aluno.")
        else:
            print("Aluno não encontrado, por favor verificar!")

    def register_falta(self, matricula, codigo):
        aluno = self.find_aluno(matricula)
        if aluno:
            if codigo in aluno.desempenho:
                aluno.desempenho[codigo]["faltas"] += 1
                print(f"Falta registrada na disciplina {codigo} para o aluno {aluno.nome}")
            else:
                print("Disciplina não encontrada para este aluno.")
        else:
            print("Aluno não encontrado, por favor verificar!")
