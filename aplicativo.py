import os

# Código de autenticación Flutter
flutter_auth_code = """
# --- Archivo: login_screen.dart ---
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class LoginScreen extends StatefulWidget {
@override
_LoginScreenState createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
final TextEditingController emailController = TextEditingController();
final TextEditingController passwordController = TextEditingController();
String? errorMessage;

Future<void> login() async {
    final String email = emailController.text;
    final String password = passwordController.text;

    if (email.isEmpty || password.isEmpty) {
    setState(() {
        errorMessage = 'Por favor, ingresa correo y contraseña.';
    });
    return;
    }

    try {
    final response = await http.post(
        Uri.parse('http://<TU_BACKEND_URL>/api/auth/login'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'email': email, 'password': password}),
    );

    if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        final token = data['token'];

        // Guardar el token JWT
        // Aquí puedes usar paquetes como flutter_secure_storage para almacenar el token
        print('Token JWT: $token');

        setState(() {
        errorMessage = null;
        });

        // Navegar a la siguiente pantalla
        Navigator.pushReplacementNamed(context, '/home');
    } else {
        final errorData = jsonDecode(response.body);
        setState(() {
        errorMessage = errorData['message'] ?? 'Error en el inicio de sesión.';
        });
    }
    } catch (e) {
    setState(() {
        errorMessage = 'Error al conectar con el servidor.';
    });
    }
}

@override
Widget build(BuildContext context) {
    return Scaffold(
    appBar: AppBar(
        title: Text('Inicio de Sesión'),
    ),
    body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
            TextField(
            controller: emailController,
            decoration: InputDecoration(
                labelText: 'Correo Electrónico',
                border: OutlineInputBorder(),
            ),
            ),
            SizedBox(height: 20),
            TextField(
            controller: passwordController,
            decoration: InputDecoration(
                labelText: 'Contraseña',
                border: OutlineInputBorder(),
            ),
            obscureText: true,
            ),
            SizedBox(height: 20),
            if (errorMessage != null)
            Text(
                errorMessage!,
                style: TextStyle(color: Colors.red),
            ),
            SizedBox(height: 20),
            ElevatedButton(
            onPressed: login,
            child: Text('Iniciar Sesión'),
            ),
        ],
        ),
    ),
    );
}
}
"""

# Ruta donde se guardará el archivo
file_path = "/mnt/data/Flutter_Login_Auth_Setup.txt"

# Asegurarse de que el directorio existe
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# Guardar el archivo
try:
    with open(file_path, "w") as file:
        file.write(flutter_auth_code)
    print(f"Archivo guardado correctamente en: {file_path}")
except FileNotFoundError:
    print(f"No se pudo encontrar o crear el archivo en la ruta: {file_path}")
except Exception as e:
    print(f"Error inesperado: {e}")

