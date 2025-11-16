# Домашнее задание к занятию "`Резервное копирование`" - `Найден Александр`

## Задание 1

```bash
# Создание резервной копии домашней директории
rsync -avc --delete --exclude='.*/' $HOME/ /tmp/backup/
```

####

![Screenshot](static/images/screenshot-1.png)


## Задание 2

![Screenshot](static/images/screenshot-2.png)

####

- Файл [crontab](crontab)

####

- Файл [backup_script.sh](backup_script.sh)
