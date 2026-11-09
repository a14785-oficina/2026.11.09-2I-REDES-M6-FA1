# Pedido Bruno: list-tasks

Ficheiro: [collections/Tarefas/list-tasks.bru](../../../collections/Tarefas/list-tasks.bru).

Este pedido exige o token colocado manualmente no cabeçalho Authorization, depois de Bearer e um espaço. Mantém o método e os campos do JSON de acordo com o recurso. Para um ID individual, substitui 1 pelo ID devolvido na criação. Os pedidos de login de A, B e admin servem para alternar a conta que estás a testar.

## Código desta versão

```bru
meta {
  name: list-tasks
  type: http
  seq: 7
}

get {
  url: http://127.0.0.1:5000/tarefas
  body: none
  auth: none
}

headers {
  Authorization: Bearer COLOCAR_TOKEN_AQUI
}
```

[Voltar ao início](../../INICIO.md)
