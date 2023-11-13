def function_ejercicio_gcp(event, context):
    """Triggeredd by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    print("HOLA MUNDO")
    file = event
    print(f"Processing file: {file['name']}.")
