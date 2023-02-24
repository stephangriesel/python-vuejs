from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

# from flask import render_template
# import connexion

# app = connexion.App(__name__, specification_dir="./")
# app.add_api("swagger.yml")

app = Flask(__name__)
api = Api(app)

random_quotes = [
    {
        "id": 0,
        "author": "Unknown",
        "fact": "Avocados are a fruit, not a vegetable. They're technically considered a single-seeded berry, believe it or not."
    },
    {
        "id": 1,
        "author": "Unknown",
        "fact": "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion meaning the iron heats up, the particles gain kinetic energy and take up more space."
    },
    {
        "id": 2,
        "author": "Unknown",
        "fact": "Trypophobia is the fear of closely-packed holes. Or more specifically, an aversion to the sight of irregular patterns or clusters of small holes or bumps. No crumpets for them, then."
    },
    {
        "id": 3,
        "author": "Unknown",
        "fact": "Australia is wider than the moon. The moon sits at 3400km in diameter, while Australia's diameter from east to west is almost 4000km."
    },
    {
        "id": 4,
        "author": "Unknown",
        "fact": "Mellifluous is a sound that is pleasingly smooth and musical to hear."
    },
    {
        "id": 5,
        "author": "Unknown",
        "fact": "Human teeth are the only part of the body that cannot heal themselves. Teeth are coated in enamel which is not a living tissue."
    },
    {
        "id": 6,
        "author": "Unknown",
        "fact": "The Ancient Romans used to drop a piece of toast into their wine for good health - hence why we 'raise a toast'."
    },
]


class Quote(Resource):

    def get(self, id=0):
        if id == 0:
            return random.choice(random_quotes), 200

        for quote in random_quotes:
            if (quote["id"] == id):
                return quote, 200
        return "Quote not found", 404

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        params = parser.parse_args()

        for quote in random_quotes:
            if (id == quote["id"]):
                return f"Quote with id {id} already exists", 400

        quote = {
            "id": int(id),
            "author": params["author"],
            "quote": params["quote"]
        }

        random_quotes.append(quote)
        return quote, 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        params = parser.parse_args()

        for quote in random_quotes:
            if (id == quote["id"]):
                quote["author"] = params["author"]
                quote["quote"] = params["quote"]
                return quote, 200

        quote = {
            "id": id,
            "author": params["author"],
            "quote": params["quote"]
        }

        random_quotes.append(quote)
        return quote, 201

    def delete(self, id):
        global random_quotes
        random_quotes = [quote for quote in random_quotes if quote["id"] != id]
        return f"Quote with id {id} is deleted.", 200


api.add_resource(Quote, "/random-quotes", "/random-quotes/",
                 "/random-quotes/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)
