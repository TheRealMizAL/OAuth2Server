from typing import Annotated

from pydantic import AnyUrl, UrlConstraints

HttpsUrl = Annotated[AnyUrl, UrlConstraints(max_length=2083, allowed_schemes=["https"])]
