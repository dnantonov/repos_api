### Сервис должен уметь:

- Выгружать данные о репозиториях через https://docs.github.com/en/rest/reference/repos.  
- Сохранить их в базе. 
- Предоставлять API с CRUD методами для работы c этими данным посредством REST.  
- Предоставлять веб-интерфейс для просмотра данных в браузере.

### Запуск проекта:

Для запуска проекта клонируем репоизиторий через терминал:

`git clone https://github.com/dnantonov/repos_api/ && cd repos_api`

Далее запускаем проект в Docker-контейнере:

`docker-compose build && docker-compose up`

### Endpoints

Получение репозиториев конкретного пользователя. http://0.0.0.0:8000/api/<str:username>/.  
Метод: GET

Получение первых 50-ти репозиториев. http://0.0.0.0:8000/api/repos/.  
Метод: GET

Получение информации о репозитории по id. http://0.0.0.0:8000/api/get-repository/<int:pk>/.  
Метод: GET

Создание нового репозитория. http://0.0.0.0:8000/api/create-repository/.  
Метод: POST

Данные передаем в формате JSON в следующем виде:
```json
{
        "id": 3617322281,
        "node_id": "MFFwOlJlcG9zaXRvcnkx",
        "name": "test_rep",
        "full_name": "mojombo/test_repo",
        "private": false,
        "html_url": "https://github.com/mojombo/test_repo",
        "description": "**Test description.",
        "owner": 46
}
```

Обновление данных репозитория. http://0.0.0.0:8000/api/update-repository/<int:pk>/.  
Метод: POST

Данные передаем в формате JSON в следующем виде:
```json
{
    "id": 1,
    "node_id": "OlJlcG9zaXRvcnkxTT",
    "name": "grit-updated",
    "full_name": "mojombo/grit-updated",
    "private": false,
    "html_url": "https://github.com/mojombo/grit-updated",
    "description": "Updated description.",
    "owner": 46
}
```

Удаление репозитория по id. http://127.0.0.1:8000/api/delete-repository/<int:pk>/.  
Метод: DELETE
