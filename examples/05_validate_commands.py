import Open_LISA_SDK

sdk = Open_LISA_SDK.SDK(log_level="INFO", default_response_format="PYTHON")
sdk.connect_through_TCP(host="127.0.0.1", port=8080)

instruments = sdk.get_instruments()

if len(instruments) != 0:
    scpi_instrument = None
    for i in instruments:
        if i["type"] == "SCPI":
            scpi_instrument = i
            break

    id = scpi_instrument["id"]

    invocation = "unexisting command"
    is_valid = sdk.is_valid_command_invocation(
        instrument_id=id,
        command_invocation=invocation
    )
    print("invocation {} is valid? {}".format(invocation, is_valid))

    invocation = "clear_status 0"
    is_valid = sdk.is_valid_command_invocation(
        instrument_id=id,
        command_invocation=invocation
    )
    print("invocation {} is valid? {}".format(invocation, is_valid))

    invocation = "clear_status ASCII"
    is_valid = sdk.is_valid_command_invocation(
        instrument_id=id,
        command_invocation=invocation
    )
    print("invocation {} is valid? {}".format(invocation, is_valid))

    invocation = "clear_status"
    is_valid = sdk.is_valid_command_invocation(
        instrument_id=id,
        command_invocation=invocation
    )
    print("invocation {} is valid? {}".format(invocation, is_valid))
else:
    print("no instruments available")

sdk.disconnect()
