from ninja import Schema


class HouseholdSchema(Schema):
    name: str


class MemberSchema(Schema):
    first_name: str
    last_name: str


class MonthlyBudgetSchema(Schema):
    label: str
    amount: float
