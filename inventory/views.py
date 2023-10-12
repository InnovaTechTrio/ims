from django.shortcuts import render
from ariadne_django.views import GraphQLView
from .schema import schema

# Create your views here.
graphql_view = GraphQLView.as_view(schema=schema)