import logging
import os

from flask import Flask, request
from flask_login import LoginManager

from config import Config#从config模块导入Config类

from flask_sqlalchemy import SQLAlchemy#从包中导入类
from flask_migrate import Migrate
from logging.handlers import RotatingFileHandler
from flask_mail import Mail

from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel,lazy_gettext as _l
app = Flask(__name__)

babel = Babel(app)
app.config.from_object(Config)
moment = Moment(app)

db = SQLAlchemy(app)#数据库对象
migrate = Migrate(app, db)#迁移引擎对象
login = LoginManager(app)
login.login_view = 'login'
login.login_message = _l('Please log in to access this page.')
mail = Mail(app)
bootstrap = Bootstrap(app)

if not app.debug:
    # ...

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])
    # return 'zh_cn'

from app import routes,models,errors
#导入一个新模块models，它将定义数据库的结构，目前为止尚未编写
