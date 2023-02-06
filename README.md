# infra_sp2
## О проекте api_yamdb:
- проект предназначен для формирования отзывов и рейтинга объектов широкого круга интересов пользователей. Например, к указанным объектам
могут окносится литературные произведения, произведения кинематографа и театра, продукты гейминдустрии, хобби пользоватлей, марки автомобильных брендов, мобильные телефоны и т.п. Список круга интересов пользователей может быть продолжен по их просьбе с
участием администратора форума. На каждое произведение выставляется рейтинг - что определяет его общественное признание. Взаимодействие
пользоватлей с инструментарием проекта осуществляется посредством API. В задачи проекта входит: сохранение контента загруженного пользователем; предоставление по запросу требуемой информации; возможность комментирования контента другими пользователями; возможность полного или частичного изменения контента автором(модератором); удаление информации автором(модератором);
- проект отличается высокой мобильностью и "развертываемостью";
- основой проекта является веб-фраемворки Django и Django REST Framework;
- Авторы проекта: Родион Прошляков(proshlyakovrodion@yandex.ru), Марк Зотов(zotov001@yandex.ru), Павел Новиков(pasha.n2006@yandex.ru)
## Создайте файл .env с переменными окружения в директории infra:
Шаблон наполнения env-файла
```
SECRET_KEY=some-kind-of-key # установите ваш секретный ключ 
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```
## Описание команд для запуска приложения в контейнерах
- Перейдите в директорию с файлом docker-compose.yaml
```
cd infra/
```
- Соберите контейнеры и запустите их
```
docker-compose up -d --build 
```
- Выполните по очереди команды
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```
- Основной функционал готов, чтобы остановить и удалить контейнеры выполните команду
```
docker-compose down -v
```
## Описание команд для заполнения базы данными
- Перейдите в директорию с файлом fixtures.json
```
cd infra/
```
- Скопируйте файл fixtures.json внутрь контейнера web
```
docker cp fixtures.json <CONTAINER>:/app
```
- Выполните команду для заполнения базы данными
```
docker-compose exec web python manage.py loaddata fixtures.json
```
## Работа с API
Получить список всех категорий
```
http://localhost/api/v1/categories/
```
Получить список всех жанров
```
http://localhost/api/v1/genres/
```
Получить список всех обьектов
```
http://localhost/api/v1/titles/
```
Получить список всех отзывов
```
http://localhost/api/v1/titles/{title_id}/reviews/
```
Комментарии к отзывам
```
http://localhost/api/v1/titles/{title_id}/reviews/{review_id}/comments/
```
Получить список всех пользователей(доступно администратору)
```
http://localhost/api/v1/users/
```
Добавить нового пользователя(доступно администратору)
```
http://localhost/api/v1/users/
```
Самостоятельная регистрация на форуме пользователем. Получение JWT-токена.
```
-http://localhost/api/v1/auth/signup/
```
```
-http://localhost/api/v1/auth/token/
```
