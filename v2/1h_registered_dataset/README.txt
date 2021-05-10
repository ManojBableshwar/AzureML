
manoj@Azure:~/clouddrive/repos/AzureML/v2/1h_registered_dataset$ az ml job create --file hello_pipeline_python_registred_dataset.yml Command group 'ml job' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus
Validation for PipelineJobSchema failed:

 {
  "inputs": {
    "pipeline_sample_data": {
      "value": [
        {
          "data": [
            {
              "_schema": [
                "Anonymous assets must be defined inline"
              ]
            },
            {
              "_schema": [
                "Either version is not provided for data or the id is not valid."
              ]
            }
          ]
        },
        {
          "_schema": [
            "Not a valid string."
          ]
        },
        {
          "_schema": [
            "Not a valid boolean."
          ]
        },
        {
          "_schema": [
            "Not a valid integer."
          ]
        },
        {
          "_schema": [
            "Not a valid number."
          ]
        },
        {
          "data": [
            "Unknown field."
          ],
          "mode": [
            "Unknown field."
          ]
        }
      ]
    }
  }
} 

 If the job type is incorrect, change the 'type' property.


