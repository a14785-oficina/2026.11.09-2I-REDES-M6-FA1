# Pedido Bruno: update-task

Ficheiro: [collections/Tarefas/update-task.bru](../../../collections/Tarefas/update-task.bru).

Este pedido exige o token colocado manualmente no cabeçalho Authorization, depois de Bearer e um espaço. Mantém o método e os campos do JSON de acordo com o recurso. Para um ID individual, substitui 1 pelo ID devolvido na criação. Os pedidos de login de A, B e admin servem para alternar a conta que estás a testar.

## Código desta versão

```bru
meta {
  name: update-task
  type: http
  seq: 9
}

put {
  url: http://127.0.0.1:5000/tarefas/1
  body: json
  auth: none
}

headers {
  Authorization: Bearer COLOCAR_TOKEN_AQUI
}

body:json {
  {
    "titulo": "Preparar apresentação",
    "descricao": "Conteúdos organizados.",
    "estado": "Em curso"
  }
}
```

[Voltar ao início](../../INICIO.md)
