
### Pipelines - Getting Started

Pipelines in AzureML lets you sequence a collection of machine learning tasks into a workflow. Data Scientists typically iterate with scripts focusing on individual tasks such as data prepration, training, scoring, etc. When each of these scripts are functionally ready, Pipelines helps connect a collection of such scripts into production quality experiments that can:
* Run in a self-contained way for hours or even days, taking upstream data, processing it and passing it to subsequent scripts without any manual intervention.
* Run on large compute clusters hosted in the cloud compute, that has the processing power to crunch large datasets or thousands of sweeps to find the best models.
* Run in a scheduled fashion to process new data and update ML models, making ML workflows repetable. 
* Generate reproducable results by logging all activity and persisting all outputs including intermediate data to the cloud, helping meet compliance and audit requirements. 

AzureML Piplines can be defined in YAML and run from the CLI, authored in Python or composed in AzureML Studio Designer with drag-n-drop UI. This document focuses on YAML and CLI.


