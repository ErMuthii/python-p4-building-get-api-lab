from random import randint
from faker import Faker
from app import app
from models import db, Bakery, BakedGood

fake = Faker()

with app.app_context():
    db.drop_all()
    db.create_all()

    print("Seeding database ...")
    BakedGood.query.delete()
    Bakery.query.delete()

    # Generate bakeries
    bakery_names = ['Sweet Treats Bakery', 'Delicious Delights', 'Bakery Bliss', 'The Pastry Shop', 'Gourmet Bakery']
    bakeries = [Bakery(name=name) for name in bakery_names]
    db.session.add_all(bakeries)
    db.session.commit()

    # Generate baked goods
    for bakery in bakeries:
        for _ in range(3):  # Let's keep 3 baked goods per bakery
            name = fake.word().capitalize()
            price = round(randint(100, 1000) / 100, 2)  # Random price between 1.00 and 10.00
            baked_good = BakedGood(name=name, price=price, bakery=bakery)
            db.session.add(baked_good)
    db.session.commit()

    print("Database seeded successfully!")
