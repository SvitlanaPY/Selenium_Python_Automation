"""
Добавление изменений на сервер (push)
Сейчас у вашего репозитория есть две разные копии — одна локальная, которая уже содержит изменения в файле,
и удаленная — на гитхабе.
Необходимо наши локальные коммиты положить в удаленный репозиторий.
Для этого есть специальная команда git push <репозиторий><название ветки>.

Сейчас мы не будем вдаваться подробно в тему ветвления.
Достаточно знать, что основная ветка, на которой вы находитесь по умолчанию — это master.
Мы будем пушить в удаленный репозиторий origin — оригинальный репозиторий,
откуда мы скопировали к себе на компьютер локальную версию.
Обратите внимание, что основная ветка в репозитории будет называться master, если он был создан до осени 2020 года.
Увидеть это можно в Git Bash после перехода в папку проекта.
s3_lesson1_master_branch.jpg

В репозитиориях, которые были созданы позднее, основная ветка по умолчанию может называться main.
s3_lesson1_main_branch.jpg

Выполним команду:
git push origin master

Или git push origin main для новых репозиториев.
Git попросит ввести ваш логин и пароль на GitHub, и покажет примерно следующее:
s3_lesson1_push_statistics.png

Теперь откройте свой репозиторий на гитхабе в браузере.
Если вы все сделали правильно, то гитхаб подтянет описание проекта из файла и красиво отобразит на страничке:
GitHub_projects.png

Обратите внимание, что рядом с файлом появилась дополнительная информация:
когда файл был последний раз модифицирован и какое было сообщение у этого коммита.

Можно, например, кликнуть на сообщение коммита и посмотреть, какие были изменения:
s3_lesson1_GitHub__SeeCommitChanges.png

Зеленые строки — это те, которые добавились, а красные — те, которые были удалены.
Вот и все, вы молодец!
"""