from faker import Faker 
import random
from datetime import datetime 

from schemas.schema_models import ColumnType

faker = Faker()

def generate_value(col_type: ColumnType, config, used_value = None):
    if col_type == ColumnType.INT:
        min_val = config.get("min")
        max_val = config.get("max")

        if min_val is None :
            min_val = 0
        if max_val is None:
            max_val = 10000

        if min_val > max_val:
            raise ValueError(
                f"Invalid range for int column '{config.get('name')}': min ({min_val}) > max ({max_val})"
            )
        
        return random.randint(min_val, max_val)
        
    
    if col_type == ColumnType.FULL_NAME:
        return faker.name()

    if col_type == ColumnType.FIRST_NAME:
        return faker.first_name()

    if col_type == ColumnType.LAST_NAME:
        return faker.last_name()

    if col_type == ColumnType.USER_NAME:
        return faker.user_name()
    
    if col_type == ColumnType.PHONE:
        return faker.phone_number()

    if col_type == ColumnType.ADDRESS:
        return faker.address()

    if col_type == ColumnType.COUNTRY:
        return faker.country()

    if col_type == ColumnType.ZIP_CODE:
        return faker.zipcode()
    
    if col_type == ColumnType.URL:
        return faker.url()

    if col_type == ColumnType.COMPANY:
        return faker.company()
    
    if col_type == ColumnType.TEXT:
        return faker.text()

    if col_type == ColumnType.PARAGRAPH:
        return faker.paragraph()

    if col_type == ColumnType.EMAIL:
        return faker.unique.email()

    if col_type == ColumnType.CITY:
        return faker.city()

    if col_type == ColumnType.DATE:
        return faker.date_between(start_date = "-5y", end_date = "today")

    if col_type == ColumnType.UUID:
        return faker.uuid4()

    if col_type == ColumnType.BOOLEAN:
        return random.choice([True, False])

    return faker.word()