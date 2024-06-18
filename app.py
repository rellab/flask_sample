from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# サンプルのリソースを作成
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

# エンドポイントを設定
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
