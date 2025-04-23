import firebase_admin
from firebase_admin import credentials, firestore
from ..utils.logging import get_logger

logger = get_logger(__name__)

def init_firebase():
    """
    Inicializa Firebase Admin SDK y retorna el cliente de Firestore.
    """
    if not firebase_admin._apps:
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred)
    return firestore.client()


def write_restaurant(db, restaurant_id: str, data: dict):
    """
    Escribe o actualiza un documento de restaurante en Firestore.
    """
    doc_ref = db.collection('restaurants').document(restaurant_id)
    doc_ref.set(data)
    logger.info(f"Stored restaurant {restaurant_id} in Firestore")