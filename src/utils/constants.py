# ============================================================
# Configuration Constants
#
# This file centralizes all configurable parameters used
# by the proxy server for easier maintenance and readability.
# ============================================================

HOST = "0.0.0.0"      # Listen on all available network interfaces
PORT = 8888           # Proxy server port
BACKLOG = 50          # Max queued connections
BUFFER_SIZE = 4096    # Size of data chunks received from clients
ENCODING = "utf-8"    # Default encoding (if needed later)