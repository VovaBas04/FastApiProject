# FastApiProject
1) Установите python3.8
2) Для работы с базой данных выполнте установите psql(Postgres)
3) Создайте базу данных, для этого выполните sudo -u postgres psql
     2.1)  Выполните комманду CREATE DATABASE db
     2.2)  Выполните комманду CREATE USER user2 WITH PASSWORD 'password'
     2.3)  Выполните комманду ALTER ROLE user2 SET client_encoding TO 'utf8';
     2.4)  Выполните комманду ALTER ROLE user2 SET default_transaction_isolation TO 'read committed';
     2.5)  Выполните комманду ALTER ROLE user2 SET timezone TO 'UTC';
     2.6)  Выполните комманду GRANT ALL PRIVILEGES ON DATABASE db TO user2;
     2.7)  Выполните комманду \q
В корне проекта:
  1) Выполните комманду python3.8 -m venv venv
  2) Выполните комманду source venv/bin/activate
  3) Выполните комманду sudo apt install uvicorn
  4) Выполните pip install -r requirments.txt
  5) Перейдите в каталог menu коммандой cd menu
В папке menu:
  1) Для запуска сервера выполните uvicorn main:app --reload

