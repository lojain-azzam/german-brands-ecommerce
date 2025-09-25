#!/usr/bin/env python3
"""
Simple HTTP server to run the German Brands PRD showcase locally
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

# Configuration
PORT = 8000
HOST = 'localhost'

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow local file access
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

def main():
    # Change to the directory containing the HTML file
    os.chdir(Path(__file__).parent)
    
    print("🇩🇪 German Brands PRD Showcase Server")
    print("=" * 50)
    print(f"Starting server on http://{HOST}:{PORT}")
    print("Press Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        with socketserver.TCPServer((HOST, PORT), CustomHTTPRequestHandler) as httpd:
            # Automatically open browser
            webbrowser.open(f'http://{HOST}:{PORT}')
            print(f"🌐 Opening browser to http://{HOST}:{PORT}")
            print("✨ Your 3D PRD showcase is now running!")
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {PORT} is already in use. Trying port {PORT + 1}...")
            try:
                with socketserver.TCPServer((HOST, PORT + 1), CustomHTTPRequestHandler) as httpd:
                    webbrowser.open(f'http://{HOST}:{PORT + 1}')
                    print(f"🌐 Opening browser to http://{HOST}:{PORT + 1}")
                    print("✨ Your 3D PRD showcase is now running!")
                    httpd.serve_forever()
            except OSError:
                print(f"❌ Could not start server. Please try a different port or stop other servers.")
                sys.exit(1)
        else:
            print(f"❌ Error starting server: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()
