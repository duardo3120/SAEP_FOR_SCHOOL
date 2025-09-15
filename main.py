from poo import System

#Função responsável pela exibição do menu
def menu():
    print("\n=== SAEP ===")
    print("1 - Criar Turma")
    print("2 - Cadastrar Aluno")
    print("3 - Cadastrar Disciplina")
    print("4 - Matricular Aluno em Turma")
    print("5 - Associar Disciplina à Turma")
    print("6 - Registrar Nota")
    print("7 - Registrar Falta")
    print("8 - Exibir Turmas")
    print("9 - Exibir Alunos")
    print("10 - Exibir Disciplinas")
    print("11 - Remover Aluno")
    print("12 - Remover Disciplina")
    print("13 - Remover Turma")
    print("14 - Atualizar Dados do Aluno")
    print("15 - Atualizar Dados da Disciplina")
    print("0 - Sair")
    return input("Escolha uma opção: ")

#Função principal do sistema
def main():
    system = System()
    system.carregar_dados() #Carrega os dados ao iniciar o sistema
    while True:
        opcao = menu()

        if opcao == "1":
            ensino = input("Tipo de Ensino (Fundamental/Médio): ")
            ano = input("Ano: ")
            turma = input("Turma: ")
            try: #Tentar realizar a conversão para int
                capacidade = int(input("Capacidade: "))
            except ValueError: #Em caso de erro informar ao usuário
                print("Capacidade deve ser número inteiro!")
                continue
            system.create_turma(ensino, ano, turma, capacidade)
            

        elif opcao == "2":
            nome = input("Nome do aluno: ")
            matricula = input("Matrícula: ")
            idade = input("Idade: ")
            system.register_aluno(nome, matricula, idade)

        elif opcao == "3":
            nome = input("Nome da disciplina: ")
            codigo = input("Código da disciplina: ")
            system.register_disciplina(nome, codigo)

        elif opcao == "4":
            matricula = input("Matrícula do aluno: ")
            ensino = input("Tipo de Ensino (Fundamental/Médio): ")
            ano = input("Ano: ")
            turma = input("Turma: ")
            system.matricular_aluno(matricula, ensino, ano, turma)

        elif opcao == "5":
            codigo = input("Código da disciplina: ")
            ensino = input("Tipo de Ensino (Fundamental/Médio): ")
            ano = input("Ano: ")
            turma = input("Turma: ")
            system.associate_disciplina(codigo, ensino, ano, turma)

        elif opcao == "6":
            matricula = input("Matrícula do aluno: ")
            codigo = input("Código da disciplina: ")
            try: #Tentar realizar a conversão para float
                nota = float(input("Nota: "))
            except ValueError: #Em caso de erro informar ao usuário
                print("Nota deve ser número válido!")
                continue
            system.register_nota(matricula, codigo, nota)

        elif opcao == "7":
            matricula = input("Matrícula do aluno: ")
            codigo = input("Código da disciplina: ")
            system.register_falta(matricula, codigo)

        elif opcao == "8":
            for turma in system.turmas.values():
                turma.exibir_turma() #Adicionado .values() para iterar sobre os valores do dicionário

        elif opcao == "9":
            for aluno in system.alunos.values(): #Adicionado .values() para iterar sobre os valores do dicionário
                aluno.exibir_aluno()

        elif opcao == "10":
            for disciplina in system.disciplinas.values(): #Adicionado .values() para iterar sobre os valores do dicionário
                disciplina.exibir_disciplina()

        elif opcao == "11":
            matricula = input("Matrícula do aluno a ser removido: ")
            tipo_ensino = input("Tipo de Ensino (Fundamental/Médio): ")
            ano = input("Ano: ")
            turma = input("Turma: ")
            system.remove_aluno(matricula, tipo_ensino, ano, turma)
            print(f"Aluno com matrícula {matricula} removido.")

        elif opcao == "12":
            codigo = input("Código da disciplina a ser removida: ")
            tipo_ensino = input("Tipo de Ensino (Fundamental/Médio): ")
            ano = input("Ano: ")
            turma = input("Turma: ")
            system.remove_disciplina(codigo, tipo_ensino, ano, turma)
            print(f"Disciplina com código {codigo} removida da turma {turma}.")

        elif opcao == "13":
            tipo_ensino = input("Tipo de Ensino (Fundamental/Médio): ")
            ano = input("Ano: ")
            turma = input("Turma: ")
            system.remove_turma(tipo_ensino, ano, turma)
            print(f"Turma {turma} do ano {ano} removida.")

        elif opcao == "14":
            matricula = input("Matrícula do aluno a ser atualizado: ")
            novo_nome = input("Novo nome: ")
            nova_idade = input("Nova idade: ")
            system.update_aluno(matricula, novo_nome if novo_nome else None, nova_idade if nova_idade else None)
            print(f"Dados do aluno com matrícula {matricula} atualizados.")

        elif opcao == "15":
            codigo = input("Código da disciplina a ser atualizado: ")
            novo_nome = input("Novo nome: ")
            system.update_disciplina(codigo, novo_nome if novo_nome else None)
            print(f"Dados da disciplina com código {codigo} atualizados.")

        elif opcao == "0":
            print("Encerrando o sistema...")
            system.salvar_dados() #Salva os dados antes de
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__": #Verifica se o script está sendo executado diretamente
    main() #Executa a função principal
