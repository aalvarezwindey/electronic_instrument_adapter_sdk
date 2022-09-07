import Open_LISA_SDK


sdk = Open_LISA_SDK.SDK(log_level="INFO", default_response_format="PYTHON")
sdk.connect_through_TCP(host="127.0.0.1", port=8080)

instruments = sdk.get_instruments()

# Precondition: instrument with ID should be registered
ins_id = 3
example_c_lib_instrument = sdk.get_instrument(instrument_id=ins_id)
assert example_c_lib_instrument["id"] == ins_id

commands = sdk.get_instrument_commands(instrument_id=ins_id)

assert "multipy_in_c_lib" in commands

result = sdk.send_command(instrument_id=ins_id,
                          command_invocation="multipy_in_c_lib 2.5 2.0")

print("multipy_in_c_lib 2.5 2.0 = {}".format(result["value"]))

sdk.disconnect()
