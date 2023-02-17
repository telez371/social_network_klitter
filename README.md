## Тестовое задание python backend developer

Написать серверную часть приложения для новостей

Бизнес постановка:
Необходимо создать сервисы позволящие каждому из пользователей создать свой канал с аватаркой, описанием и возможностью постить новости, получать подписчиков, ставить реации, комменты и ответы к ним. У заказчика уже есть вся информация о зарегистрированных пользователях.


## Решение


<p align="center">
     <a href="https://ibb.co/X8cm69k"><img src="https://i.ibb.co/4dhBCcg/Klitter-Logo-new.png" alt="Klitter-Logo-new" border="0"></a>
</p>


<p align="center">
   <img src="https://img.shields.io/badge/django-4.1.6-blueviolet" alt="django Version" >
   <img src="https://img.shields.io/badge/DRF-3.14.0-blue" alt="DRF Version">
   <img src="https://img.shields.io/badge/PostgreSQL-14-orange" alt="PostgreSQL Version">
   <img src="https://img.shields.io/badge/LICENSE-MIT-brightgreen" alt="License">
</p>

## Документация

swagger documentation.



Example Request

<pre>
<span class="key">/api/v1/swagger/</span>
</pre>

## Docker

<pre>
<span class="key">docker build --tag kliter .</span>
</pre>

<pre>
<span class="key">docker run -p 8080:80 -d kliter</span>
</pre>



## Физическая схема базы данных 


<p align="left">
     <a href="https://imgbb.com/"><img src="https://i.ibb.co/JdPP9Zw/bd-klitter.jpg" alt="bd-klitter" border="0"></a>
</p>
