from google.cloud import translate_v3

def sample_batch_translate_document():
    # Create a client
    client = translate_v3.TranslationServiceClient()

    # Initialize request argument(s)
    input_configs = translate_v3.BatchDocumentInputConfig()
    input_configs.gcs_source.input_uri = "input_uri_value"

    output_config = translate_v3.BatchDocumentOutputConfig()
    output_config.gcs_destination.output_uri_prefix = "output_uri_prefix_value"

    request = translate_v3.BatchTranslateDocumentRequest(
        parent="parent_value",
        source_language_code="source_language_code_value",
        target_language_codes=['target_language_codes_value_1', 'target_language_codes_value_2'],
        input_configs=input_configs,
        output_config=output_config,
    )

    # Make the request
    operation = client.batch_translate_document(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)