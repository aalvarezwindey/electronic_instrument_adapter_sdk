import Open_LISA_SDK

sdk = Open_LISA_SDK.SDK(log_level="DEBUG")
sdk.connect_through_TCP(host="10.147.18.66", port=8080)

# List instruments
instruments = sdk.get_instruments()

if len(instruments) != 0:
    instrument = instruments[0]

    commands = instrument.available_commands()
    for c in commands:
        print(c)
else:
    print("no instruments available")

sdk.disconnect()
