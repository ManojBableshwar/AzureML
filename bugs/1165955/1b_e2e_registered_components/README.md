Register components with the AzureML workspace using the `az ml component create --file <your_yaml_file>`. If you are re-running samples, the version specified in the component yaml may already be registered. You can edit the component yaml to bump up the version or you can simply specify a new version using the command line: `az ml component create --file train.yml --set version=<version_number>`


```
manoj@Azure:~/clouddrive/repos/AzureML/samples/1b_e2e_registered_components$ az ml component create --file train.yml --set version=20
Command group 'ml component' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus
{
  "code": "azureml:/subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/resourceGroups/OpenDatasetsPMRG/providers/Microsoft.MachineLearningServices/workspaces/OpenDatasetsPMWorkspace/codes/13eec8de-86ac-4bc8-bfeb-4f6fe6b2f0fa/versions/1",
  "command": "python train.py  --training_data {inputs.training_data}  --max_epocs {inputs.max_epocs}    --learning_rate {inputs.learning_rate}  --learning_rate_schedule {inputs.learning_rate_schedule}  --model_output {outputs.model_output}",
  "display_name": "Train",
  "environment": "azureml:/subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/resourceGroups/OpenDatasetsPMRG/providers/Microsoft.MachineLearningServices/workspaces/OpenDatasetsPMWorkspace/environments/AzureML-Minimal/versions/1",
  "inputs": {
    "learning_rate": {
      "default": "0.01",
      "optional": false,
      "type": "number"
    },
    "learning_rate_schedule": {
      "default": "time-based",
      "optional": false,
      "type": "string"
    },
    "max_epocs": {
      "optional": false,
      "type": "integer"
    },
    "training_data": {
      "optional": false,
      "type": "path"
    }
  },
  "is_deterministic": true,
  "name": "Train",
  "outputs": {
    "model_output": {
      "type": "path"
    }
  },
  "tags": {},
  "type": "command_component",
  "version": 20
}
manoj@Azure:~/clouddrive/repos/AzureML/samples/1b_e2e_registered_components$ az ml component create --file score.yml --set version=20
Command group 'ml component' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus
{
  "code": "azureml:/subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/resourceGroups/OpenDatasetsPMRG/providers/Microsoft.MachineLearningServices/workspaces/OpenDatasetsPMWorkspace/codes/aefc1434-4823-4a49-9ef4-2ff397b88955/versions/1",
  "command": "python score.py  --model_input {inputs.model_input}  --test_data {inputs.test_data} --score_output {outputs.score_output}",
  "display_name": "Score",
  "environment": "azureml:/subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/resourceGroups/OpenDatasetsPMRG/providers/Microsoft.MachineLearningServices/workspaces/OpenDatasetsPMWorkspace/environments/AzureML-Minimal/versions/1",
  "inputs": {
    "model_input": {
      "optional": false,
      "type": "path"
    },
    "test_data": {
      "optional": false,
      "type": "path"
    }
  },
  "is_deterministic": true,
  "name": "Score",
  "outputs": {
    "score_output": {
      "type": "path"
    }
  },
  "tags": {},
  "type": "command_component",
  "version": 20
}
manoj@Azure:~/clouddrive/repos/AzureML/samples/1b_e2e_registered_components$ az ml component create --file eval.yml --set version=20
Command group 'ml component' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus
{
  "code": "azureml:/subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/resourceGroups/OpenDatasetsPMRG/providers/Microsoft.MachineLearningServices/workspaces/OpenDatasetsPMWorkspace/codes/03df61e7-87d5-44e4-8af0-ae073c00cdb9/versions/1",
  "command": "python eval.py  --scoring_result {inputs.scoring_result}  --eval_output {outputs.eval_output}",
  "display_name": "Eval",
  "environment": "azureml:/subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/resourceGroups/OpenDatasetsPMRG/providers/Microsoft.MachineLearningServices/workspaces/OpenDatasetsPMWorkspace/environments/AzureML-Minimal/versions/1",
  "inputs": {
    "scoring_result": {
      "optional": false,
      "type": "path"
    }
  },
  "is_deterministic": true,
  "name": "Eval",
  "outputs": {
    "eval_output": {
      "type": "path"
    }
  },
  "tags": {},
  "type": "command_component",
  "version": 20
}
manoj@Azure:~/clouddrive/repos/AzureML/samples/1b_e2e_registered_components$ 

```


Make sure the version of the components you registered matches with the version defined in pipeline.yml. You can then create the Pipeline Job with the `az ml  job create --file pipeline.yml` command. 

```
manoj@Azure:~/clouddrive/repos/AzureML/bugs/1165955/1b_e2e_registered_components$ az ml  job create --file pipeline.yml --set defaults.component_job.compute.target=manojcompute6
Command group 'ml job' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus
Validation for PipelineJobSchema failed:

 {
  "jobs": {
    "train-job": {
      "value": {
        "component": [
          {
            "_schema": [
              "Either version is not provided for component or the id is not valid."
            ]
          },
          {
            "_schema": [
              "Anonymous assets must be defined inline"
            ]
          },
          {
            "_schema": [
              "Not supporting non file for component"
            ]
          }
        ]
      }
    },
    "score-job": {
      "value": {
        "component": [
          {
            "_schema": [
              "Either version is not provided for component or the id is not valid."
            ]
          },
          {
            "_schema": [
              "Anonymous assets must be defined inline"
            ]
          },
          {
            "_schema": [
              "Not supporting non file for component"
            ]
          }
        ]
      }
    },
    "evaluate-job": {
      "value": {
        "component": [
          {
            "_schema": [
              "Either version is not provided for component or the id is not valid."
            ]
          },
          {
            "_schema": [
              "Anonymous assets must be defined inline"
            ]
          },
          {
            "_schema": [
              "Not supporting non file for component"
            ]
          }
        ]
      }
    }
  }
}

 If the job type is incorrect, change the 'type' property.
manoj@Azure:~/clouddrive/repos/AzureML/bugs/1165955/1b_e2e_registered_components$
```


