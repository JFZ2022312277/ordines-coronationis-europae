#!/usr/bin/env python3
"""
Local HTTP server for Ordines Coronationis Europae.

This project is a static web application. Because it loads data files via
fetch(), it MUST be served over HTTP(S) — opening index.html directly with
file:/// will produce an apparently empty map and an empty ego-network.

USAGE
-----
    python serve.py

then open the URL printed in the terminal (defaults to http://localhost:8765/).

Press Ctrl+C to stop.

If port 8765 is busy:
    python serve.py 9000          # or any other free port

This script has no third-party dependencies; the Python 3 standard library
is enough.
"""

from __future__ import annotations
import http.server
import os
import socketserver
import sys
import webbrowser
from pathlib import Path


def main() -> int:
    port = 8765
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"Bad port: {sys.argv[1]!r}", file=sys.stderr)
            return 2

    here = Path(__file__).resolve().parent
    os.chdir(here)

    handler = http.server.SimpleHTTPRequestHandler
    # Allow same-origin requests even when the site is served from localhost
    # under a non-default port.
    handler.extensions_map = {
        **handler.extensions_map,
        ".geojson": "application/geo+json",
        ".cff":     "text/yaml; charset=utf-8",
        ".md":      "text/markdown; charset=utf-8",
        ".xml":     "application/xml; charset=utf-8",
        ".tei":     "application/xml; charset=utf-8",
    }

    with socketserver.TCPServer(("127.0.0.1", port), handler) as httpd:
        url = f"http://localhost:{port}/index.html"
        print()
        print(f"  Ordines Coronationis Europae — local preview")
        print(f"  Serving:  {here}")
        print(f"  URL:      {url}")
        print(f"  Stop:     Ctrl+C")
        print()
        try:
            webbrowser.open(url)
        except Exception:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
