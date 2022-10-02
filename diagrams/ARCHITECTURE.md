# Open LISA SDK - Architecture

## Logic view

The main classes involved for the SDK are shown in the following class diagram

[![Class Diagram](https://tinyurl.com/2dv383pr)](https://tinyurl.com/2dv383pr)<!--![Class Diagram](./class_diagram.puml)-->

## Development view

The packages diagram below, shows how the modules are organized in the client side of Open LISA project

[![Packages Diagram](https://tinyurl.com/2nv6s7d2)](https://tinyurl.com/2nv6s7d2)<!--![Packages Diagram](./packages_diagram.puml)-->

## Processes view

In the following sequence diagrams we can see from a high to low perspective the interactions involved between the SDK and Server.

First, being a client-server architecture this is the logic for any request that is made by the Open LISA SDK:

1. The SDK sends a request and its payload
2. The server handles it and sends back a response
3. The SDK raises if there was an error o sends a result back

[![Generic SDK request](https://tinyurl.com/2kgpca8j)](https://tinyurl.com/2kgpca8j)<!--![Generic SDK request](./sequence_diagram_high_level_sdk_request.puml)-->

For example, these are the messages involved in a `send_file` request made by the Open LISA SDK.

[![Messages involved in SDK request](https://tinyurl.com/2nyq62xk)](https://tinyurl.com/2nyq62xk)<!--![Messages involved in SDK request](./sequence_diagram_messages_in_request.puml)-->

Lastly, in the following diagram we see how a message is composed in Open LISA, being always four bytes for the message length and then the message content itself.

Through this concept, is easy to extend the transport protocol to a new one always implementing `MessageProtocol` interface

[![What is a Message?](https://tinyurl.com/2hb5gnt9)](https://tinyurl.com/2hb5gnt9)<!--![What is a Message?](./sequence_diagram_what_is_a_message.puml)-->
