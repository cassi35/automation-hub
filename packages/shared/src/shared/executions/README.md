# objetivo

essa camada é a parte aonde vou abrir uma threading paralelo para inserção no banco de dados para tirar acoplamento e resolver problema de latencia I/O

# estrtura

```
main
 │
 ├── queue.put(finish_execution)
 │
 └── processo termina
       ↓
     thread daemon morre
       ↓
     evento não chegou no backend
```
