# deploy-template
For my dear friend

# Локально
## Запуск проекта
```commandline
docker compose -f docker-compose.yml -f docker-compose.override.yml up --build
```
## Остановка проекта
```commandline

docker compose -f docker-compose.yml -f docker-compose.override.yml down
```

# На сервере
## Запуск проекта
```commandline
docker compose -f docker-compose.yml -f docker-compose.production.yml up --remove-orphans -d
```

### Пере запуском добавить .env файл в корне проекта 
```commandline
BOT_TOKEN=my_very_secret_token
```


### Как добавить библиотеку
```commandline
1. поставить poetry
2. зайти в директорию ./backend
3. в файле pyproject.toml
добавить либу с версией с сайта (необязательно)
например:
requests = "2.27.*"
4. находясь в той же директории набрать команду 
poetry lock
(poetry надо видеть файл pyproject.toml)
```