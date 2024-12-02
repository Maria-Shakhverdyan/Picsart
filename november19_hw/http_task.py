from http.server import BaseHTTPRequestHandler, HTTPServer
import json

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Smartphone", "price": 500}
]

class RequestHandler(BaseHTTPRequestHandler):

    def _send_response(self, status_code, response_data):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        if response_data:
            self.wfile.write(json.dumps(response_data).encode('utf-8'))

    def _parse_id(self):
        parts = self.path.split('/')
        if len(parts) > 2 and parts[2].isdigit():
            return int(parts[2])
        return None

    # Handle GET requests
    def do_GET(self):
        if self.path.startswith('/users'):
            user_id = self._parse_id()
            if user_id:
                user = next((u for u in users if u["id"] == user_id), None)
                if user:
                    self._send_response(200, user)
                else:
                    self._send_response(404, {"error": "User not found"})
            else:
                self._send_response(200, users)

        elif self.path.startswith('/products'):
            product_id = self._parse_id()
            if product_id:
                product = next((p for p in products if p["id"] == product_id), None)
                if product:
                    self._send_response(200, product)
                else:
                    self._send_response(404, {"error": "Product not found"})
            else:
                self._send_response(200, products)
        else:
            self._send_response(404, {"error": "Endpoint not found"})

    # Handle POST requests
    def do_POST(self):
        if self.path.startswith('/users'):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            new_user = json.loads(post_data)
            new_user["id"] = max([u["id"] for u in users] + [0]) + 1
            users.append(new_user)
            self._send_response(201, new_user)

        elif self.path.startswith('/products'):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            new_product = json.loads(post_data)
            new_product["id"] = max([p["id"] for p in products] + [0]) + 1
            products.append(new_product)
            self._send_response(201, new_product)
        else:
            self._send_response(404, {"error": "Endpoint not found"})

    # Handle PUT requests
    def do_PUT(self):
        if self.path.startswith('/users'):
            user_id = self._parse_id()
            if user_id:
                user = next((u for u in users if u["id"] == user_id), None)
                if user:
                    content_length = int(self.headers['Content-Length'])
                    put_data = self.rfile.read(content_length)
                    updated_data = json.loads(put_data)
                    user.update(updated_data)
                    self._send_response(200, user)
                else:
                    self._send_response(404, {"error": "User not found"})
            else:
                self._send_response(400, {"error": "Invalid ID"})

        elif self.path.startswith('/products'):
            product_id = self._parse_id()
            if product_id:
                product = next((p for p in products if p["id"] == product_id), None)
                if product:
                    content_length = int(self.headers['Content-Length'])
                    put_data = self.rfile.read(content_length)
                    updated_data = json.loads(put_data)
                    product.update(updated_data)
                    self._send_response(200, product)
                else:
                    self._send_response(404, {"error": "Product not found"})
            else:
                self._send_response(400, {"error": "Invalid ID"})

    # Handle DELETE requests
    def do_DELETE(self):
        if self.path.startswith('/users'):
            user_id = self._parse_id()
            if user_id:
                global users
                users = [u for u in users if u["id"] != user_id]
                self._send_response(204, None)
            else:
                self._send_response(404, {"error": "User not found"})

        elif self.path.startswith('/products'):
            product_id = self._parse_id()
            if product_id:
                global products
                products = [p for p in products if p["id"] != product_id]
                self._send_response(204, None)
            else:
                self._send_response(404, {"error": "Product not found"})

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()