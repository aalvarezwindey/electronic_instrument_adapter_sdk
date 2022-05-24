import Open_LISA_SDK
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--host", type=str, help="server host", default="127.0.0.1")
parser.add_argument("--port", type=int, help="server port", default=8080)
args = parser.parse_args()

# Define server config
sdk = Open_LISA_SDK.SDK(args.host, args.port)

# List instruments
print(sdk.list_instruments())
