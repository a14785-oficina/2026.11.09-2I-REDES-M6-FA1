# Relação com o export original

Fonte: api-hotel.7z, SHA-256 54c8c28cb1354c419c87cce8cdae1eab09cbb053d3970bb065b27f73d66b391e. Foram relidos os sete ficheiros Python e os pedidos do export; os 18 ficheiros de projeto foram novamente confrontados com os bytes do arquivo. O original não foi alterado.

| Original | Adaptação conservadora |
| --- | --- |
| con_sql.py: bd = SQLAlchemy() | Mesmo ficheiro, byte a byte. |
| blocklist.py: BLOCKLIST = set() | Mesmo ficheiro, byte a byte. |
| app.py com Flask, Api, JWTManager e add_resource | Mantém esse arranque, configuração direta e callbacks JWT. |
| Inicialização SQL em if __name__ == __main__ | Mantida; nesse contexto foi acrescentada a criação inicial do admin exigida. |
| models/user.py: UserModel e métodos de instância | Mantém classe, construtor, json(), find_user() e save_user(); acrescenta email, tipo e consulta por ID. |
| models/hotel.py: HotelModel | models/task.py: TaskModel, mantendo construtor, json(), find/save/update/delete e commit. |
| resources/user.py: UserRegister/UserLogin/UserLogout | Mesmas classes, args de reqparse e comparação hmac. Login corrigido e adaptado a email. |
| resources/hotel.py: Hotels/Hotel | resources/task.py: Tasks/Task; POST passa para a coleção /tarefas porque o ID é automático. |
| Parser args dentro de Hotel | Parser args dentro de Task, partilhado com o POST de Tasks; sem parser global ou função genérica de leitura. |
| Métodos com procura, if, retorno e persistência | Verificações diretas nos métodos, incluindo permissões e proprietário. |
| GET de hotéis público | GET de tarefas exige JWT e filtra os registos, como obriga o enunciado. |
| user_id String autoincremental | id Integer autoincremental; correção exigida pelo esquema e por SQLite. |
| Campos próprios de Hotel | Campos de Tarefa e chave estrangeira para Utilizador; relação de um para muitos. |
| PUT com erros value(), objeto novo duplicado e lista antiga | Atualiza a instância encontrada; ID ausente devolve 404, sem criar tarefa. |
| Return de login fora do método e create_acess_token | Indentação e nomes corrigidos; credenciais inválidas devolvem 401. |
| Criação devolvia 200 | 201 nos registos e tarefas, conforme os estados pedidos no enunciado. |
| JSON do utilizador devolvia password | Password retirada das respostas; mantém-se a comparação ensinada, destinada a contas fictícias. |
| Bruno com URL literal e corpo JSON | Mesmo formato, com cabeçalho Bearer explícito nos pedidos protegidos. |

A adaptação acrescenta apenas a lógica necessária para este domínio e os requisitos indicados. Logout permanece como funcionalidade adicional do original, mas não substitui qualquer requisito da avaliação. Não foram acrescentados papéis além de admin e utilizador, factories, ficheiros de configuração por ambiente, parsing manual de JSON ou helpers genéricos de acesso.

Em relação ao ZIP anterior desta conversa, os ficheiros passam dos nomes utilizador/tarefa para user/task, de acordo com o estilo do export. O PUT exige os três campos completos; a inicialização volta a __main__; as passwords seguem o formato de exercício original. Não mistures os ficheiros nem a base de dados das duas revisões.
