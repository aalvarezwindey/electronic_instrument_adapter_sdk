import Open_LISA_SDK
import numpy as np
from struct import unpack
import matplotlib.pyplot as plt

# Precondition: this example assumes a Tektronix TDS1002B oscilloscope registered
# with all the commands needed with the physicial address specified
physical_address = "USB0::0x0699::0x0363::C107676::INSTR"

sdk = Open_LISA_SDK.SDK(log_level="INFO", default_response_format="PYTHON")
sdk.connect_through_TCP(host="127.0.0.1", port=8080)


instruments = sdk.get_instruments()
osc_tds1002b = None
for i in instruments:
    if i["physical_address"] == physical_address:
        osc_tds1002b = i

if osc_tds1002b:
    id = osc_tds1002b["id"]
    sdk.send_command(instrument_id=id,
                     command_invocation="set_waveform_source_ch1")
    sdk.send_command(instrument_id=id,
                     command_invocation="set_waveform_source_ch1")
    sdk.send_command(instrument_id=id,
                     command_invocation="set_waveform_bytes_width_1")
    sdk.send_command(instrument_id=id,
                     command_invocation="set_waveform_encoding_rpbinary")
    Volts = np.empty(0)
    ymult = float(sdk.send_command(instrument_id=id,
                  command_invocation="get_waveform_vertical_scale_factor"))
    yzero = float(sdk.send_command(instrument_id=id,
                  command_invocation="get_waveform_conversion_factor"))
    yoff = float(sdk.send_command(instrument_id=id,
                 command_invocation="get_waveform_vertical_offset"))
    xincr = float(sdk.send_command(instrument_id=id,
                  command_invocation="get_waveform_horizontal_sampling_interval"))

    data = sdk.send_command(
        instrument_id=id, command_invocation="get_waveform_data")

    headerlen = 2 + int(data[1])
    header = data[:headerlen]
    ADC_wave = data[headerlen:-1]
    ADC_wave = np.array(unpack('%sB' % len(ADC_wave), ADC_wave))
    Volts = np.append(Volts, (ADC_wave - yoff) * ymult + yzero)
    Time = np.arange(0, xincr * len(Volts), xincr)

    plt.figure(figsize=(20, 10))
    plt.plot(Time, Volts)
    plt.grid()
    plt.xlabel("Time")
    plt.ylabel("Voltage [V]")
    plt.show()

else:
    print("Oscilloscope TDS1002B not found")

sdk.disconnect()
