1) Запуск всего проекта через докер (у меня проект запускается, но не удается в браузере открыть ссылку).
  cd redis_web
  docker-compose build
  docker-compose up
2) Запуск django без докера (redis уже запущен через docker-compose)
  ./script.sh
