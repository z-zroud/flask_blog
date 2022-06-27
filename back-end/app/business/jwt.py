from datetime import datetime, timedelta
import jwt
import logging


JWT_KEY = 'JWT_KEY_IS_HARD_TO_GUESS'

logger = logging.getLogger()

def generate_jwt(user_id, username, expires_in=3600):
    now = datetime.utcnow()
    payload = {
        'user_id': user_id,
        'user_name': username,
        'exp': now + timedelta(seconds=expires_in),
        'iat': now
    }
    return jwt.encode(payload, JWT_KEY, algorithm='HS256')



def verify_jwt(token):
    try:
        payload = jwt.decode(token, JWT_KEY, algorithms=['HS256'])
    except (jwt.exceptions.ExpiredSignatureError, jwt.exceptions.InvalidSignatureError, jwt.exceptions.DecodeError) as e:
        logger.error(f"validate token failed. {e.args}")
        return None
    return payload.get('user_id')