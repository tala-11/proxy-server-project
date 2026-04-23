# ============================================================
# Team Member: Tala
# Contribution: Person 1 - Core connection handling + threading
#
# Tasks implemented in this file:
# - Create the proxy server socket
# - Bind the server to a host and port
# - Listen for incoming client connections
# - Accept client connections
# - Start a separate thread for each connected client
# ============================================================

import socket
import threading

from client_handler import handle_client
from utils.constants import HOST, PORT, BACKLOG


def start_proxy_server():
    """
    Starts the proxy server and continuously listens for clients.
    Each accepted client is assigned to a separate thread so multiple
    client requests can be handled concurrently.
    """

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Allows the same port to be reused quickly after restarting the server.
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen(BACKLOG)

        print("=" * 55)
        print("[INFO] Proxy Server Started")
        print(f"[INFO] Listening on: {HOST}:{PORT}")
        print(f"[INFO] Maximum queued connections: {BACKLOG}")
        print("=" * 55)

        while True:
            client_socket, client_address = server_socket.accept()

            print(f"[ACCEPTED] Connection from {client_address}")

            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address),
                name=f"ClientThread-{client_address[0]}-{client_address[1]}"
            )

            client_thread.daemon = True
            client_thread.start()

            print(f"[THREAD STARTED] {client_thread.name}")

    except KeyboardInterrupt:
        print("\n[SHUTDOWN] Server stopped manually by user.")

    except Exception as e:
        print(f"[SERVER ERROR] {e}")

    finally:
        server_socket.close()
        print("[CLOSED] Server socket closed.")