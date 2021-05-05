manoj@Azure:~/clouddrive/repos/AzureML/v2/1e_component_input_output_mapped_to_pipeline_job$ az ml job create --file hello_pipeline_python.yml --name job2
Command group 'ml job' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus
datastore_name workspaceblobstore is not a full arm id. Proceed with a shortened name.
Code: BadRequest
Message: Response status code does not indicate success: 400 (Bad Request).
Trace id: [bef64410-a19c-457f-a11a-b1f83fa7c7a0], message: Can't build command text for [123_78a39f86-6fe3-499d-9645-6be877a7a6f0], moduleId [51cfac85-63fd-4554-bad0-b4d1b5571736] executionId [ffd9894b]: Assignment for parameter sample_string is not specified
