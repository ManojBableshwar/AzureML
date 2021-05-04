manoj@Azure:~/clouddrive/repos/AzureML/v2/hello_python_world_data_input_output$ az ml data create --file data.yml
Command group 'ml data' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus
datastore_name workspaceblobstore is not a full arm id. Proceed with a shortened name.
Uploading data: 100%|██████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 1272.93it/s]
{
  "creation_context": {
    "created_at": "2021-05-04T01:03:15.336980+00:00",
    "created_by": "Manoj Bableshwar",
    "created_by_type": "User",
    "last_modified_at": "2021-05-04T01:03:15.336980+00:00",
    "last_modified_by": "Manoj Bableshwar",
    "last_modified_by_type": "User"
  },
  "datastore": "azureml:/subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/resourceGroups/OpenDatasetsPMRG/providers/Microsoft.MachineLearningServices/workspaces/OpenDatasetsPMWorkspace/datastores/workspaceblobstore",
  "description": "sample dataset",
  "id": "/subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/resourceGroups/OpenDatasetsPMRG/providers/Microsoft.MachineLearningServices/workspaces/OpenDatasetsPMWorkspace/data/sampledata/versions/1",
  "name": "sampledata",
  "path": "az-ml-artifacts/3c233acc7a166896202ebe35aedc2e13/data",
  "resourceGroup": "OpenDatasetsPMRG",
  "tags": {},
  "version": 1
}

manoj@Azure:~/clouddrive/repos/AzureML/v2/hello_python_world_data_input_output$ az ml data show --name sampledata --version 1
Command group 'ml data' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus
{
  "creation_context": {
    "created_at": "2021-05-04T01:03:15.336980+00:00",
    "created_by": "Manoj Bableshwar",
    "created_by_type": "User",
    "last_modified_at": "2021-05-04T01:03:15.336980+00:00",
    "last_modified_by": "Manoj Bableshwar",
    "last_modified_by_type": "User"
  },
  "datastore": "azureml:/subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/resourceGroups/OpenDatasetsPMRG/providers/Microsoft.MachineLearningServices/workspaces/OpenDatasetsPMWorkspace/datastores/workspaceblobstore",
  "description": "sample dataset",
  "id": "/subscriptions/21d8f407-c4c4-452e-87a4-e609bfb86248/resourceGroups/OpenDatasetsPMRG/providers/Microsoft.MachineLearningServices/workspaces/OpenDatasetsPMWorkspace/data/sampledata/versions/1",
  "name": "sampledata",
  "path": "az-ml-artifacts/3c233acc7a166896202ebe35aedc2e13/data",
  "resourceGroup": "OpenDatasetsPMRG",
  "tags": {},
  "version": 1
}

manoj@Azure:~/clouddrive/repos/AzureML/v2/hello_python_world_data_input_output$ az ml job create --file hello_pipeline_python.yml --name job2
Command group 'ml job' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus
datastore_name workspaceblobstore is not a full arm id. Proceed with a shortened name.
Code: UserError
Message: Pipeline job: ComponentJob does not support ComponentJobInput.InputData.DatasetId.

