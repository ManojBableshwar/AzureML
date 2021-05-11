
### Components - Getting Started

Components are the building blocks of Pipelines in Azure Machine Learning. While Jobs enable you to get started quickly with running your scripts, components enable you to create composable and reusable assets. Let's look at a simple example.

```yaml
type: command_component

name: Hello_Python_World
display_name: Hello_Python_World
version: 1

code:
  local_path: ./src

environment:
  docker:
    image: docker.io/python

command: >-
  python hello.py
```

The `code` section points to the location where the script source code is located. The `Environment` refers to the execution environment in which the script will be run. The `command` section defines the actual command string that will be run when this component is executed. You can run a component by referencing it in a Pipeline Job. You can run this simple component with `az ml job create --file pipeline.yml`. The Pipeline Job binds the component to a `compute` on which the the component can run in a `component_job`. Code and sample output is available [here](https://github.com/ManojBableshwar/AzureML/blob/master/samples/2a_basic_component)

```yaml
type: pipeline_job

jobs:
  hello_python_world_job:
    type: component_job
    component: file:./component.yml
    compute:
      target: azureml:ManojCluster
```

A component can take inputs and produce outputs. Inputs can be values such as strings, numbers, etc. or data in a local machine or cloud storage. Outputs can only be data which are typically files written to local directory by the script that then get saved to cloud storage. The type definition of the Inputs and Outputs is defined in the respective `inputs` and `outputs section. They are mapped to the command line parameters of the command in the `command` section. Note that the component only defines the types of Inputs and Outputs. The actual values for the Inputs and Outputs of a Component are provided in the Pipeline Job.

```yaml
type: command_component

name: Hello_Python_World
display_name: Hello_Python_World
version: 1

inputs:
  sample_input_data:
    type: path
  sample_input_string:
    type: string
    default: "hello_python_world"

outputs:
  sample_output_data:
    type: path

code:
  local_path: ./src

environment:
  docker:
    image: docker.io/python

command: >-
  python hello.py --input_data {inputs.sample_input_data} --input_string {inputs.sample_input_string} --output_data {outputs.sample_output_data}

```

Below is a Pipeline Job that assigns values to the Inputs and Outputs of the component. 

```yaml
type: pipeline_job

inputs:
  pipeline_sample_input_data:
    data:
      local_path: ./data
  pipeline_sample_input_string: 'Hello_Pipeline_World'

outputs:
  pipeline_sample_output_data:
    data:
      datastore: azureml:workspaceblobstore

jobs:
  hello_python_world_job:
    type: component_job
    component: file:./component.yml
    compute:
      target: azureml:ManojCluster
    inputs:
      sample_input_data: inputs.pipeline_sample_input_data
      sample_input_string: inputs.pipeline_sample_input_string
    outputs:
      sample_output_data: outputs.pipeline_sample_output_data
```
