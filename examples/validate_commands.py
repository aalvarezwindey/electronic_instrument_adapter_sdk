import electronic_instrument_adapter_sdk

sdk = electronic_instrument_adapter_sdk.EIA("127.0.0.1", 8080)

instruments = sdk.list_instruments()

if len(instruments) != 0:
  instrument = instruments[0]

  instrument.validate_command("unexisting command")
  instrument.validate_command("set_waveform_encoding_ascii")
  instrument.validate_command("set_trigger_level 10 20")
  instrument.validate_command("set_trigger_level ASCII")
  instrument.validate_command("set_trigger_level 3.4")
else:
  print("no instruments available")