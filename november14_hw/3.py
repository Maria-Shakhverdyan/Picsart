from http.server import BaseHTTPRequestHandler, HTTPServer
import json

users = []

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            user_data = json.loads(post_data)
            users.append(user_data)
            
            response = {
                "message": "User data added successfully",
                "user_data": user_data,
                "all_users": users
            }
            self.send_response(200)
        except json.JSONDecodeError:
            response = {"error": "Invalid JSON"}
            self.send_response(400)
        
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = {"message": "List of users", "users": users}
        self.wfile.write(json.dumps(response).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting HTTP server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
