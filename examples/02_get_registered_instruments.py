import Open_LISA_SDK

sdk = Open_LISA_SDK.SDK(log_level="INFO", default_response_format="PYTHON")
sdk.connect_through_TCP(host="127.0.0.1", port=8080)

instruments = sdk.get_instruments()
for instrument in instruments:
    print("instrument {} {}".format(instrument["brand"], instrument["model"]))

sdk.disconnect()
