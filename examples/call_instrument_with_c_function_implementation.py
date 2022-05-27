import Open_LISA_SDK

def main():
  sdk = Open_LISA_SDK.SDK()
  sdk.connect_through_RS232()

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