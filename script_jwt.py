import jwt
import time
from jwt import ExpiredSignatureError, InvalidTokenError

# ==========================
# Datos del estudiante
# ==========================
payload = {
    "carnet": "1990-21-1683",
    "nombre": "Axel Omar Santizo",
    "curso": "Seguridad Auditoría de Sistemas",
    "exp": int(time.time()) + 5  # Token expira en 5 segundos
}

# Clave secreta correcta
SECRET_KEY = "12345abcde"

# Clave secreta incorrecta
WRONG_SECRET_KEY = "54321edcba"

print("\n=== Generando JWT ===")
token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print("JWT generado:", token)

# ==========================
# Validación con clave correcta
# ==========================
print("\n=== Validación con clave correcta ===")
try:
    decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    print("JWT válido ✅")
    print("Contenido:", decoded)
except InvalidTokenError as e:
    print("Error:", str(e))

# ==========================
# Validación con clave incorrecta
# ==========================
print("\n=== Validación con clave incorrecta ===")
try:
    decoded = jwt.decode(token, WRONG_SECRET_KEY, algorithms=["HS256"])
    print("JWT válido (esto no debería pasar) ❌")
except InvalidTokenError as e:
    print("Error al validar con clave incorrecta:", str(e))

# ==========================
# Esperar a que expire
# ==========================
print("\n=== Esperando a que el token expire (6 segundos) ===")
time.sleep(6)

print("\n=== Validación después de expirar ===")
try:
    decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    print("JWT válido (esto no debería pasar) ❌")
except ExpiredSignatureError:
    print("Error: el token ha expirado ⏰")
except InvalidTokenError as e:
    print("Error:", str(e))
