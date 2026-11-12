# API de Gestão de Tarefas

## Como Executar

Extrair para uma pasta nova. Esta revisão usa uma base nova e não migra bases de dados ou passwords de outra versão. O código está em models/user.py, models/task.py, resources/user.py e resources/task.py.

Windows, no terminal da pasta que contém app.py:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Linux / Codespaces:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python app.py
```

O arranque é `python app.py`, como no original. Na primeira execução, cria automaticamente instance/tarefas.db, as tabelas Utilizador e Tarefa e um administrador. A rota `/` não existe. No Codespaces, usar/encaminhar a porta 5000.

Administrador inicial de demonstração: **admin@exemplo.pt / Admin123!**. O arranque não duplica o administrador quando a aplicação reinicia.

## Como testar no Bruno

Abrir collections/Tarefas. Os pedidos usam URLs diretos, meta, body:json e headers como no formato do original. Se estiveres no Codespaces, substitui http://127.0.0.1:5000 pelo endereço encaminhado nos pedidos.

1. Enviar insert-user-a e insert-user-b para criar duas contas comuns.
2. Enviar login-user-a e copiar apenas o valor de access_token.
3. Nos pedidos de tarefas, substituir COLOCAR_TOKEN_AQUI pelo token, mantendo Bearer e um espaço.
4. Enviar insert-task, com titulo, descricao e estado. Guardar o ID devolvido; se não for 1, trocar esse ID nos pedidos individuais.
5. Listar e atualizar a tarefa de A. No PUT enviar os três campos, como no parser da API Hotel.
6. Fazer login como B e trocar o token: não deve conseguir consultar, alterar ou eliminar a tarefa de A.
7. Fazer login como admin e trocar o token: deve conseguir todas essas operações.

O token é colocado manualmente no cabeçalho de cada pedido, sem scripts ou variáveis de ambiente do Bruno. O pedido login-admin é uma alternativa aos logins dos utilizadores; não é necessário executá-los todos antes de criar uma tarefa.

## Endpoints

| Método | Rota | Resultado |
| --- | --- | --- |
| POST | /registo | Recebe username, email e password; cria utilizador comum com 201. Email repetido ou tentativa de enviar tipo dá 400. |
| POST | /login | Recebe email e password; devolve access_token com ID e tipo. Credenciais erradas dão 401. |
| POST | /tarefas | Cria com 201; o proprietário vem do utilizador autenticado. |
| GET | /tarefas | Admin consulta todas; utilizador consulta apenas as próprias. |
| GET | /tarefas/1 | Consulta individual: 200, 403 ou 404. |
| PUT | /tarefas/1 | Altera uma tarefa existente com os três campos; não cria um ID ausente. |
| DELETE | /tarefas/1 | Elimina com 200; sem permissão dá 403, ausente dá 404. |
| POST | /logout | Extra já presente no original: revoga o token atual e devolve 200. |

Todos os endpoints de tarefas exigem JWT. Titulo, descricao e estado são obrigatórios no POST e PUT. Null é rejeitado. Os estados permitidos são exatamente Pendente, Em curso e Concluída. O título não pode ser vazio. Enviar utilizador_id no JSON é rejeitado: a atribuição é feita pelo servidor. Estas escolhas de validação completam os detalhes não especificados pelo enunciado.