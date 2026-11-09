# Ligação SQLAlchemy

Ficheiro: [con_sql.py](../con_sql.py).

É exatamente o mesmo ficheiro do export. Os modelos importam este objeto, e app.py inicializa-o. Não é necessária uma ligação diferente por tabela.

## Código desta versão

```python
from flask_sqlalchemy import SQLAlchemy

bd = SQLAlchemy()
```

[Voltar ao início](INICIO.md)
