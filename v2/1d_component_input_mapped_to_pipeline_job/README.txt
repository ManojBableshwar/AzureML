
=============>>>> Pass <<<<=============
manoj@Azure:~/clouddrive/repos/AzureML/v2/1d_component_input_mapped_to_pipeline_job$ cat hello_pipeline_python.yml
type: pipeline_job

#compute:
#  target: azureml:ManojCluster

inputs:
  pipeline_sample_data:
    data:
      datastore: azureml:workspaceblobstore
      path: az-ml-artifacts/3c233acc7a166896202ebe35aedc2e13/data
  pipeline_sample_string: "hello"

jobs:
  hello_world_component_1:
    type: component_job
    compute:
      target: azureml:ManojCluster
    component: file:./helloworld_component_python.yml
    inputs:
      sample_data: inputs.pipeline_sample_data
      sample_string: inputs.pipeline_sample_string



70_driver_log.txt:
[2021-05-05T05:09:13.925321] Starting Linux command : python hello.py --sample_input_data /mnt/batch/tasks/shared/LS_root/jobs/opendatasetspmworkspace/azureml/3a195ab3-d971-4035-bcc8-d967e509cb93/wd/tmpbvp86k51 --sample_input_string hello
Hello Python World
sample_input_string: hello
sample_input_data mounted path: /mnt/batch/tasks/shared/LS_root/jobs/opendatasetspmworkspace/azureml/3a195ab3-d971-4035-bcc8-d967e509cb93/wd/tmpbvp86k51
mounted_path files: 
['sample1.csv']
reading file: sample1.csv ...
"Month", "Average", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015"
"May",  0.1,  0,  0, 1, 1, 0, 0, 0, 2, 0,  0,  0
"Jun",  0.5,  2,  1, 1, 0, 0, 1, 1, 2, 2,  0,  1
"Jul",  0.7,  5,  1, 1, 2, 0, 1, 3, 0, 2,  2,  1
"Aug",  2.3,  6,  3, 2, 4, 4, 4, 7, 8, 2,  2,  3
"Sep",  3.5,  6,  4, 7, 4, 2, 8, 5, 2, 5,  2,  5
"Oct",  2.0,  8,  0, 1, 3, 2, 5, 1, 5, 2,  3,  0
"Nov",  0.5,  3,  0, 0, 1, 1, 0, 1, 0, 1,  0,  1
"Dec",  0.0,  1,  0, 1, 0, 0, 0, 0, 0, 0,  0,  1

=============>>>> Fail <<<<=============

manoj@Azure:~/clouddrive/repos/AzureML/v2/1d_component_input_mapped_to_pipeline_job$ cat hello_pipeline_python_string_input_with_spaces.yml
type: pipeline_job

#compute:
#  target: azureml:ManojCluster

inputs:
  pipeline_sample_data:
    data:
      datastore: azureml:workspaceblobstore
      path: az-ml-artifacts/3c233acc7a166896202ebe35aedc2e13/data
  pipeline_sample_string: "hello python world"

jobs:
  hello_world_component_1:
    type: component_job
    compute:
      target: azureml:ManojCluster
    component: file:./helloworld_component_python.yml
    inputs:
      sample_data: inputs.pipeline_sample_data
      sample_string: inputs.pipeline_sample_string

70_driver_log.txt:

[2021-05-05T05:09:14.977611] Command finished with return code 0

[2021-05-05T05:10:46.866099] Starting Linux command : python hello.py --sample_input_data /mnt/batch/tasks/shared/LS_root/jobs/opendatasetspmworkspace/azureml/6d14ab5c-5655-4692-970f-905ad8238a69/wd/tmpwtwojjv0 --sample_input_string hello python world
Hello Python World
usage: hello.py [-h] [--sample_input_data SAMPLE_INPUT_DATA]
                [--sample_input_string SAMPLE_INPUT_STRING]
hello.py: error: unrecognized arguments: python world
[2021-05-05T05:10:47.147113] Command finished with return code 2


