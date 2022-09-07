import Open_LISA_SDK

sdk = Open_LISA_SDK.SDK()
sdk.connect_through_RS232()

instruments = sdk.get_instruments()

if len(instruments) != 0:
    instrument = instruments[0]

    instrument.validate_command("unexisting command")
    instrument.validate_command("set_waveform_encoding_ascii")
    instrument.validate_command("set_trigger_level 10 20")
    instrument.validate_command("set_trigger_level ASCII")
    instrument.validate_command("set_trigger_level 3.4")
else:
    print("no instruments available")

sdk.disconnect()
