# Pedido Bruno: logout

Ficheiro: [collections/Tarefas/logout.bru](../../../collections/Tarefas/logout.bru).

Este pedido exige o token colocado manualmente no cabeçalho Authorization, depois de Bearer e um espaço. Mantém o método e os campos do JSON de acordo com o recurso. Para um ID individual, substitui 1 pelo ID devolvido na criação. Os pedidos de login de A, B e admin servem para alternar a conta que estás a testar.

## Código desta versão

```bru
meta {
  name: logout
  type: http
  seq: 11
}

post {
  url: http://127.0.0.1:5000/logout
  body: none
  auth: none
}

headers {
  Authorization: Bearer COLOCAR_TOKEN_AQUI
}
```

[Voltar ao início](../../INICIO.md)
