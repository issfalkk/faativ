#este arquivo vai ser responsável por inserir, listar e excluir

from classes import Pessoa_atelie, Nota_atelie

#função para inserir pessoa atelie 
def inserir_pessoa(session, nome, turma, curso):
    pessoa = Pessoa_atelie(
        nome=nome,
        turma=turma,
        curso=curso
    )

    session.add(pessoa)
    session.commit()

#função para listar pessoa atelie 
def listar_pessoa(session):
    return session.query(Pessoa_atelie).all()

#função para excluir pessoa atelie 
def excluir_pessoa(session, id):
    pessoa = session.get(Pessoa_atelie, id)

    session.delete(pessoa)
    session.commit()


#função para inserir nota atelie
def inserir_nota(session, desenho, data, nota, pessoa_id):
    nova_nota = Nota_atelie(
        desenho=desenho,
        data=data,
        nota=nota,
        pessoa_id=pessoa_id
    )

    session.add(nova_nota)
    session.commit()

#função para listar nota atelie 
def listar_nota(session):
    return session.query(Nota_atelie).all()
        

#função para excluir nota atelie
def excluir_nota(session, id):
    nota = session.get(Nota_atelie, id)
        
    session.delete(nota)
    session.commit()
