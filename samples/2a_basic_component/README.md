
This is a simple component with the corresponding pipeline job. 

```
manoj@Azure:~/clouddrive/repos/AzureML/samples/2a_basic_component$ az ml  job create --file pipeline.ymlCommand group 'ml job' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus
Uploading src: 100%|██████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 1092.55it/s]
Custom pipeline job names are not supported yet. Please refer to the created pipeline job using the name: c9069e5c-114a-4fe7-8329-5dc7967e80c7
{
  "creation_context": {
    "created_at": "2021-05-11T05:07:19.196969+00:00",
    "created_by": "Manoj Bableshwar",
    "created_by_type": "User"
  },
  "defaults": {
    "component_job": {}
  },
  "experiment_name": "2a_basic_component",
  "id": "azureml:/subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/resourceGroups/OpenDatasetsPMRG/providers/Microsoft.MachineLearningServices/workspaces/OpenDatasetsPMWorkspace/jobs/c9069e5c-114a-4fe7-8329-5dc7967e80c7",
  "inputs": {},
  "interaction_endpoints": {
    "Studio": {
      "endpoint": "https://ml.azure.com/runs/c9069e5c-114a-4fe7-8329-5dc7967e80c7?wsid=/subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/resourcegroups/OpenDatasetsPMRG/workspaces/OpenDatasetsPMWorkspace&tid=72f988bf-86f1-41af-91ab-2d7cd011db47"
    },
    "Tracking": {
      "endpoint": "azureml://eastus2.api.azureml.ms/mlflow/v1.0/subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/resourceGroups/OpenDatasetsPMRG/providers/Microsoft.MachineLearningServices/workspaces/OpenDatasetsPMWorkspace?"
    }
  },
  "jobs": {
    "hello_python_world_job": {
      "component": "azureml:dbc3e54f-43f8-46f9-a2db-2e760b39cc18:1",
      "compute": {
        "target": "azureml:ManojCluster"
      },
      "inputs": {},
      "outputs": {},
      "type": "component_job"
    }
  },
  "name": "c9069e5c-114a-4fe7-8329-5dc7967e80c7",
  "outputs": {},
  "properties": {
    "azureml.parameters": "{}",
    "azureml.runsource": "azureml.PipelineRun",
    "runSource": "MFE",
    "runType": "HTTP"
  },
  "resourceGroup": "OpenDatasetsPMRG",
  "status": "Preparing",
  "tags": {
    "azureml.pipelineComponent": "pipelinerun"
  },
  "type": "pipeline_job"
}
```
