% Define the Python interpreter
pcPythonExe = 'C:\PathTo\Python\Python39\python.exe';
%[ver, exec, loaded]	= pyversion(pcPythonExe);
pyversion
py.print("Connect with server")

% Precondition: this example assumes a Tektronix TDS1002B oscilloscope registered
% with all the commands needed with the physicial address specified and ID = 1
physical_address = "USB0::0x0699::0x0363::C107676::INSTR"

sdk = py.Open_LISA_SDK.SDK(log_level="INFO", default_response_format="JSON")
sdk.connect_through_TCP("127.0.0.1", "8080")
try
    % List instruments
    json_instruments = sdk.get_instruments()

    % transform json strings to matlab types
    instruments = jsondecode(json_instruments)

    id = 1
    % Configuration commands
    sdk.send_command(instrument_id=id,
                     command_invocation="set_waveform_source_ch1")
    sdk.send_command(instrument_id=id,
                     command_invocation="set_waveform_source_ch1")
    sdk.send_command(instrument_id=id,
                     command_invocation="set_waveform_bytes_width_1")
    sdk.send_command(instrument_id=id,
                     command_invocation="set_waveform_encoding_rpbinary")


    % Get needed parameters to draw the figure
    ymult = sdk.send_command(instrument_id=id, command_invocation="get_waveform_vertical_scale_factor")
    yzero = sdk.send_command(instrument_id=id, command_invocation="get_waveform_conversion_factor")
    yoff = sdk.send_command(instrument_id=id, command_invocation="get_waveform_vertical_offset")
    xincr = sdk.send_command(instrument_id=id, command_invocation="get_waveform_horizontal_sampling_interval")

    % Cast native python bytes to Matlab type
    data = uint8(sdk.send_command(instrument_id=id, command_invocation="get_waveform_data", convert_result_to="bytes"));

    % Cast header to double because it will be the index
    header_len = double(2 + data(2));

    % Discard header and last data (logic necessary for this specific instrument)
    ADC_wave = data(header_len:end-1);
    volts = (double(ADC_wave) - yoff) * ymult + yzero;
    vols_size = size(volts);
    time = 0 : xincr : xincr * (vols_size(2)-1);
    plot(time, volts);
catch e
    fprintf(1,'The identifier was:\n%s', e.identifier);
    fprintf(1,'There was an error! The message was:\n%s', e.message);
    sdk.disconnect()
end
sdk.disconnect()