from jose import jwk


def try_to_construct_jwk(jwk_dict: dict) -> dict:
    jwk.construct(jwk_dict)
    return jwk_dict
