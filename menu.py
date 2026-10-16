#arquivo resposável por interagir com o usuário (menu)

from sqlalchemy.orm import Session

#imports dos arquivos bancos e crud, pra conectar/criar banco de dados atelie e inserir,listar e excluir informações
from bancos import conectar_sqlite, conectar_mysql
from crud import (
    inserir_pessoa,
    listar_pessoa,
    excluir_pessoa,
    inserir_nota,
    listar_nota,
    excluir_nota
)

escolha = input("Escolha o banco de dados:\n 1. SQlite \n" \
"2. MySQl \n" \
"Digite o número correspondente ao Banco de Dados")

if escolha == "1":
    #fazer o engine com sqlte
    engine = conectar_sqlite()
elif escolha == "2":
    #fazer engine com mysql
    engine = conectar_mysql()
else:
    #caso de errado
    print("Opção inválida!")
    exit()

#-----------------------------------------------------------------------------

with Session(engine) as session:

    while True:
        print("\n--+-- MENU DO ATELIÊ DE DESENHO --+--")
        print("1. Inserir aluno")
        print("2. Listar alunos")
        print("3. Excluir aluno")
        print("--------------------------")
        print("4. Inserir nota")
        print("5. Listar notas")
        print("6. Excluir nota")
        print("--------------------------")
        print("7. Alterar banco para SQLite")
        print("8. Alterar banco para MySQL")
        print("9. Sair")

        opcao = input("Digite o número correspondente: ")

        if opcao == "1":
            nome = input("Nome do aluno: ")
            turma = input("Turma: ")
            curso = input("Curso: ")

            inserir_pessoa(session, nome, turma, curso)

        elif opcao == "2":
            pessoas = listar_pessoa(session)

            for pessoa in pessoas:
                print(
                    f"ID: {pessoa.id}"
                    f"Nome: {pessoa.nome}"
                    f"Turma: {pessoa.turma}"
                    f"Curso: {pessoa.curso}"
                )

        elif opcao == "3":
            id_pessoa = int(input("Digite o ID do aluno que deseja excluir: "))
            excluir_pessoa(session, id_pessoa)

        elif opcao == "4":
            desenho = input("Nome do desenho: ")
            data = input("Data: ")
            nota = float(input("Nota: "))
            pessoa_id = int(input("ID do aluno responsável: "))

            inserir_nota(session, desenho, data, nota, pessoa_id)

        elif opcao == "5":
            notas = listar_nota(session)

            for nota in notas:
                print(
                    f"ID: {nota.id}"
                    f"Desenho: {nota.desenho}"
                    f"Data: {nota.data}"
                    f"Nota: {nota.nota}"
                    f"ID do aluno: {nota.pessoa_id}"
                )

        elif opcao == "6":
            id_nota = int(input("Digite o ID do desenho que deseja excluir: "))
            excluir_nota(session, id_nota)

        elif opcao == "7":
            session.close()

            engine = conectar_sqlite()
            session = Session(engine)
            print("Banco alterado.")

        elif opcao == "8":
            session.close()
            
            engine = conectar_mysql()
            session = Session(engine)

            print("Banco alterado.")

        elif opcao == "9":
            print("Fechando sistema.")
            break

        else:
            print("Opção inválida! Tente novamente.")