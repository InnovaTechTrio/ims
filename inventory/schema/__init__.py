from ariadne import make_executable_schema, load_schema_from_path
import os
from .query import query


query_type_defs = load_schema_from_path("inventory/schema/query/query.graphql")



type_defs = query_type_defs


# Create the executable schema
schema = make_executable_schema(type_defs,query)