# faativ
repositório av5 prog

comandos ultilizados

Obs: a pasta ja estava salva no computador onde foi tirado os prints, por isso não ha fotos do git clone.

1. "git clone https://github.com/issfalkk/faativ.git" clonar repositório;

2. "cd faativ" entrar na pasta pelo terminal;

4. "dir" verificar os arquivos na pasta;

5. "uv init" adiciona arquivos como pyproject.toml e uv.lock;

6. "uv add sqlachemy pymsql python-dotenv" instala o sqlachemy, pymsql e python-dotenv pro arquivo .env;

7. "uv python list" lista versões do python pelo uv para instalar;

8. "uv python pin 3.13" defini o python 3.13 como versão do projeto;

9. "Get-Content pyproject.toml" mostra o que tem dentro do arquivo. A mudança de versão deu erro porque nesse arquivo estava "requiest-python>=3.14", impedindo a mudança. Então pelo vscode, essa linha foi trocada por "requiest-python>=3.13";

10. "uv sync --python 3.13" sincroniza o ambiente virtual;

11. "uv run python --version" mostra a versão do Python utilizada pelo ambiente executado pelo uv. Foi usado para confirmar que a configuração da versão 3.13 havia funcionado;

12. "uv run menu.py" erro relacionado ao carregamento de um módulo do SQLAlchemy. Para investigar o problema, foram utilizados os seguintes comandos:
    " uv run python -c "import sqlalchemy; print(sqlalchemy.__version__)" "  importa a biblioteca SQLAlchemy e exibe sua versão instalada
    
    " uv run python -c "from sqlalchemy.orm import Session; print('SQLAlchemy OK')" " verifica se é possível importar a classe Session, utilizada para gerenciar as sessões de interação com o banco de dados por meio do SQLAlchemy;

13. "uv run menu.py" funcionou apenas com o banco de dados SQLite. Ocorreu um erro relacionado com a URL do banco.
    
    No arquivo banco.py, a função responsável pela conexão com o banco de dados MySql foi alterada;

14. "uv run menu.py" inicia o programa;

15. Consulta ao MySql:

 Para o MySql, foi criado um banco de dados local no meu computador(Isadora Falk), por isso no arquivo .env, tem as informações do meu banco de dados. Para criar e consultar o banco, foram utilizados estes comandos:
    "create database atelie;" Diferente do SQLite que é direto no vscode, o Mysql precisa ser criado o banco antes para criar uma conexão com o engine.

    "show database atelite" para conferir se o banco foi criado

    "use atelie;

    show tables:" para ver as tabelas criadas

    "use atelie;

    select * from pessoas_atelie;" para ver os dados da tabela pessoas

    "use atelie;

    select * from notas_atelie;" para ver os dados da tabela notas

16. Parte final:
    "git status" consulta quais arquivos foram modificados;
    "git add ." adiciona as alterações para serem incluidas no commit
    "git commit -m "mensagem"" registra as alterações preparadas em um commit;
    "git push" envia os commits locais ao repositório.