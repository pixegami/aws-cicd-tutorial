def handler(event, context):
    response_body = {"message": "Hello World", "version": "1.0.0"}
    return {"statusCode": 200, "body": response_body}
