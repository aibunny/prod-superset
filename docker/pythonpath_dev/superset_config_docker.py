SUPERSET_SECRET_KEY="$(openssl rand -base64 42)"
SECRET_KEY="$(openssl rand -base64 42)"

SQLALCHEMY_ECHO = True

ROW_LIMIT = 5000



FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True
}

TALISMAN_ENABLED =False


