# miron1126 Flash Lab

Игра про прошивку и ремонт телефонов. Сайт: https://miron11265282.github.io/FlashLab-Miron1126/

## Как выложить (один раз)
1. Создай публичный репозиторий **FlashLab_Miron1126** на GitHub и загрузи в него всё из этой папки (папки `docs`, `app`, `ios`, `.github` и этот файл).
   Проще всего — через GitHub Desktop или командой `git push`. Через сайт папку `.github` можно загрузить перетаскиванием всей папки.
2. **Settings → Pages → Branch: main, папка /docs → Save.** Через минуту сайт заработает.
3. **Releases → Draft a new release → тег `v6.0.0`.** Прикрепи файлы игры (лимит GitHub — 2 ГБ на файл):
   `FlashLab-6.0.0-Setup-x64.exe`, `FlashLab-6.0.0-Setup-arm64.exe`, `FlashLab-6.0.0-android.apk` и `FlashLab-web.zip` (веб-версия). Нажми **Publish**.
4. После публикации релиза GitHub сам запустит сборку (вкладка **Actions**, ~15 минут) и добавит в релиз
   `.dmg` для Mac, `.ipa` для iPhone, `.AppImage` и `.deb` для Linux. Кнопки на странице «Скачать» сразу начнут работать.

## iPhone
`.ipa` без подписи Apple. Установи через **AltStore** или **Sideloadly** со своим Apple ID (бесплатно; переподписывать раз в 7 дней).
## Mac
Приложение не подписано. Первый запуск: правый клик по приложению → «Открыть» → «Открыть».
