from flask import Flask

from app.posts.error_handlers import handle_bad_request, internal_server_error

# Импортируем блюпринты
from app.posts.views import posts_blueprint
from app.search.views import search_blueprint
from api.api import api_blueprint

# Создаем экземпляр Flask
app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

# Регистрируем блюпринты
app.register_blueprint(posts_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(api_blueprint)

# Регистрируем страницы ошибок
app.register_error_handler(404, handle_bad_request)
app.register_error_handler(500, internal_server_error)

# Запускаем сервер, только если файл запущен, а не импортирован
if __name__ == '__main__':
    app.run(port=8000)
