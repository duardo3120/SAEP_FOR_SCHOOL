import json

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
        self.turmas = {}
        self.alunos = {}
        self.disciplinas = {}

    def salvar_dados(self, arquivo="dados.json"): #Metodo para salvar os dados em um arquivo JSON, parametros de alunos,disciplinas e turmas
        dados = {
            "alunos": {mat: {"nome": a.nome, "idade": a.idade, "desempenho": a.desempenho} 
                   for mat, a in self.alunos.items()},
            "disciplinas": {cod: {"nome": d.nome} for cod, d in self.disciplinas.items()},
            "turmas": {str(chave): {
                        "tipo_ensino": t.tipo_ensino,
                        "ano": t.ano,
                        "turma": t.turma,
                        "capacidade": t.capacidade,
                        "alunos": [a.matricula for a in t.lista_alunos],
                        "disciplinas": [d.codigo for d in t.lista_disciplinas]
                    } for chave, t in self.turmas.items()}
        }
        with open(arquivo, 'w', encoding="utf-8") as f: #Abrir o arquivo em modo escrita
            json.dump(dados, f, indent=4, ensure_ascii=False) #Conversão de objeto python para JSON

    def carregar_dados(self, arquivo="dados.json"):
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
        except FileNotFoundError:
            print("Arquivo de dados não encontrado, iniciando com dados vazios.")
            return

    # Recriar alunos
        self.alunos = {}
        for mat, info in dados.get("alunos", {}).items():
            aluno = Aluno(info["nome"], mat, info["idade"])
            aluno.desempenho = info["desempenho"]
            self.alunos[mat] = aluno
        print(f"Alunos carregados: {list(self.alunos.keys())}")

    # Recriar disciplinas
        self.disciplinas = {}
        for cod, info in dados.get("disciplinas", {}).items():
            disciplina = Disciplina(info["nome"], cod)
            self.disciplinas[cod] = disciplina
        print(f"Disciplinas carregadas: {list(self.disciplinas.keys())}")

    # Recriar turmas
        self.turmas = {}
        for chave_str, info in dados.get("turmas", {}).items():
        # chave original era uma tupla, aqui armazenada como string
            chave = (info["tipo_ensino"], info["ano"], info["turma"])
            turma = Turma(info["tipo_ensino"], info["ano"], info["turma"], info["capacidade"])

        # Associar alunos já criados
        for mat in info.get("alunos", []):
            print(f"Tentando associar aluno {mat} na turma {info['ano']}-{info['turma']}")
            if mat in self.alunos:
                turma.lista_alunos.append(self.alunos[mat])
                print(f" -> Associado: {self.alunos[mat].nome}")
            else:
                print(f" -> Matrícula {mat} não encontrada em self.alunos")

        # Associar disciplinas já criadas
        for cod in info.get("disciplinas", []):
            print(f"Tentando associar disciplina {cod} na turma {info['ano']}-{info['turma']}")
            if cod in self.disciplinas:
                turma.lista_disciplinas.append(self.disciplinas[cod])
                print(f" -> Associada: {self.disciplinas[cod].nome}")
            else:
                print(f" -> Código {cod} não encontrado em self.disciplinas")

        self.turmas[chave] = turma

    print("Dados carregados com sucesso!")


    # Metodo para criar turmas
    def create_turma(self, tipo_ensino, ano, turma, capacidade):
        chave = (tipo_ensino, ano, turma) # Adicionado tupla como chave para evitar duplicatas
        if chave in self.turmas:  # já existe
            print(f"Erro: a turma {ano}-{turma} do {tipo_ensino} já existe.")
            return
        new_turma = Turma(tipo_ensino, ano, turma, capacidade)
        self.turmas[chave] = new_turma
        print(f"Turma criada com sucesso: {ano}-{turma} com capacidade: {capacidade}")


    # Metodo para cadastrar alunos
    def register_aluno(self, nome, matricula, idade):
        if matricula in self.alunos: #Verifica se a matricula existe, é necessário o if vir antes da criação do novo aluno para validação
            print("Aluno já existe, por favor incluir nova matricula!")
            return
        new_aluno = Aluno(nome, matricula, idade)
        self.alunos[matricula] = new_aluno #Usa a matricula como chave no dicionario
        print(f"Aluno cadastrado com sucesso: {nome}, Matricula: {matricula}, Idade: {idade}")

    #Metodo para registrar disciplinas
    def register_disciplina(self, nome, codigo):
        if codigo in self.disciplinas: #Verifica se o codigo existe, é necessário o if vir antes da criação da nova disciplina para validação
            print("Disciplina já existe, por favor incluir novo código!")
            return
        new_disciplina = Disciplina(nome, codigo)
        self.disciplinas[codigo] = new_disciplina #Usa o codigo como chave no dicionario
        print(f"Disciplina cadastrada com sucesso: {nome}, Codigo: {codigo}")

    #Metodo para procurar o aluno e realizar validações
    def find_aluno(self, matricula):
        return self.alunos.get(matricula, None) #Retorna none caso não encontre o aluno

    #Metodo para realizar a busca de turmas
    def find_turma(self, tipo_ensino, ano, turma):
        return self.turmas.get((tipo_ensino, ano, turma))  # retorna None se não achar


    #Metodo para realizar a busca de disciplinas
    def find_disciplina(self, codigo):
        return self.disciplinas.get(codigo) #Refatorando o método para usar get do dicionário

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

    def remove_aluno(self, matricula, tipo_ensino, ano, turma):
        aluno = self.find_aluno(matricula)
        turma_obj = self.find_turma(tipo_ensino, ano, turma)
        if aluno and turma_obj:
            if aluno in turma_obj.lista_alunos:
                turma_obj.lista_alunos.remove(aluno)
                # opcional: remover desempenho relacionado a essa turma
                for disciplina in turma_obj.lista_disciplinas:
                    if disciplina.codigo in aluno.desempenho:
                        del aluno.desempenho[disciplina.codigo]
                print(f"Aluno {aluno.nome} removido da turma {turma_obj.ano}-{turma_obj.turma}")
            else:
                print("Aluno não está matriculado nesta turma.")
        else:
            print("Aluno ou turma não encontrada, por favor verificar!")

    def remove_disciplina(self, codigo, tipo_ensino, ano, turma):
            disciplina = self.find_disciplina(codigo)
            turma_obj = self.find_turma(tipo_ensino, ano, turma)
            if disciplina and turma_obj:
                if disciplina in turma_obj.lista_disciplinas:
                    turma_obj.lista_disciplinas.remove(disciplina)
                    # opcional: remover desempenho relacionado a essa disciplina
                    for aluno in turma_obj.lista_alunos:
                        if codigo in aluno.desempenho:
                            del aluno.desempenho[codigo]
                    print(f"Disciplina {disciplina.nome} removida da turma {turma_obj.ano}-{turma_obj.turma}")
                else:
                    print("Disciplina não está associada a esta turma.")
            else:
                print("Disciplina ou turma não encontrada, por favor verificar!")

    def remove_turma(self, tipo_ensino, ano, turma):
        chave = (tipo_ensino, ano, turma)
        turma_obj = self.find_turma(tipo_ensino, ano, turma)
        if turma_obj:
            # opcional: limpar desempenho dos alunos relacionados a essa turma
            for aluno in turma_obj.lista_alunos:
                for disciplina in turma_obj.lista_disciplinas:
                    if disciplina.codigo in aluno.desempenho:
                        del aluno.desempenho[disciplina.codigo]
            del self.turmas[chave]
            print(f"Turma {ano}-{turma} removida com sucesso.")
        else:
            print("Turma não encontrada, por favor verificar!")

    def update_aluno(self, matricula, novo_nome=None, nova_idade=None):
        aluno = self.find_aluno(matricula)
        if aluno:
            if novo_nome:
                aluno.nome = novo_nome
            if nova_idade:
                aluno.idade = nova_idade
            print(f"Dados do aluno {matricula} atualizados com sucesso.")
        else:
            print("Aluno não encontrado, por favor verificar!")

    def update_disciplina(self, codigo, novo_nome=None):
        disciplina = self.find_disciplina(codigo)
        if disciplina:
            if novo_nome:
                disciplina.nome = novo_nome
            print(f"Dados da disciplina {codigo} atualizados com sucesso.")
        else:
            print("Disciplina não encontrada, por favor verificar!")
