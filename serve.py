#!/usr/bin/env python3
"""
Preview server for the 洋ちゃれのカフェ homepage.
Run this file and open http://localhost:8000 to view index.html.
"""
import argparse
import http.server
import os
import socketserver


class PreviewTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def run_server(port: int) -> None:
    web_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(web_dir)

    handler = http.server.SimpleHTTPRequestHandler

    with PreviewTCPServer(("", port), handler) as httpd:
        print(f"Serving preview at http://localhost:{port}")
        print("Press Ctrl+C to stop.")
        httpd.serve_forever()


def main() -> None:
    parser = argparse.ArgumentParser(description="Start a local preview server for index.html")
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to bind the preview server (default: 8000)",
    )
    args = parser.parse_args()

    run_server(args.port)


if __name__ == "__main__":
    main()
