import Open_LISA_SDK
import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--host", type=str, help="server host", default="127.0.0.1")
  parser.add_argument("--port", type=int, help="server port", default=8080)
  args = parser.parse_args()

  sdk = Open_LISA_SDK.SDK(args.host, args.port)

  instruments = sdk.list_instruments()
  cammera = None
  for i in instruments:
    if i.ID == "CAM_ID":
      cammera = i

  if cammera:
    result = cammera.send("init_cammera 1 2.0", "int")
    print("Result from cammera command: {}".format(result))
  else:
    print("Cammera with ID 'CAM_ID' not found")

if __name__ == "__main__":
    main()