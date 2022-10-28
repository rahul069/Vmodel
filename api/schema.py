import graphene

from graphene_django import DjangoObjectType, DjangoListField
from .models import ModelUsers


class Users(DjangoObjectType):
    class Meta:
        model = ModelUsers
        fields = "__all__"


class Query(graphene.ObjectType):
    all_users = graphene.List(Users)
    book = graphene.Field(Users, user_id=graphene.Int())

    def resolve_all_users(self, info, **kwargs):
        return ModelUsers.objects.all()

    def resolve_user(self, info, user_id):
        return ModelUsers.objects.get(pk=user_id)


class UserInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()
    password = graphene.String()
    isActive = graphene.Boolean()
    created_on = graphene.Date()
    updated_on = graphene.Date()


class CreateUser(graphene.Mutation):
    class Arguments:
        user_data = UserInput(required=True)

    user = graphene.Field(Users)

    @staticmethod
    def mutate(root, info, user_data=None):
        user_instance = ModelUsers(
            name = user_data.name,
            email = user_data.email,
            password = user_data.password,
            isActive = user_data.isActive,
            created_on = user_data.created_on,
            updated_on = user_data.updated_on,
        )
        user_instance.save()
        return CreateUser(user=user_instance)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)


