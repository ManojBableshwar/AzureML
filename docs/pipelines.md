
### Pipelines - Getting Started

Pipelines in AzureML lets you sequence a collection of machine learning tasks into a workflow. Data Scientists typically iterate with scripts focusing on individual tasks such as data prepration, training, scoring, etc. When each of these scripts are functionally ready, Pipelines helps connect a collection of such scripts into production quality experiments that can:
* Run in a self-contained way for hours or even days, taking upstream data, processing it and passing it to subsequent scripts without any manual intervention.
* Run on large compute clusters hosted in the cloud compute, that has the processing power to crunch large datasets or thousands of sweeps to find the best models.
* Run in a scheduled fashion to process new data and update ML models, making ML workflows repetable. 
* Generate reproducable results by logging all activity and persisting all outputs including intermediate data to the cloud, helping meet compliance and audit requirements. 

AzureML Piplines can be defined in YAML and run from the CLI, authored in Python or composed in AzureML Studio Designer with drag-n-drop UI. This document focuses on YAML and CLI.

Below is a simple Pipeline Job that runs 3 Command Component Jobs. The `jobs` section lists the tasks or scripts that run in this Pipeline. A Pipeline Job is flexible in the sense it that can run directly run jobs such as Command Jobs, Sweep Jobs, etc. or it can run Components such as Command Component, Sweep Component, etc. A Job is a one time submission of a script with context such as inputs, compute, environment, etc. A Component is a composable and reusable asset that can be registered with the Workspace and used in any Pipeline Job. See [Components - Getting Started](https://github.com/ManojBableshwar/AzureML/blob/master/docs/components.md) for more details. (NOTE: The current preview supports only Command Components in a Pipeline Job, with support for Command Jobs and other Component types to be added soon.). Since there are no dependencies between the 3 Command Component Jobs, all of them will run concurrently, provided there are sufficient nodes on the Compute Cluster. You can submit this Pipeline Job with the `az ml job create --file <your_pipeline.yml>`. If your Workspace has a different compute cluster than the one mentioned in pipeline.yml, you can either edit the YAML or specify the compute cluster on the command line: `az ml job create --file <your_pipeline.yml> --set compute.cluster=<your_cluster>`. Code and sample output for this example is available [here](https://github.com/ManojBableshwar/AzureML/tree/master/samples/3a_basic_pipeline).

```yaml
type: pipeline_job

compute:
  target: azureml:cpu-cluster

jobs:
  componentA_job:
    type: component_job
    component: file:./componentA.yml
  componentA_job:
    type: component_job
    component: file:./componentB.yml
  componentA_job:
    type: component_job
    component: file:./componentC.yml
```

Let's sequence these Jobs by adding data dependencies between them. 


