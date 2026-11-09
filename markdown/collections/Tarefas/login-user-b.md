# Pedido Bruno: login-user-b

Ficheiro: [collections/Tarefas/login-user-b.bru](../../../collections/Tarefas/login-user-b.bru).

Este pedido de registo/login não precisa de JWT. Mantém o método e os campos do JSON de acordo com o recurso. Para um ID individual, substitui 1 pelo ID devolvido na criação. Os pedidos de login de A, B e admin servem para alternar a conta que estás a testar.

## Código desta versão

```bru
meta {
  name: login-user-b
  type: http
  seq: 4
}

post {
  url: http://127.0.0.1:5000/login
  body: json
  auth: none
}

body:json {
  {
    "email": "b@exemplo.pt",
    "password": "AlunoB123!"
  }
}
```

[Voltar ao início](../../INICIO.md)
