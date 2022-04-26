import os
import json
import urllib
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        fruit = self.request.get('fruitName')
        url = "https://fruityvice.com/api/fruit/"+ fruit
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        genus = data['genus']
        name = data['name']
        carbohydrates = data['nutritions']['carbohydrates']
        protein = data['nutritions']['protein']
        fat = data['nutritions']['fat']
        calories = data['nutritions']['calories']
        sugar = data['nutritions']['sugar']

        template_values = {
            "genus": genus,
            "name": name,
            "carbohydrates": carbohydrates,
            "protein": protein,
            "fat": fat,
            "calories": calories,
            "sugar": sugar,
        }
        path = os.path.join(os.path.dirname(__file__), 'results.html')
        self.response.out.write(template.render(path, template_values))
        
        
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
