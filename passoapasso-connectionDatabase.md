## CONFIGURAÇÃO PARA CONEXÃO DO BANCO DE DADOS

### Criação do banco dados na plataforma
1. Abrir o prompt e digitar comando de exportação usando o comando **pg_dump**:
```
pg_dump -U nomeusuario -h localhost -p 5432 -d nomebanco -f "c:\caminho\para\o\arquivo\database.sql"
```
2. Digite a senha

3. Importar o arquivo.sql para o banco de dados na plataforma (lembre-se de já ter criado o banco de dados primeiro na render,pois irá precisar das informações criadas no 'external database url'), usando o comando **psql**:
```
psql -h <host_do_render> -U <usuario_do_render> -d <banco_de_dados_no_render> -f "c:\caminho\para\o\arquivo.sql"
```

4. Digite a senha

### Deploy do sistema

1. Depois de fazer a importação insira a URL external e ponha na variavel de ambiente no momento do deploy do sistema, ex:
```
postgresql://usuario:password@host-name/nome-do-banco
```
2. Altere o seu arquivo database de coneção com o banco local, para que ele possa usar a variavel de ambiente. Exemplo em python:
```python
import psycopg2
import os

def get_db_connection():
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise ValueError("DATABASE_URL environment variable is not set.")
    banco = psycopg2.connect(database_url)
    return banco
```

3. Por fim faça o deploy do sistema



