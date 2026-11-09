# Pedido Bruno: insert-user-b

Ficheiro: [collections/Tarefas/insert-user-b.bru](../../../collections/Tarefas/insert-user-b.bru).

Este pedido de registo/login não precisa de JWT. Mantém o método e os campos do JSON de acordo com o recurso. Para um ID individual, substitui 1 pelo ID devolvido na criação. Os pedidos de login de A, B e admin servem para alternar a conta que estás a testar.

## Código desta versão

```bru
meta {
  name: insert-user-b
  type: http
  seq: 2
}

post {
  url: http://127.0.0.1:5000/registo
  body: json
  auth: none
}

body:json {
  {
    "username": "alunoB",
    "email": "b@exemplo.pt",
    "password": "AlunoB123!"
  }
}
```

[Voltar ao início](../../INICIO.md)
