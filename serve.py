#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys

# Muda para o diretório dist
os.chdir('dist')

PORT = 8080

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.send_header('X-Frame-Options', 'ALLOWALL')
        super().end_headers()

    def do_GET(self):
        # Para SPAs, redireciona todas as rotas para index.html
        if not os.path.exists(self.path[1:]) and not self.path.startswith('/assets'):
            self.path = '/index.html'
        return super().do_GET()

with socketserver.TCPServer(("0.0.0.0", PORT), MyHTTPRequestHandler) as httpd:
    print(f"Servidor rodando na porta {PORT}")
    print(f"Acesse: http://localhost:{PORT}")
    httpd.serve_forever()