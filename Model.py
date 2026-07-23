from peewee import SqliteDatabase , Model , CharField , IntegerField , ForeignKeyField

db = SqliteDatabase("ali.db")


class BaseModel(Model):
    class Meta:
        database = db


class Cook(BaseModel):
    cook_name = CharField()
    cook_family = CharField()


class Chef(BaseModel):
    chef_name = CharField()
    chef_family = CharField()


class Food(BaseModel):
    food_name = CharField()


class Customer(BaseModel):
    customer_name = CharField()
    customer_family = CharField()


class CookingStaff(BaseModel):
    chef = ForeignKeyField(
        Chef,
        backref="cooking_staffs",
        on_delete="CASCADE"
    )

    cook = ForeignKeyField(
        Cook,
        backref="cooking_staffs",
        on_delete="CASCADE"
    )

    class Meta:
        indexes = (
            (("chef", "cook"), True),
        )


class Order(BaseModel):
    customer = ForeignKeyField(
        Customer,
        backref="orders",
        on_delete="CASCADE"
    )

    food = ForeignKeyField(
        Food,
        backref="orders",
        on_delete="CASCADE"
    )

    class Meta:
        indexes = (
            (("customer", "food"), True),
        )


class OrderComplete(BaseModel):
    cooking_staff = ForeignKeyField(
        CookingStaff,
        backref="completed_orders",
        on_delete="CASCADE"
    )

    order = ForeignKeyField(
        Order,
        backref="completion",
        unique=True,
        on_delete="CASCADE"
    )

db.connect()

db.create_tables([
    Cook,
    Chef,
    Food,
    Customer,
    CookingStaff,
    Order,
    OrderComplete
])

