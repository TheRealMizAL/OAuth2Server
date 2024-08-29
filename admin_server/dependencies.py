async def pagination(q: int = 10, start: int = 0, limit: int = 10):
    return {"q": q, "start": start, "limit": limit}


class Pagination:
    def __init__(self, start: int = 0, limit: int = 10):
        self.start = start
        self.limit = limit
