from sqlalchemy import create_engine, String, Integer, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

#duas classes com 4 atributos cada, com relacionamento 1 pra N

#Pessoa que participa do atelie de desenho
class Pessoa_atelie(Base):
    __tablename__ = "pessoas_atelie"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    turma: Mapped[str] = mapped_column(String(20), nullable=False)
    curso: Mapped[str] = mapped_column(String(100), nullable=False)

    #uma pessoa pode ter várias notas
    notas: Mapped[list["Nota_atelie"]] = relationship(
        back_populates="aluno"
    )


class Nota_atelie(Base):
    __tablename__ = "notas_atelie"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    desenho: Mapped[str] = mapped_column(String(200), nullable=False)
    data: Mapped[str] = mapped_column(String(10), nullable=False)
    nota: Mapped[float] = mapped_column(Float, nullable=False)

    #chave estrangeira de Pessoa_atelie
    pessoa_id: Mapped[int] = mapped_column(
        ForeignKey("pessoas_atelie.id"),
        nullable=False
    )

    #cada nota pertence a uma pessoa
    aluno: Mapped["Pessoa_atelie"] = relationship(
        back_populates="notas"
    )
