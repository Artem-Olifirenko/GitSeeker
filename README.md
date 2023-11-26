# GitSeeker

GitSeeker – это скрипт на Python, предназначенный для поиска репозиториев на GitHub. Он использует GitHub API для получения информации о репозиториях, соответствующих заданным критериям поиска.

## Особенности

- Поиск репозиториев по ключевым словам.
- Аутентификация с использованием персонального токена доступа.
- Поддержка постраничного вывода результатов.
- Легко расширяемый для дополнительных функций поиска.

## Начало работы

### Предварительные требования

Перед использованием скрипта убедитесь, что у вас установлен Python и библиотека `requests`. Вы можете установить `requests` с помощью следующей команды:

```bash
pip install requests
```

### Установка

Клонируйте репозиторий с помощью Git:

```bash
git clone https://github.com/your-username/GitSeeker.git
cd GitSeeker
```

### Настройка

Для использования скрипта необходимо установить переменную окружения `GITHUB_ACCESS_TOKEN`:

```bash
export GITHUB_ACCESS_TOKEN=your_github_access_token
```

### Использование

Чтобы запустить скрипт, используйте следующую команду:

```bash
python main.py "поисковый_запрос" [количество_результатов_на_странице] [номер_страницы]
```

## Лицензия

Этот проект распространяется под BSD-3-Clause License - см. [LICENSE](LICENSE) файл для подробностей.
