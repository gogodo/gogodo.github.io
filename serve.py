from __future__ import annotations

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class Utf8SimpleHTTPRequestHandler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".css": "text/css; charset=utf-8",
        ".html": "text/html; charset=utf-8",
        ".js": "application/javascript; charset=utf-8",
        ".json": "application/json; charset=utf-8",
        ".md": "text/markdown; charset=utf-8",
        ".svg": "image/svg+xml; charset=utf-8",
    }


def main() -> None:
    host = ""
    port = 8000
    httpd = ThreadingHTTPServer((host, port), Utf8SimpleHTTPRequestHandler)
    print(f"Serving UTF-8 HTTP on port {port} (http://localhost:{port}/) ...")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
