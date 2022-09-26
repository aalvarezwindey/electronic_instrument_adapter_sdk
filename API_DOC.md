# Open LISA SDK - API Doc

## Constructor

Initializes the SDK with the specified log level and default response format of the methods

```
Open_LISA_SDK.SDK(log_level='WARNING', default_response_format='PYTHON')

    Args:
        log_level (str, optional): specifies the SDK log level. Defaults to "WARNING".
        default_response_format (str, optional): specifies the response format of the SDK methods supported
        types are "PYTHON" for Python native types or "JSON" for JSON strings. Defaults to "PYTHON".

```

### Methods

#### `connect_through_RS232`

Tries to connect with Open LISA Server through RS232 protocol

```
    Open_LISA_SDK.SDK.connect_through_RS232(self, baudrate=921600, port=None) ‑> None

    Args:
        baudrate (int, optional): Specifies the baudrate, must be the same as in Open LISA Server. Defaults to 921600.
        port (str, optional): Serial port of the client side. Defaults to None and will try with all the ports listed by serial.tools.list_ports.comports(),
        this is not recommended since handshake information could be sent to unexpected serial ports.

    Raises:
        CouldNotConnectToServerException: raised when connection could not be stablished
```

#### `connect_through_TCP`

Tries to connect with Open LISA Server through TCP protocol

```
    Open_LISA_SDK.SDK.connect_through_TCP(self, host: str, port: int) ‑> None

    Args:
        host (string): Open LISA Server IP address
        port (int): Open LISA Server port number

    Raises:
        CouldNotConnectToServerException: raised when connection could not be stablished
```

#### `create_directory`

Creates a folder with the name specified by new_directory in remote_path folder

```
    Open_LISA_SDK.SDK.create_directory(self, remote_path, new_directory)

    Args:
        remote_path (str): folder in server side
        new_directory (str): new folder name

    Raises:
        OpenLISAException: raised when there was an error in the Server
```

#### `create_instrument`

Tries to create the new instrument with the fields specified

```
    Open_LISA_SDK.SDK.create_instrument(self, new_instrument, response_format=None)

    Args:
        new_instrument (dict): new instrument payload
        response_format (str, optional): specifies response format. Defaults to None and default_response_format will be used in that case

    Returns:
        dict|string: server creation response

    Raises:
        OpenLISAException: raised when there was an error in the Server
```

#### `create_instrument_command`

Creates the command specified by new_command payload

```
    Open_LISA_SDK.SDK.create_instrument_command(self, new_command, response_format=None)

    Args:
        new_command (dict): new command payload
        response_format (str, optional): specifies response format. Defaults to None and default_response_format will be used in that case

    Raises:
        OpenLISAException: raised when there was an error in the Server
```

#### `delete_directory`

Deletes the folder specified by remote_path and all its content

```
    Open_LISA_SDK.SDK.delete_directory(self, remote_path)

    Args:
        remote_path (str): path in server side

    Raises:
        OpenLISAException: raised when there was an error in the Server
```

#### `delete_file`

Deletes the remote file specified by file_path

```
    Open_LISA_SDK.SDK.delete_file(self, file_path)

    Args:
        file_path (str): file path in server

    Raises:
        OpenLISAException: raised when there was an error in the Server
```

#### `delete_instrument`

Tries to delete the instrument specified

```
    Open_LISA_SDK.SDK.delete_instrument(self, instrument_id, response_format=None)

    Args:
        instrument_id (int): instrument ID
        response_format (str, optional): specifies response format. Defaults to None and default_response_format will be used in that case

    Returns:
        dict|string: server delete response

    Raises:
        OpenLISAException: raised when there was an error in the Server
```

#### `delete_instrument_command`

Deletes the command specified by command_id

```
    Open_LISA_SDK.SDK.delete_instrument_command(self, command_id)

    Args:
        command_id (int): command ID

    Raises:
        OpenLISAException: raised when there was an error in the Server
```

#### `disconnect`

Gracefully disconnect with Open LISA Server

```
    Open_LISA_SDK.SDK.disconnect(self)
```

#### `execute_bash_command`

Executes the bash command specified by command in the server

```
    Open_LISA_SDK.SDK.execute_bash_command(self, command, capture_stdout=False, capture_stderr=False)

    Args:
        command (str): bash command to be executed in server side, the command is executed at sandbox folder
        capture_stdout (bool, optional): if true the stdout of the command is retrieved. Defaults to False.
        capture_stderr (bool, optional): if true the stderr of the command is retrieved. Defaults to False.

    Returns:
        any: command execution result
```

#### `get_detected_physical_addresses`

Get a list of the detected physical addresses in the Open LISA Server

```
    Open_LISA_SDK.SDK.get_detected_physical_addresses(self, response_format=None)

    Args:
        response_format (str, optional): specifies response format. Defaults to None and default_response_format will be used in that case

    Returns:
        list|string: the physical addresses detected

    Raises:
        OpenLISAException: raised when there was an error in the Server
```

#### `get_directory_structure`

Retrieves the directory structure in server specified in remote_path

```
    Open_LISA_SDK.SDK.get_directory_structure(self, remote_path, response_format=None)

    Args:
        remote_path (str): directory path in server side
        response_format (str, optional): specifies response format. Defaults to None and default_response_format will be used in that case

    Returns:
        dict|str: directory structure

    Raises:
        OpenLISAException: raised when there was an error in the Server
```

#### `get_file`

Tries to retrieve the file in server specified by remote_file_name and tries to save in file_target_name in client side

    Open_LISA_SDK.SDK.get_file(self, remote_file_name, file_target_name)

```
    Args:
        remote_file_name (str): file path in server
        file_target_name (str): file path in client

    Raises:
        OpenLISAException: raised when there was an error in the Server
```

#### `get_instrument`

Get the instrument registered in Open LISA Server that matches with the ID

```
    Open_LISA_SDK.SDK.get_instrument(self, instrument_id, response_format=None)

    Args:
        instrument_id (int): instrument ID
        response_format (str, optional): specifies response format. Defaults to None and default_response_format will be used in that case

    Returns:
        dict|string: the instrument match
    Raises:
        OpenLISAException: raised when there was an error in the Server
```

#### `get_instrument_commands`

Get a list of the specified instrument commands

```
    Open_LISA_SDK.SDK.get_instrument_commands(self, instrument_id, response_format=None)

    Args:
        instrument_id (int): instrument ID
        response_format (str, optional): specifies response format. Defaults to None and default_response_format will be used in that case

    Returns:
        list|stirng: The list of the registered commands for that instrument

    Raises:
        OpenLISAException: raised when there was an error in the Server
```

#### `get_instrument_visa_attribute`

Gets the state of the attribute of the instrument with ID instrument_id

```
    Open_LISA_SDK.SDK.get_instrument_visa_attribute(self, instrument_id, attribute)

    Args:
        instrument_id (int): instrument ID
        attribute (Any): the VISA attribute to get

    Returns:
        Any: state of the attribute

    Raises:
        OpenLISAException: raised when there was an error in the Server
```

#### `get_instruments`

Get all the instruments registered in Open LISA Server

```
    Open_LISA_SDK.SDK.get_instruments(self, response_format=None)

    Args:
        response_format (str, optional): specifies response format. Defaults to None and default_response_format will be used in that case

    Returns:
        dict|string: list of registered instruments

    Raises:
        OpenLISAException: raised when there was an error in the Server
```

#### `is_valid_command_invocation`

Determines if the command invocation syntax is valid but it is not sent to the instrument

```
    Open_LISA_SDK.SDK.is_valid_command_invocation(self, instrument_id, command_invocation)

    Args:
        instrument_id (int): instrument ID
        command_invocation (str): command invocation syntax

    Returns:
        bool: True or False depending the validity of the command invocation syntax
```

#### `send_command`

Sends the command_invocation to the specified instrument by instrument_id

```
    Open_LISA_SDK.SDK.send_command(self, instrument_id, command_invocation, command_result_output_file=None, response_format=None, convert_result_to=None)

    Args:
        instrument_id (int): instrument ID
        command_invocation (str): command invocation syntax with parameters
        command_result_output_file (str, optional): if provided the output of the command will be saved in server at the specified path and
        not returned to the client (convinient for low throughputs between client and server). Defaults to None.
        response_format (str, optional): specifies response format. Defaults to None and default_response_format will be used in that case
        convert_result_to (str, optional): converts the result to the specified type, supported types are "str", "double", "bytearray", "bytes" and "int". Defaults to None.

    Raises:
        InvalidCommandException: when the command could not be executed

    Returns:
        str|int|float|bytearray|bytes: the result of the command execution
```

#### `send_file`

Sends the file specified by client file_path and saves it in the server at file_target_name

```
    Open_LISA_SDK.SDK.send_file(self, file_path, file_target_name)

    Args:
        file_path (str): client side file path
        file_target_name (_type_): server remote file path

    Raises:
        OpenLISAException: raised when there was an error in the Server
```

#### `set_instrument_visa_attribute`

Sets the state of the attribute of the instrument with ID instrument_id

```
    Open_LISA_SDK.SDK.set_instrument_visa_attribute(self, instrument_id, attribute, state)

    Args:
        instrument_id (int): instrument ID
        attribute (Any): the VISA attribute to set
        state (str): the state to set

    Returns:
        str: status of the set operation

    Raises:
        OpenLISAException: raised when there was an error in the Server
```

#### `update_instrument`

Tries to update the instrument with the fields specified

```
    Open_LISA_SDK.SDK.update_instrument(self, instrument_id, updated_instrument, response_format=None)

    Args:
        instrument_id (int): instrument ID
        updated_instrument (dict): new instrument fields
        response_format (str, optional): specifies response format. Defaults to None and default_response_format will be used in that case

    Returns:
        dict|string: server update response

    Raises:
        OpenLISAException: raised when there was an error in the Server
```
