# Frontend

## Запуск

Запуск решения ничем не отличается от запуска любого node.js приложения:
  - Вначале нужно установить все зависимости запустив `npm i`
  - Затем нужно заменить константу `API_URI` в файле `Search.jsx` на текущий адрес на котором работает backend сервис
  - В режиме разработки можно запустить с помощью команды `npm run start`
  - Во время развертки приложения на конечном сервере необходимо запустить `npm run build` и затем переместить статический сайт из папки `build` на конечный хостинг
