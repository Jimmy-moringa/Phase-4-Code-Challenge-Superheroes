from app import app
from models import db, Hero, Power

with app.app_context():
    db.create_all()

    hero1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    hero2 = Hero(name="Doreen Green", super_name="Squirrel Girl")
    power1 = Power(name="Super Strength", description="gives the wielder super-human strengths")
    power2 = Power(name="Flight", description="gives the wielder the ability to fly")

    db.session.add_all([hero1, hero2, power1, power2])
    db.session.commit()
