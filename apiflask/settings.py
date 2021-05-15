import typing as t

from .schemas import http_error_schema
from .schemas import validation_error_schema
from .types import SchemaType
from .types import TagsType


# OpenAPI fields
OPENAPI_VERSION: str = '3.0.3'
DESCRIPTION: t.Optional[str] = None
TAGS: t.Optional[TagsType] = None
CONTACT: t.Optional[t.Dict[str, str]] = None
LICENSE: t.Optional[t.Dict[str, str]] = None
SERVERS: t.Optional[t.List[t.Dict[str, str]]] = None
EXTERNAL_DOCS: t.Optional[t.Dict[str, str]] = None
TERMS_OF_SERVICE: t.Optional[str] = None
YAML_SPEC_MIMETYPE: str = 'text/vnd.yaml'
JSON_SPEC_MIMETYPE: str = 'application/json'
# Automation behavior control
AUTO_TAGS: bool = True
AUTO_PATH_SUMMARY: bool = True
AUTO_PATH_DESCRIPTION: bool = True
AUTO_200_RESPONSE: bool = True
AUTO_VALIDATION_ERROR_RESPONSE: bool = True
AUTO_AUTH_ERROR_RESPONSE: bool = True
# Response customization
SUCCESS_DESCRIPTION: str = 'Successful response'
VALIDATION_ERROR_DESCRIPTION: str = 'Validation error'
AUTH_ERROR_DESCRIPTION: str = 'Authentication error'
VALIDATION_ERROR_STATUS_CODE: int = 400
AUTH_ERROR_STATUS_CODE: int = 401
VALIDATION_ERROR_SCHEMA: SchemaType = validation_error_schema
HTTP_ERROR_SCHEMA: SchemaType = http_error_schema
# Swagger UI and Redoc
DOCS_HIDE_BLUEPRINTS: t.List[str] = []
DOCS_FAVICON: t.Optional[str] = None
REDOC_USE_GOOGLE_FONT: bool = True
REDOC_STANDALONE_JS: str = 'https://cdn.jsdelivr.net/npm/redoc@next/bundles/\
redoc.standalone.js'
SWAGGER_UI_CSS: str = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist@3/swagger-ui.css'
SWAGGER_UI_BUNDLE_JS: str = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist@3/\
swagger-ui-bundle.js'
SWAGGER_UI_STANDALONE_PRESET_JS: str = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist@3/\
swagger-ui-standalone-preset.js'
SWAGGER_UI_LAYOUT: str = 'BaseLayout'
SWAGGER_UI_CONFIG: t.Optional[dict] = None
SWAGGER_UI_OAUTH_CONFIG: t.Optional[dict] = None
