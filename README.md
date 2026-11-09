# Exercicios Docker - Orion Bootcamp

## Estrutura
- docker/exercicio-1 - Hello Container com Python + Compose
- docker/exercicio-2 - API + Postgres com volume e persistencia
- docker/exercicio-3 - Dev/Prod com docker-compose.dev.yml e docker-compose.prod.yml
- docker/exercicio-extra - API + Postgres + Adminer com /health, .env e healthcheck

## Como rodar
cd docker/exercicio-extra
docker compose up --build -d
# API: http://localhost:3000
# Health: http://localhost:3000/health
# Adminer: http://localhost:8080 (Servidor: db, Usuario: postgres, Senha: postgres)