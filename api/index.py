from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import aielostora

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        q = query.get('q', [None])[0]
        m = query.get('m', ['1'])[0]
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        
        if not q:
            self.wfile.write("Error: ?q= is required".encode('utf-8'))
            return
            
        try:
            if m == "1":
                res = aielostora.gemini(q)
            else:
                res = aielostora.gpt3(q)
            self.wfile.write(str(res).encode('utf-8'))
        except Exception as e:
            self.wfile.write(f"Error: {str(e)}".encode('utf-8'))
