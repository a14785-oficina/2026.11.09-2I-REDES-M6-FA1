# Pedido Bruno: login-admin

Ficheiro: [collections/Tarefas/login-admin.bru](../../../collections/Tarefas/login-admin.bru).

Este pedido de registo/login não precisa de JWT. Mantém o método e os campos do JSON de acordo com o recurso. Para um ID individual, substitui 1 pelo ID devolvido na criação. Os pedidos de login de A, B e admin servem para alternar a conta que estás a testar.

## Código desta versão

```bru
meta {
  name: login-admin
  type: http
  seq: 5
}

post {
  url: http://127.0.0.1:5000/login
  body: json
  auth: none
}

body:json {
  {
    "email": "admin@exemplo.pt",
    "password": "Admin123!"
  }
}
```

[Voltar ao início](../../INICIO.md)
