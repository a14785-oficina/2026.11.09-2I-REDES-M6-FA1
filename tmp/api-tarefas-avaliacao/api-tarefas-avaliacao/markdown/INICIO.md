# Adaptação conservadora da API Hotel para Gestão de Tarefas

## Ordem de leitura

1. con_sql.py e os dois modelos: comparar UserModel e TaskModel com o código de aula.
2. resources/user.py: registar e fazer login por email.
3. resources/task.py: seguir um pedido até ao modelo e reconhecer onde são verificadas as permissões.
4. app.py: ligar as rotas e criar o administrador na primeira execução.
5. Pedidos Bruno: usar contas A, B e admin para confirmar os acessos.

## Espelho dos ficheiros

| Ficheiro | Guia |
| --- | --- |
| `.gitignore` | [.gitignore.md](.gitignore.md) |
| `README.md` | [README.md](README.md) |
| `app.py` | [app.md](app.md) |
| `blocklist.py` | [blocklist.md](blocklist.md) |
| `collections/Tarefas/bruno.json` | [collections/Tarefas/bruno.md](collections/Tarefas/bruno.md) |
| `collections/Tarefas/collection.bru` | [collections/Tarefas/collection.md](collections/Tarefas/collection.md) |
| `collections/Tarefas/delete-task.bru` | [collections/Tarefas/delete-task.md](collections/Tarefas/delete-task.md) |
| `collections/Tarefas/insert-task.bru` | [collections/Tarefas/insert-task.md](collections/Tarefas/insert-task.md) |
| `collections/Tarefas/insert-user-a.bru` | [collections/Tarefas/insert-user-a.md](collections/Tarefas/insert-user-a.md) |
| `collections/Tarefas/insert-user-b.bru` | [collections/Tarefas/insert-user-b.md](collections/Tarefas/insert-user-b.md) |
| `collections/Tarefas/list-task.bru` | [collections/Tarefas/list-task.md](collections/Tarefas/list-task.md) |
| `collections/Tarefas/list-tasks.bru` | [collections/Tarefas/list-tasks.md](collections/Tarefas/list-tasks.md) |
| `collections/Tarefas/login-admin.bru` | [collections/Tarefas/login-admin.md](collections/Tarefas/login-admin.md) |
| `collections/Tarefas/login-user-a.bru` | [collections/Tarefas/login-user-a.md](collections/Tarefas/login-user-a.md) |
| `collections/Tarefas/login-user-b.bru` | [collections/Tarefas/login-user-b.md](collections/Tarefas/login-user-b.md) |
| `collections/Tarefas/logout.bru` | [collections/Tarefas/logout.md](collections/Tarefas/logout.md) |
| `collections/Tarefas/update-task.bru` | [collections/Tarefas/update-task.md](collections/Tarefas/update-task.md) |
| `con_sql.py` | [con_sql.md](con_sql.md) |
| `models/task.py` | [models/task.md](models/task.md) |
| `models/user.py` | [models/user.md](models/user.md) |
| `requirements.txt` | [requirements.md](requirements.md) |
| `resources/task.py` | [resources/task.md](resources/task.md) |
| `resources/user.py` | [resources/user.md](resources/user.md) |

Os guias espelham os ficheiros do projeto; os documentos INICIO, COMPARACAO-ORIGINAL e VERIFICACAO são adicionais. Não se cria um espelho recursivo da própria pasta markdown.

## Ciclo de avaliação

- Registar A e B; ambos ficam como utilizador. Repetir email deve dar 400. Tentar enviar tipo=admin deve dar 400.
- Fazer login como A, copiar o token para os cabeçalhos e criar uma tarefa com os três campos: 201. O ID e o proprietário são atribuídos pelo servidor.
- Fazer GET /tarefas como A: vê apenas as suas. GET/PUT/DELETE da própria tarefa funcionam.
- Trocar para o token de B: não vê a tarefa de A na lista; GET/PUT/DELETE desse ID dão 403.
- Trocar para o token do admin: vê todas e consegue consultar/alterar/eliminar a tarefa alheia.
- Sem token: os cinco endpoints de tarefas dão 401.
- ID inexistente: GET/PUT/DELETE dão 404. PUT não cria um ID ausente.
- Título vazio, campo em falta, null, estado inválido ou tentativa de enviar utilizador_id: 400.
- Após reinício, os registos SQL continuam presentes e o admin não é duplicado.

## Como explicar o acesso

O JWT identifica o utilizador. O método carrega essa conta da base. Se for admin, permite o acesso a qualquer tarefa. Se não for, compara task_found.utilizador_id com user.id. No POST, o novo objeto recebe user.id diretamente; o cliente nunca escolhe o proprietário.

As verificações repetidas nos métodos são deliberadas: seguem o estilo de procura, condições e retorno do original, sem criar uma camada auxiliar nova. O enunciado obriga a acrescentar estas condições mesmo numa adaptação conservadora.
