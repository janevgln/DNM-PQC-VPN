"""
Simple Prometheus Metrics Exporter
"""

from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8000


class MetricsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        metrics = """
vpn_connections 5
vpn_latency_ms 18
vpn_packets_sent 1250
vpn_packets_received 1210
"""

        self.wfile.write(metrics.encode())


if __name__ == "__main__":
    print(f"Metrics Exporter running on port {PORT}")

    server = HTTPServer(("0.0.0.0", PORT), MetricsHandler)

    server.serve_forever()