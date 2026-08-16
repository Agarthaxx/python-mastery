message = "Café à 3€"
message_bytes = message.encode("utf-8")
print(message_bytes)

message_decode = message_bytes.decode("utf-8")
print(message_decode)

message.encode("ascii")