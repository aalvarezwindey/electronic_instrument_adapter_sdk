import Open_LISA_SDK

sdk = Open_LISA_SDK.SDK(log_level="INFO", default_response_format="PYTHON")
sdk.connect_through_TCP(host="127.0.0.1", port=8080)

instruments = sdk.get_instruments()
for instrument in instruments:
    print("instrument {} {}".format(instrument["brand"], instrument["model"]))

    commands = sdk.get_instrument_commands(instrument_id=instrument["id"])

    for key in commands:
        command_info = commands[key]

        print("\t command {}".format(command_info["name"]))

sdk.disconnect()
