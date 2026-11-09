# Tokens revogados

Ficheiro: [blocklist.py](../blocklist.py).

É exatamente o set do original. O logout guarda jti; o callback JWT consulta esse identificador. O conjunto não persiste após reinício.

## Código desta versão

```python
BLOCKLIST = set() # A python set to store the JWT tokens that have been revoked or blacklisted.
```

[Voltar ao início](INICIO.md)
