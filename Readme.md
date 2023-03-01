## Skyentodo

Это веб-приложение — планировщик задач, который позволит работать с целями и
отслеживать прогресс по ним.

### Функционал:

1. Вход/регистрация/аутентификация через вк.
2. Создание целей.
- Выбор временного интервала цели с отображением кол-ва дней до завершения цели.
- Выбор категории цели (личные, работа, развитие, спорт и т. п.) с возможностью добавлять/удалять/обновлять категории.
- Выбор приоритета цели (статичный список minor, major, critical и т. п.).
- Выбор статуса выполнения цели (в работе, выполнен, просрочен, в архиве).
3. Изменение целей.
- Изменение описания цели.
- Изменение статуса.
- Дать возможность менять приоритет и категорию у цели.
4. Удаление цели.
- При удалении цель меняет статус на «в архиве».
5. Поиск по названию цели.
6. Фильтрация по статусу, категории, приоритету, году.
8. Заметки к целям.
9. Реализован телеграм-бот для связи с приложением.

### Стек:
python3.11, Django, DRF, Postgres

### Запуск:
Локально - в дирректории проекта выполнить команду:
docker-compose up

На сервере сборка и деплой осуществляются автоматически с помощью github actions
