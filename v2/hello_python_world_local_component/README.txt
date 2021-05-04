manoj@Azure:~/clouddrive/repos/AzureML/v2/hello_python_world_3may21_local$ ls
hello_pipeline_python.yml  helloworld_component_python.yml  src
manoj@Azure:~/clouddrive/repos/AzureML/v2/hello_python_world_3may21_local$ az ml job create --file hello_pipeline_python.yml --name job-khberhb
Command group 'ml job' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus
datastore_name workspaceblobstore is not a full arm id. Proceed with a shortened name.
Unsupported job type None
manoj@Azure:~/clouddrive/repos/AzureML/v2/hello_python_world_3may21_local$ az ml job show --name job-khberhbCommand group 'ml job' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus
Code: UserError
Message: Job job-khberhb not found.
manoj@Azure:~/clouddrive/repos/AzureML/v2/hello_python_world_3may21_local$ az ml job show --name 4ec4d3d9-844f-4741-a9ba-a891ab1cdb1c
Command group 'ml job' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus
Unsupported job type None
manoj@Azure:~/clouddrive/repos/AzureML/v2/hello_python_world_3may21_local$ az ml job show --name c04c7143-2437-4e28-846b-282c35cdb745
Command group 'ml job' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus
Code: UserError
Message: A job was found, but it is not supported in this API version and cannot be accessed.
manoj@Azure:~/clouddrive/repos/AzureML/v2/hello_python_world_3may21_local$ az ml job show --name 4ec4d3d9-844f-4741-a9ba-a891ab1cdb1c
Command group 'ml job' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus
Unsupported job type None
manoj@Azure:~/clouddrive/repos/AzureML/v2/hello_python_world_3may21_local$
