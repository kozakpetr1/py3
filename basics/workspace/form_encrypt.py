from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from cryptography.fernet import Fernet

# Generate or use a predefined key for encryption/decryption
KEY = Fernet.generate_key()
cipher_suite = Fernet(KEY)

# HTML content for the login page
html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}
        .login-container {{
            background: #ffffff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 300px;
        }}
        .login-container h1 {{
            text-align: center;
            margin-bottom: 20px;
        }}
        .login-container input {{
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 3px;
        }}
        .login-container button {{
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }}
        .login-container button:hover {{
            background-color: #0056b3;
        }}
    </style>
    <script>
        async function encryptAndSubmit(event) {{
            event.preventDefault();
            const form = event.target;
            const username = form.username.value;
            const password = form.password.value;

            // Encrypt the data using the key
            const encryptedData = btoa(encodeURIComponent(username + ":" + password));
            const formData = new FormData();
            formData.append("data", encryptedData);

            // Send the encrypted data
            const response = await fetch("/", {{
                method: "POST",
                body: formData
            }});
            const result = await response.text();
            document.body.innerHTML = result;
        }}
    </script>
</head>
<body>
    <div class="login-container">
        <h1>Login</h1>
        <form onsubmit="encryptAndSubmit(event)">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>
"""

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Respond to a GET request with the login page
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html_content.encode("utf-8"))

    def do_POST(self):
        # Handle form submission (decrypt the received data)
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("utf-8")
        form_data = parse_qs(post_data)
        encrypted_data = form_data.get("data", [None])[0]
        if encrypted_data:
            decrypted_data = cipher_suite.decrypt(encrypted_data.encode("utf-8"))
            username, password = decrypted_data.decode("utf-8").split(":")
            print(f"Decrypted username: {username}, password: {password}")

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>Login data received and decrypted. Check the server console for details.</h1>")
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"<h1>Invalid data received.</h1>")

# Define and run the server
def run_server():
    server_address = ('', 8080)  # Listen on all interfaces, port 8080
    httpd = HTTPServer(server_address, RequestHandler)
    print("Server running on http://localhost:8080")
    print(f"Encryption Key (keep this safe): {KEY.decode()}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
