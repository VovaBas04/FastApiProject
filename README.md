# FastApiProject
<pre>
1) Установите python3.8
2) Для работы с базой данных выполнте установите psql(Postgres)
3) Создайте базу данных, для этого выполните sudo -u postgres psql<br>
     3.1)  Выполните комманду CREATE DATABASE db; <br>
     3.2)  Выполните комманду CREATE USER user2 WITH PASSWORD 'password;' <br>
     3.3)  Выполните комманду ALTER ROLE user2 SET client_encoding TO 'utf8'; <br>
     3.4)  Выполните комманду ALTER ROLE user2 SET default_transaction_isolation TO 'read committed';<br>
     3.5)  Выполните комманду ALTER ROLE user2 SET timezone TO 'UTC';<br>
     3.6)  Выполните комманду GRANT ALL PRIVILEGES ON DATABASE db TO user2;<br>
     3.7)  Выполните комманду \q <br>
4)В корне проекта:
  1) Выполните комманду python3.8 -m venv venv
  2) Выполните комманду source venv/bin/activate
  3) Выполните комманду sudo apt install uvicorn
  4) Выполните pip install -r requirments.txt
  5) Перейдите в каталог menu коммандой cd menu
5)В папке menu:
  1) Для запуска сервера выполните uvicorn main:app --reload

</pre>
