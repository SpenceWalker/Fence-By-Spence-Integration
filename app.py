from flask import Flask
from views import views

app = Flask(__name__)

app.register_blueprint(views, url_prefix="/views")

#True is capatilzied in the following statement to indicate its a set boolean -- lower case would be a variable // value
if __name__ == '__main__':
    app.run(debug=True, port=8080)
