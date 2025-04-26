# 📚 Proyecto: Autenticación Básica con Flask

Este proyecto implementa una autenticación básica utilizando **Flask** y **Flask-Login**, como parte de la actividad de la lección.

Tecnologías utilizadas: Python, Flask, Flask-Login, Bootstrap 5, Jinja2.

## 🛠️ Funcionalidades principales

- Autenticación de usuarios usando `username` y `password`.
- Contraseñas almacenadas de forma **segura** usando **hash** (`generate_password_hash`).
- Gestión de sesión con **Flask-Login**.
- Rutas protegidas que sólo permiten acceso a usuarios autenticados.
- Mensajes de error amigables cuando se ingresan credenciales incorrectas.
- Roles o permisos para los usuarios (`admin`, `user`).

---

## 🧩 Esquema de Usuario

Cada usuario incluye:
- **Nombre de usuario**: el identificador principal (ej. `"admin"`, `"user"`).
- **Contraseña (Hash)**: contraseñas no se guardan en texto plano, sino en hash seguro.
- **Rol o permiso**: define el nivel de acceso (ej. `"admin"`, `"user"`).

```python
users = {
    "admin": {
        "password": generate_password_hash("adminpass"),
        "role": "admin"
    },
    "user": {
        "password": generate_password_hash("userpass"),
        "role": "user"
    }
}
```
---
## 🧪 Flujo del programa

![image](https://github.com/user-attachments/assets/0bf1a1d5-7171-4341-b02d-12a1c6bc4671)

## 📸 Pantallas 

### Index 
Muestra área para iniciar sesión 

![image](https://github.com/user-attachments/assets/92d93df4-0d7e-4cdd-98f5-df03ea1aa560)

### Login
Donde se ingresan las credenciales de usuario y contraseña 
![image](https://github.com/user-attachments/assets/680ae26b-16c3-4f07-9cef-f6cc55124f82)
![image](https://github.com/user-attachments/assets/0215a745-c84d-4994-b9e6-d0f9cd4fa33b)

### Mensaje de error 
Muestra cuando las credenciales son incorrectas
![image](https://github.com/user-attachments/assets/7f78ecd5-190c-4b79-8f22-fa5962a310e4)


### Dashboard 
Las credenciales son correctas y se redirige a dashboard. Presenta el nombre rol, y botón para cerrar la sesión.
![image](https://github.com/user-attachments/assets/0dc0d151-516f-4169-ad65-06f5bc9869c9)

### Password Hashing
![image](https://github.com/user-attachments/assets/bae2da84-3f30-4cc1-89d6-9e184b50f98c)
