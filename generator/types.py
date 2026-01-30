from faker import Faker 
import random
from datetime import datetime 

faker = Faker()

def generate_value(col_type, config, used_value = None):
    if col_type == "int":
        return random.randint(
            config.get("min", 0),
            config.get("max", 10000)
        )
    
    if col_type == "full_name":
        return faker.name()

    if col_type == "email":
        return faker.unique.email()

    if col_type == "city":
        return faker.city()

    if col_type == "date":
        return faker.date_between(start_date = "-5y", end_date = "today")

    if col_type == "uuid":
        return faker.uuid4()

    if col_type == "boolena":
        return random.choice([True, False])

    return faker.word()