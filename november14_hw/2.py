from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def extract_query_params(self, url_path):
        query_params = {}
        if '?' in url_path:
            _, query = url_path.split('?', 1)
            pairs = query.split('&')
            for pair in pairs:
                if '=' in pair:
                    key, value = pair.split('=', 1)
                    query_params[key] = value
        return query_params
    
    def do_GET(self):
        query_params = self.extract_query_params(self.path)

        email = query_params.get('email', 'Not provided')

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {"message": "GET request received", "email": email, "all_params": query_params}
        self.wfile.write(json.dumps(response).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting HTTP server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
