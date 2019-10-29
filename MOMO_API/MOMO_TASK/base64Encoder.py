import base64

def encode(data):
 # Standard Base64 Encoding
 encodedBytes = base64.b64encode(data.encode("utf-8"))
 encodedStr = str(encodedBytes, "utf-8")
 return encodedStr