# ============================================================
# Integration Layer
#
# Created by Person 1 to connect the client-handling layer
# to the request-processing layer.
#
# Note:
# Person 2 will replace/expand this file with full request
# parsing, HTTP forwarding, and response relaying logic.
# ============================================================


def route_request(client_socket, client_address, request_data):
    """
    Temporary routing function used to verify that Person 1's
    connection-handling and threading logic works correctly.
    """

    try:
        body = b"Proxy received the request successfully."

        headers = (
            b"HTTP/1.1 200 OK\r\n"
            b"Content-Type: text/plain\r\n"
            b"Content-Length: " + str(len(body)).encode() + b"\r\n"
            b"Connection: close\r\n"
            b"\r\n"
        )

        client_socket.sendall(headers + body)

        print(f"[ROUTER] Request passed to routing layer for {client_address}")
        print("[ROUTER] Temporary test response sent successfully.")

    except Exception as e:
        print(f"[ROUTER ERROR] {client_address} -> {e}")