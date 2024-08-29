# Исключения взяты из RFC 6749, раздел 4.2.2.1.

from urllib import parse

from pydantic import AnyUrl


class ProtoException(Exception):
    error: str
    description: str

    @classmethod
    def to_dict(cls):
        return {'error': cls.error, 'description': cls.description}


class InvalidClientMetadataException(ProtoException):
    error: str = "invalid_client_metadata"
    description: str = "Client metadata is invalid"


class InvalidResponseTypesException(InvalidClientMetadataException):
    description = "Provided \"response_types\" does not match \"grant_types\""


class NoRedirectURIsException(InvalidClientMetadataException):
    description = "\"redirect_uris\" must be provided if client use \"authorization_code\" or \"implicit\" grant type"


class PublicClientNotAllowedException(InvalidClientMetadataException):
    description = "Public clients are not allowed by authorization server's policiy"


class MultipleGrantTypesNotAllowedException(InvalidClientMetadataException):
    description = "Using multiple grant types is not allowed by authorization server's policiy"


class InvalidRedirectURI(InvalidClientMetadataException):
    description = "The value of one or more redirection URIs is invalid."


class InvalidMetadataURI(InvalidClientMetadataException):
    description = "Scheme and site of all URIs must be same with one of redirect URIs"


class SussySoftwareException(InvalidClientMetadataException):
    description = "Software version and/or software id are suspicious"


class NoInitialTokenException(ProtoException):
    error = "access_denied"
    description = "Initial token required"


class SoftwareStatementException(ProtoException):
    pass


class InvalidSoftwareStatement(SoftwareStatementException):
    error = "invalid_software_statement"
    description = "The software statement presented is invalid."


class UnapprovedSoftwareStatement(SoftwareStatementException):
    error = "unapproved_software_statement"
    description = "The software statement presented is not approved for use by this authorization server."


class BaseOauthError(Exception):
    status_code: int = 400
    error: str = "oauth_error"
    description: str = "Ошибка авторизации"


class AuthError(BaseOauthError):
    status_code = 302
    error = "auth_error"
    description = "Ошибка аутентификации"

    def __init__(self, redirect_uri: AnyUrl, state: str | None = None):
        self.redirect_uri = redirect_uri
        self.state = state

    async def get_redirect_uri(self):
        values = {
            'error': self.error,
            'description': self.description
        }
        if self.state:
            values['state'] = self.state

        return f"{self.redirect_uri}?{parse.urlencode(values)}"


class InvalidRequestError(AuthError):
    def __init__(self, redirect_uri: AnyUrl, state: str | None = None):
        self.redirect_uri = redirect_uri
        self.state = state
        self.error = "invalid_request"
        self.description = "The request is missing a required parameter, includes an " \
                           "invalid parameter value, includes a parameter more than " \
                           "once, or is otherwise malformed."


class UnauthorizedClientError(AuthError):
    def __init__(self, redirect_uri: AnyUrl, state: str | None = None):
        self.redirect_uri = redirect_uri
        self.state = state
        self.error = "unauthorized_client"
        self.description = "The client is not authorized to request an access token" \
                           "using this method."


class AccessDeniedError(AuthError):
    def __init__(self, redirect_uri: AnyUrl, state: str | None = None):
        self.redirect_uri = redirect_uri
        self.state = state
        self.error = "access_denied"
        self.description = "The resource owner or authorization server denied the request."


class UnsupportedResponseTypeError(AuthError):
    def __init__(self, redirect_uri: AnyUrl, state: str | None = None):
        self.redirect_uri = redirect_uri
        self.state = state
        self.error = "unsupported_response_type"
        self.description = "The authorization server does not support obtaining an access token using this method."


class InvalidScopeError(AuthError):
    def __init__(self, redirect_uri: AnyUrl, state: str | None = None):
        self.redirect_uri = redirect_uri
        self.state = state
        self.error = "invalid_scope"
        self.description = "The requested scope is invalid, unknown, or malformed."


class ServerError(AuthError):
    def __init__(self, redirect_uri: AnyUrl, state: str | None = None):
        self.redirect_uri = redirect_uri
        self.state = state
        self.error = "server_error"
        self.description = "The authorization server encountered an unexpected" \
                           "condition that prevented it from fulfilling the request."


class TemporarilyUnavailable(AuthError):
    def __init__(self, redirect_uri: AnyUrl, state: str | None = None):
        self.redirect_uri = redirect_uri
        self.state = state
        self.error = "temporarily_unavailable"
        self.description = "The authorization server is currently unable to handle" \
                           "the request due to a temporary overloading or maintenance" \
                           "of the server."


class TokenInvalidRequest(BaseOauthError):
    error = "invalid_request"
    description = "The request is missing a required parameter, includes an " \
                  "invalid parameter value, includes a parameter more than " \
                  "once, or is otherwise malformed."


class TokenUnauthorizedClient(BaseOauthError):
    error = "unauthorized_client"
    description = "The client is not authorized to request an access token" \
                  "using this method."


class TokenAccessDenied(BaseOauthError):
    error = "access_denied"
    description = "The resource owner or authorization server denied the request."
