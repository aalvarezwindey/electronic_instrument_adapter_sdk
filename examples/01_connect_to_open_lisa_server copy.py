import Open_LISA_SDK

sdk = Open_LISA_SDK.SDK(log_level="DEBUG", default_response_format="PYTHON")

# Connecting under TCP protocol
try:
    sdk.connect_through_TCP(host="127.0.0.1", port=8080)
    sdk.disconnect()
except Exception as e:
    print("fail connecting through TCP", e)

# Connecting under RS232 protocol
try:
    sdk.connect_through_RS232(port="COM3")
    sdk.disconnect()
except Exception as e:
    print("fail connecting through RS232", e)
