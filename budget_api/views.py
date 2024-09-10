from django.contrib.auth.models import User

from auth_api.shemas import MessageSchema
from auth_api.token import AuthBearer
from budget_api.models import Household, Member, MonthlyBudget
from budget_api.schemas import HouseholdSchema, MemberSchema, MonthlyBudgetSchema
from budget_demo.urls import api


@api.post("/households/", response={201: HouseholdSchema}, tags=["Household"])
def create_household(request, payload: HouseholdSchema):
    household = Household.objects.create(**payload.dict())

    return 201, household


@api.post("/members/", response={201: MemberSchema}, auth=AuthBearer(), tags=["Member"])
def create_member(request, payload: MemberSchema):
    user = User.objects.get(username=request.auth.username)
    member = Member.objects.create(**payload.dict(), user=user)

    return 201, member


@api.post(
    "/monthly_budgets/",
    response={201: MonthlyBudgetSchema},
    auth=AuthBearer(),
    tags=["Monthly Budget"],
)
def create_monthly_budget(request, payload: MonthlyBudgetSchema):
    user = User.objects.get(username=request.auth.username)
    member = Member.objects.get(user=user)
    monthly_budget = MonthlyBudget.objects.create(**payload.dict(), member=member)

    return 201, monthly_budget


@api.patch(
    "/households/join/{household_id}",
    response={200: MessageSchema},
    auth=AuthBearer(),
    tags=["Household"],
)
def join_household(request, household_id: int):
    user = User.objects.get(username=request.auth.username)
    member = Member.objects.get(user=user)
    member.household_id = household_id
    member.save()

    return 200, MessageSchema(message="Member joined household")


@api.get(
    "/monthly_budgets/",
    response={200: list[MonthlyBudgetSchema]},
    auth=AuthBearer(),
    tags=["Monthly Budget"],
)
def get_monthly_budgets(request):
    user = User.objects.get(username=request.auth.username)
    member = Member.objects.get(user=user)
    monthly_budgets = MonthlyBudget.objects.filter(member=member)

    return 200, monthly_budgets
