from app import db
from models import Hero, Power

def seed_data():
    h1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    h2 = Hero(name="Doreen Green", super_name="Squirrel Girl")
    p1 = Power(name="super strength", description="gives the wielder super-human strengths")
    p2 = Power(name="flight", description="gives the wielder the ability to fly")

    db.session.add_all([h1, h2, p1, p2])
    db.session.commit()

if __name__ == '__main__':
    seed_data()
