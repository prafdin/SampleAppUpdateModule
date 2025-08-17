from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from .update_app import update_app

def check_event(github_payload):
    pass

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        payload = json.loads(post_data.decode('utf-8'))

        # Проверяем событие
        if check_event(payload):
            repo_path = payload.get('repository', {}).get('clone_url', '')
            commit_hash = payload.get('after', '')
            
            if repo_path and commit_hash:
                update_app(repo_path, commit_hash)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')


def main():
    """Entry point для консольной команды webhook-handler"""
    server = HTTPServer(('0.0.0.0', 8080), RequestHandler)
    print("Webhook handler started on port 8080")
    server.serve_forever()


if __name__ == '__main__':
    main()