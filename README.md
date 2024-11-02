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

### Настройка сервера для Github Actions
```commandline

1. Настроить сервак по инструкции как тут
    https://hostgeek.ru/manuals/49-nachalnaja-nastrojka-servera-ubuntu-2004.html
2. Далее будет инструкция, если вы добавили пользователя safeuser
3. Дать новому пользователю safeuser sudo права
    sudo usermod -aG sudo newuser
4. Зайти под новым юзером на сервак
5. Создаем раннер в настройках проекта Actions/Runner
6. Настроить раннер по инструкции из разделов Установка и Автозапуск
    https://blog.bissquit.com/unix/ustanovka-github-runner/#note-6758-4
7. Поставить Docker на сервер
    - создаем файл на серваке install_docker.sh

        sudo apt install apt-transport-https ca-certificates curl software-properties-common
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
        sudo add-apt-repository -y "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
        sudo apt-get install -y docker-ce docker-ce-cli containerd.io
        sudo systemctl start docker
        sudo systemctl enable docker
        sudo usermod -aG docker $USER
        exit 0

    - запускаем скрипт bash install_docker.sh
8. Даем sudo права для Docker
    sudo usermod -a -G docker <USER>
9. Перезапустить runner
    sudo ./svc.sh stop
    sudo ./svc.sh start
10. В корне репозитория проекта создаем директорию .github/workflows
    - добавляем файл main.yml
11. В настройках проекта в разделе Secrets and Variables/Actions/ в Variables 
12. При новых коммитах в ветку master (см. .github/workflows/master.yml on:push:branches:- master) будет происходить деплой
13. Поздравляю, вы великолепны!
```