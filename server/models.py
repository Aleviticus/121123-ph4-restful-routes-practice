from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Traveler(db.Model):
    pass

    # ATTRIBUTES #

    # id - Integer
    # name - String - required
    # age - Integer
    # budget - Integer
    # frequent_flyer - Boolean

    __tablenmae__ = "traveler_table"

    id = db.Column ( db.Integer, primary_key = True)
    name = db.Column ( db.String, unique =True )
    age = db.Column ( db.Integer )
    budget = db.Column ( db.Integer )
    frequent_flyer = db.Column ( db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "budget": self.budget,
            "frequent_flyer": self.frequent_flyer
        }

class Island(db.Model):
    pass

    # ATTRIBUTES #

    # id - Integer
    # name - String - required and unique
    # square_miles - Integer
    # average_temperature - Integer

    __tablename__ = "island_table"

    id = db.Column ( db.Integer, primary_key = True )
    name = db.Column ( db.String, unique = True )
    square_miles = db.Column ( db.Integer ) 
    average_temperature = db.Column ( db.Integer )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "square_miles": self.square_miles,
            "average_temperature": self.average_temperature
        }