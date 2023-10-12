from ariadne import QueryType

query = QueryType()


@query.field("getName")
def resolve_get_name(*_,):
    return "Bob"