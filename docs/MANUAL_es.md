# Manual – Electronic Instrument Adapter SDK

Esta SDK provee una interfaz para integrarse con el [Electronic Instrument Adapter server](https://github.com/aalvarezwindey/electronic-instrument-adapter/). El servidor debe estar integrado con los instrumentos de interés y estar corriendo en una IP y puertos conocidos.

## Instalación
```
pip install electronic-instrument-adapter-sdk
```

## Ejemplos

### Listar los instrumentos disponibles y registrados
```python
import electronic_instrument_adapter_sdk
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--host", type=str, help="server host", default="127.0.0.1")
parser.add_argument("--port", type=int, help="server port", default=8080)
args = parser.parse_args()

# Connect with server running on localhost and port 8080
sdk = electronic_instrument_adapter_sdk.EIA(args.host, args.port)

# List instruments
print(sdk.list_instruments())
```

### Listar los comandos disponibles para un instrumento específico

This snippet list all available commands for the first instrument returned by the server.

```python
import electronic_instrument_adapter_sdk

sdk = electronic_instrument_adapter_sdk.EIA("127.0.0.1", 8080)

instruments = sdk.list_instruments()

if len(instruments) != 0:
  instrument = instruments[0]

  commands = instrument.available_commands()
  for c in commands:
    print(c)
else:
  print("no instruments available")
```

### Validar comando

Los comandos de los instrumentos que son configurados en el servidor tienen una sintaxis específica. Este ejemplo muestra cómo es posible comprobar si un comando que queremos utilizar es válido. Se recomienda esta práctica con el fin de prevenir el envío de comandos malformados a los instrumentos.

```python
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
```

### Enviando un comando

Este ejemplo más avanzado muestra cómo realizar un gráfico de lo que muestra un Osciloscopio Tektronix TDS1002B en el canal 1. Notar que el ejemplo asume un instrumento configurado en el servidor con un ID y comandos específicos.

```python
import electronic_instrument_adapter_sdk
import numpy as np
from struct import unpack
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--host", type=str, help="server host", default="127.0.0.1")
parser.add_argument("--port", type=int, help="server port", default=8080)
args = parser.parse_args()

sdk = electronic_instrument_adapter_sdk.EIA(args.host, args.port)

instruments = sdk.list_instruments()
osc_tds1002b = None
for i in instruments:
  if i.ID == "USB0::0x0699::0x0363::C107676::INSTR":
    osc_tds1002b = i

if osc_tds1002b:
  osc_tds1002b.send("set_waveform_source_ch1")
  osc_tds1002b.send("set_waveform_bytes_width_1")
  osc_tds1002b.send("set_waveform_encoding_rpbinary")
  Volts = np.empty(0)
  ymult = float(osc_tds1002b.send("get_waveform_vertical_scale_factor"))
  yzero = float(osc_tds1002b.send("get_waveform_conversion_factor"))
  yoff = float(osc_tds1002b.send("get_waveform_vertical_offset"))
  xincr = float(osc_tds1002b.send("get_waveform_horizontal_sampling_interval"))

  data = osc_tds1002b.send("get_waveform_data")

  headerlen = 2 + int(data[1])
  header = data[:headerlen]
  ADC_wave = data[headerlen:-1]
  ADC_wave = np.array(unpack('%sB' % len(ADC_wave), ADC_wave))
  Volts = np.append(Volts, (ADC_wave - yoff) * ymult + yzero)
  Time = np.arange(0, xincr * len(Volts), xincr)

  plt.figure(figsize=(20,10))
  plt.plot(Time, Volts)
  plt.grid()
  plt.xlabel("Time")
  plt.ylabel("Voltage [V]")
  plt.show()

else:
  print("Oscilloscope TDS1002B not found")
```

### Obtener una imagen capturada por una cámara

En este ejemplo se obtienen los bytes capturados por una cámara registrada con ID `CAM_ID` a la cual se le registró un comando `get_image`. Notar que esta función se integra del lado del servidor con código C pero a los fines de esta SDK es transparente si el comando está configurado correctamente. Como resultado genera un archivo `image.jpeg`.

```python
import electronic_instrument_adapter_sdk
import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--host", type=str, help="server host", default="127.0.0.1")
  parser.add_argument("--port", type=int, help="server port", default=8080)
  args = parser.parse_args()

  sdk = electronic_instrument_adapter_sdk.EIA(args.host, args.port)

  instruments = sdk.list_instruments()
  cammera = None
  for i in instruments:
    if i.ID == "CAM_ID":
      cammera = i

  if cammera:
    result = cammera.send("get_image", "bytes")
    print("Saving image bytes...")
    with open("image.jpeg", "wb") as f:
      f.write(result)
  else:
    print("Cammera with ID 'CAM_ID' not found")

if __name__ == "__main__":
    main()
```

### Integración con Matlab

Es posible hacer uso de esta SDK vía Matlab. Para ello se debe:
* Indicar en Matlab la ubicación del intérprete de Python
* En caso de que un comando responda datos del tipo `bytes`, el casteo más sencillo para trabajarlo en Matlab es a `uint8()``

En el ejemplo siguiente tenemos el caso análogo del gráfico del Osciloscopio Tektronix pero desde Matlab:

```octave
% Es necesario definir la ruta del intérprete de python
pcPythonExe = 'C:\PathTo\Python\Python39\python.exe';
%[ver, exec, loaded]	= pyversion(pcPythonExe);
pyversion

py.print("Conexion con el servidor")
eia_sdk = py.electronic_instrument_adapter_sdk.EIA("127.0.0.1", "8080")

try
    % Se obtienen los instrumentos
    instruments = eia_sdk.list_instruments()

    % El ID del oscilloscopio es: USB0::0x0699::0x0363::C107676::INSTR
    osciliscopio = eia_sdk.get_instrument("USB0::0x0699::0x0363::C107676::INSTR")

    % Enviamos comandos de configuracion
    osciliscopio.send("set_waveform_bytes_width_1")
    osciliscopio.send("set_waveform_encoding_rpbinary")

    % Obtenemos parámetros necesarios para hacer el gráfico
    ymult = osciliscopio.send("get_waveform_vertical_scale_factor")
    yzero = osciliscopio.send("get_waveform_conversion_factor")
    yoff = osciliscopio.send("get_waveform_vertical_offset")
    xincr = osciliscopio.send("get_waveform_horizontal_sampling_interval")

    % Data es una lista de bytes de python (bytes), casteo a un dato nativo de Matlab
    data = uint8(osciliscopio.send("get_waveform_data", "bytes"));

    % Casteo a double el header len porque luego indexaremos con eso
    header_len = double(2 + data(2));

    % Descartamos el header y el Ultimo dato (lógica necesaria para este instrumento y modelo en particular)
    ADC_wave = data(header_len:end-1);

    volts = (double(ADC_wave) - yoff) * ymult + yzero;
    vols_size = size(volts);
    time = 0 : xincr : xincr * (vols_size(2)-1);

    plot(time, volts);
catch e
    fprintf(1,'The identifier was:\n%s', e.identifier);
    fprintf(1,'There was an error! The message was:\n%s', e.message);

    % Es necesario desconectar la SDK explicitamente ya que
    % los destructores de los objetos Python no son llamados
    % Esto se debe a que las variables siguen existiendo en el Workspace de Matlab.
    eia_sdk.disconnect()
end

eia_sdk.disconnect()
```