from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource  
from models import db, Newsletter

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsletters.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)



class Home(Resource):
    def get(self):
        response = {
            "message": "Welcome to the Newsletter RESTful API",
        }
        response = make_response(
            response,
            200,
        )
        return response


#GET Method
class Newsletters(Resource):
    def get(self):
        newsletters = Newsletter.query.all()
        if newsletters:
            response_list = [n.to_dict() for n in newsletters]
            response = make_response(
                response_list,
                200,
            )
        else:
            response = make_response(
                jsonify({"message": "No newsletters found."}),
                404,
            )
        return response
    
#POST Method
    def post(self):
        data = request.get_json()
        if not data:
            response = make_response(
                jsonify({"message": "No data provided."}),
                400,
            )
            return response

        title = data.get('title')
        body = data.get('body')

        if not title or not body:
            response = make_response(
                jsonify({"message": "Title and body are required fields."}),
                400,
            )
            return response

        new_record = Newsletter(
            title=title,
            body=body,
        )
        db.session.add(new_record)
        db.session.commit()
        response = new_record.to_dict()
        response = make_response(
            response,
            201,
        )
        return response



class NewsletterByID(Resource):
#GET By ID
    def get(self, id):
        newsletter = Newsletter.query.filter_by(id=id).first()
        if newsletter:
            response = newsletter.to_dict()
            response = make_response(
                response,
                200,
            )
        else:
            response = make_response(
                jsonify({"message": f"Newsletter with id {id} not found."}),
                404,
            )
        return response

#PUT Method
    def put(self, id):
        newsletter = Newsletter.query.filter_by(id=id).first()
        if not newsletter:
            response = make_response(
                jsonify({"message": f"Newsletter with id {id} not found."}),
                404,
            )
            return response

        data = request.get_json()
        if not data:
            response = make_response(
                jsonify({"message": "No data provided."}),
                400,
            )
            return response

        title = data.get('title')
        body = data.get('body')

        if not title and not body:
            response = make_response(
                jsonify({"message": "At least one field (title or body) is required."}),
                400,
            )
            return response

        if title:
            newsletter.title = title
        if body:
            newsletter.body = body

        db.session.commit()
        response = newsletter.to_dict()
        response = make_response(
            response,
            200,
        )
        return response
    
#DELETE Method
    def delete(self, id):
        newsletter = Newsletter.query.filter_by(id=id).first()
        if not newsletter:
            response = make_response(
                jsonify({"message": f"Newsletter with id {id} not found."}),
                404,
            )
            return response

        db.session.delete(newsletter)
        db.session.commit()
        response = make_response(
            jsonify({"message": f"Newsletter with id {id} deleted."}),
            200,
        )
        return response

#HEADER-FILTER    
class NewspapersByHeader(Resource):
    def get(self):
        header_value = request.headers.get('Filter')
        if not header_value:
            response = make_response(
                jsonify({"message": "Missing 'Filter' header."}),
                400,
            )
            return response

        newsletters = Newsletter.query.filter(Newsletter.title.contains(header_value) | Newsletter.body.contains(header_value)).all()
        if newsletters:
            response_list = [n.to_dict() for n in newsletters]
            response = make_response(
                response_list,
                200,
            )
        else:
            response = make_response(
                jsonify({"message": f"No newsletters found for filter '{header_value}'."}),
                404,
            )
        return response


#Mapping resource classes  & URL endpoints for handling requests.
api.add_resource(Home, '/')
api.add_resource(Newsletters, '/newsletters')
api.add_resource(NewsletterByID, '/newsletters/<int:id>')
api.add_resource(NewspapersByHeader, '/newsletters/filter')


if __name__ == '__main__':
    app.run(port=5555, debug=True)

