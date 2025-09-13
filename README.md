# ScriptJWT

## 📖 Descripción  
Este proyecto implementa un script que genera y valida **JSON Web Tokens (JWT)** firmado con una clave secreta.  
El JWT incluye datos académicos básicos: **número de carnet, nombre completo, curso y sección**.  
El token se configura con un vencimiento muy corto para permitir pruebas en diferentes escenarios:  
- Validación con la clave correcta  
- Validación con clave incorrecta  
- Validación después de que el token haya expirado  

---

## ✍️ Autor  
- **Nombre:** Axel Omar Santizo
- **Carnet:** 1990-21-1683

---

## ⚙️ Funcionalidades  
1. Generar un JWT firmado con clave secreta.  
2. Decodificar y mostrar la información almacenada en el JWT.  
3. Validar el JWT correctamente usando la clave secreta.  
4. Intentar validar el JWT con una clave secreta incorrecta.  
5. Validar el JWT después de su vencimiento.  

---

## 🛠️ Tecnologías  
- Lenguaje de programación: **Python 3.11**  
- Librería principal: **PyJWT** (para generación y validación de JWT)  
- Entorno de ejecución: **Consola o terminal en Windows/Linux/MacOS**  

---

## ▶️ Ejecución  
Clonar el repositorio desde GitHub:  
```bash
`git clone https://github.com/Santizo00/ScriptJWT.git`  
```

Instalar dependencias necesarias:  
```bash
`pip install pyjwt`  
```

Ejecutar el script con Python:  
```bash
`python script_jwt.py`
```  

Ejecutar el script con el lenguaje configurado.  

La salida esperada incluye:  
- Información del JWT válido con la clave correcta  
- Error al validar con clave incorrecta  
- Error al validar cuando el token haya expirado  

**Ejemplo de datos impresos en la salida:**  
- Carnet: 202012345  
- Nombre: Juan Pérez Monzón  
- Curso: Programación Web  
- Sección: A  

---

## 📌 Notas  
Este proyecto se desarrolló con fines académicos para comprender el uso de **JWT**, su seguridad y la importancia de la expiración en sistemas de autenticación.
