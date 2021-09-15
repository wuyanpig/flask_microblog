from flask import Flask
from config import Config#从config模块导入Config类

app = Flask(__name__)
app.config.from_object(Config)

#放在下面，不放在开头，是为了避免循环引用
from app import routes
