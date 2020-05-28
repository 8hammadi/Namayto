import nexmo

client = nexmo.Client(key='950d1ba0', secret='9Qz3Eclw0CRGy8Cx')


response = client.start_verification(
  number="+212610781949",
  brand="Vonage",
  code_length="4")

if response["status"] == "0":
  print("Started verification request_id is %s" % (response["request_id"]))
else:
  print("Error: %s" % response["error_text"])