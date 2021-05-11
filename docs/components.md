
### Components - Getting Started

Components are the building blocks of Pipelines in Azure Machine Learning. While Jobs enable you to get started quickly with running your scripts, components enable you to create composable and reusable assets. Let's look at a simple example.

```
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

The `code` section points to the location where the script source code is located. The `Environment` refers to the execution environment in which the script will be run. The `command` section defines the actual command string that will be run when this component is executed. You can run a component by referencing it in a Pipeline Job. You can run this simple component with `az ml job create --file pipeline.yml`. Code and sample output is available [here](https://github.com/ManojBableshwar/AzureML/blob/master/samples/2a_basic_component)

```
type: pipeline_job

jobs:
  hello_python_world_job:
    type: component_job
    component: file:./component.yml
    compute:
      target: azureml:ManojCluster
```


