# Webhook App Updater

Пакет для автоматического обновления приложений через webhooks.

## Установка

```bash
pip install -e .
```

## Использование

### Запуск webhook handler

```bash
webhook-handler
```

Сервер запустится на порту 8080 и будет слушать POST запросы.

### Ручное обновление приложения

```bash
update-app <repo_url> <commit_hash>
```

## Структура проекта

```
webhook-app-updater/
├── setup.py
├── requirements.txt
├── README.md
└── webhook_app_updater/
    ├── __init__.py
    ├── webhook_handler.py
    └── update_app.py
```

## API

### Webhook события

Сервер принимает POST запросы с JSON payload, содержащим:
- `ref` - ветка (обрабатывается только `refs/heads/main`)
- `repository.clone_url` - URL репозитория
- `after` - хеш коммита