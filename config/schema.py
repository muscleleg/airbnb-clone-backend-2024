import strawberry


@strawberry.type()
class Query:

    def ping(self) -> str:
        return "pong"


schema = strawberry.Schema(query=Query)
