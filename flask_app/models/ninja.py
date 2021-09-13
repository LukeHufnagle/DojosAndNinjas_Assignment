from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja: 
    def __init__(self, data):
        self.id = data['id']

        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.dojo = {}

#=============================================
# Create Ninja query
#=============================================
    @classmethod
    def create_ninja(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(age)s, %(dojo_id)s, NOW(), NOW());'
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return results