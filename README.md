# ДИПЛОМНЫЙ ПРОЕКТ  
## Сайт компании медицинской диагностики 'HealthChek'

### Инструкция по запуску

1. Клонируйте данный репозиторий на свой локальный компьютер

`git clone https://github.com/YuliyaArkhipova/Diploma_project`  

2. Установите виртуальное окружение

`python3 -m venv venv`

3. Активируйте виртуальное окружение
   
Windows: `venv\Scripts\activate`  
macOS и Linux: `source venv/bin/activate` 

4. Установите необходимые для работы библиотеки, указанные в requirements.txt
   
`python -m pip install -r requirements.txt`  

5. Заполните файл .env.exampl затем переименуйте его в .env   
   
6. Выполните команду для регистрации админа   

`python manage.py csu`
   
7. Создайте и примените миграции   

`python manage.py makemigrations`   
`python manage.py migrate`

9. Запустите приложение 

`python manage.py runserver`


### Для запуска проекта через Docker:

 `docker-compose up -d --build`

