# ============================================================
# Team Member: Tala
# Contribution: Person 1 - Basic client connection handling
#
# Tasks implemented in this file:
# - Handle individual client connections
# - Receive request data from client
# - Manage connection lifecycle (open → process → close)
# - Forward request data to routing/handler layer
# ============================================================

from request_router import route_request
from utils.constants import BUFFER_SIZE


def handle_client(client_socket, client_address):
    """
    Handles a single client connection.
    Receives the request and forwards it to the routing layer.
    """

    print(f"[NEW CONNECTION] Client connected: {client_address}")

    try:
        request_data = client_socket.recv(BUFFER_SIZE)

        if not request_data:
            print(f"[WARNING] Empty request from {client_address}")
            return

        print(f"[REQUEST RECEIVED] From {client_address}")
        print(f"[REQUEST SIZE] {len(request_data)} bytes")

        # Pass request to routing layer (Person 2 will expand this)
        route_request(client_socket, client_address, request_data)

    except Exception as e:
        print(f"[CLIENT ERROR] {client_address} -> {e}")

    finally:
        client_socket.close()
        print(f"[CONNECTION CLOSED] {client_address}")