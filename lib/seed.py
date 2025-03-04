from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Dev, Company, Freebie, Base  # Ensure you import Base for table creation

# Create an engine (modify the database URL as needed)
engine = create_engine('sqlite:///freebies.db')  # Or use another DB type

# Create session factory and initialize a session instance
Session = sessionmaker(bind=engine)
session = Session()  # This is the actual session object

# Ensure the database tables are created
Base.metadata.create_all(engine)

# Seed data
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")
company1 = Company(name="Google", founding_year=1998)
company2 = Company(name="Microsoft", founding_year=1975)

freebie1 = Freebie(item_name="T-Shirt", value=10, dev=dev1, company=company1)
freebie2 = Freebie(item_name="Mug", value=5, dev=dev2, company=company2)

# Add records to the session and commit
session.add_all([dev1, dev2, company1, company2, freebie1, freebie2])
session.commit()

print("Database seeded successfully!")
