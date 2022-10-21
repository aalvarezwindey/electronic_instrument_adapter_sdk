# Open LISA SDK - Architecture

## Overview
In the following diagram there is an overview of the different components in Open LISA platform:
* Client PCs that runs SDK and/or UI
* PC running Open LISA Server which communicates with instruments and stores configurations

![open_lisa_architecture](https://user-images.githubusercontent.com/45921171/195215569-f92946ba-066e-493d-a0c1-76c4ffdb0531.png)

## Physical View

The following deploy diagram shows the different hardware components, and their services/interfaces involved
in end-to-end Open LISA experience.

[![Deploy Diagram](https://tinyurl.com/27a7x6sc)](https://tinyurl.com/27a7x6sc)

## Logic view

The main classes involved for the SDK are shown in the following class diagram
* `SDK` class is the entrypoint, the only class that the user should use directly
* `ClientProtocol` class implements the messages interchanged between client and server to consume Open LISA functionalities
* Custom exceptions and protocol specific classes.

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

[![Generic SDK request](https://tinyurl.com/2b9dvu35)](https://tinyurl.com/2b9dvu35)<!--![Generic SDK request](./sequence_diagram_high_level_sdk_request.puml)-->

For example, these are the messages involved in a `send_file` request made by the Open LISA SDK.

[![Messages involved in SDK request](https://tinyurl.com/265hyne4)](https://tinyurl.com/265hyne4)<!--![Messages involved in SDK request](./sequence_diagram_messages_in_request.puml)-->

Lastly, in the following diagram we see how a message is composed in Open LISA, being always four bytes for the message length and then the message content itself.

Through this concept, is easy to extend the transport protocol to a new one always implementing `MessageProtocol` interface

[![What is a Message?](https://tinyurl.com/23zplzc5)](https://tinyurl.com/23zplzc5)<!--![What is a Message?](./sequence_diagram_what_is_a_message.puml)-->
