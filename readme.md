# Поиск предприятий
Чтобы развернуть проект:
1. Устанавливаем репозиторий:
 - **git clone https://14bd02002@bitbucket.org/14bd02002/interprisenew.kz.git**
 - **cd interprises.test**
 - **composer install**
 - **npm install**
2. Редактируем .env файл (Если нет то создаем), настраиваем:
 - **DB_CONNECTION=mysql**  
 - **DB_HOST=127.0.0.1**  
 - **DB_PORT=3306**  
 - **DB_DATABASE=Ваша база данных**  
 - **DB_USERNAME=Логин**
 - **DB_PASSWORD=Пароль**
3.  Выполняем следующие команды:
 - **php artisan key:generate**  
 - **php artisan migrate**  
4. Обновить всю базу предприятий:
(При необходимости настроить конфиг БАЗЫ:
connect_timeout = 2000,
interactive_timeout=2000,
wait_timeout=1000)
 - **php artisan make:UpdateInterprises**  

