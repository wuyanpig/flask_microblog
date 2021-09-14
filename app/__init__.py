from flask import Flask

app= Flask(__name__)

print('ttttttttttttttttttt:',__name__)


#放在下面，不放在开头，是为了避免循环引用
from app import routes
