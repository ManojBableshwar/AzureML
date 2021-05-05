70_driver_log

bash: /azureml-envs/azureml_873581932c94d3f04d256fdaa1d2d7c6/lib/libtinfo.so.5: no version information available (required by bash)
2021/05/05 06:41:40 Starting App Insight Logger for task:  runTaskLet
bash: /azureml-envs/azureml_873581932c94d3f04d256fdaa1d2d7c6/lib/libtinfo.so.5: no version information available (required by bash)
2021/05/05 06:41:40 Attempt 1 of http call to http://10.0.0.6:16384/sendlogstoartifacts/info
2021/05/05 06:41:40 Attempt 1 of http call to http://10.0.0.6:16384/sendlogstoartifacts/status
[2021-05-05T06:41:40.790782] Entering context manager injector.
[context_manager_injector.py] Command line Options: Namespace(inject=['ProjectPythonPath:context_managers.ProjectPythonPath', 'Dataset:context_managers.Datasets', 'TrackUserError:context_managers.TrackUserError', 'UserExceptions:context_managers.UserExceptions'], invocation=['python hello.py --sample_input_data /mnt/batch/tasks/shared/LS_root/jobs/opendatasetspmworkspace/azureml/8a4a9fb4-e9f5-4527-bb9f-9916c3739be8/wd/tmprddnqazo --sample_input_string hello --sample_output_data DatasetOutputConfig:sample_output'])
Script type = COMMAND
[2021-05-05T06:41:42.237729] Command=python hello.py --sample_input_data /mnt/batch/tasks/shared/LS_root/jobs/opendatasetspmworkspace/azureml/8a4a9fb4-e9f5-4527-bb9f-9916c3739be8/wd/tmprddnqazo --sample_input_string hello --sample_output_data DatasetOutputConfig:sample_output
[2021-05-05T06:41:42.240602] Command Working Directory=/mnt/batch/tasks/shared/LS_root/jobs/opendatasetspmworkspace/azureml/8a4a9fb4-e9f5-4527-bb9f-9916c3739be8/mounts/workspaceblobstore/azureml/8a4a9fb4-e9f5-4527-bb9f-9916c3739be8
[2021-05-05T06:41:42.244875] Starting Linux command : python hello.py --sample_input_data /mnt/batch/tasks/shared/LS_root/jobs/opendatasetspmworkspace/azureml/8a4a9fb4-e9f5-4527-bb9f-9916c3739be8/wd/tmprddnqazo --sample_input_string hello --sample_output_data /mnt/batch/tasks/shared/LS_root/jobs/opendatasetspmworkspace/azureml/8a4a9fb4-e9f5-4527-bb9f-9916c3739be8/wd/tmpytc2z3zb
Hello Python World
sample_input_string: hello
sample_input_data mounted path: /mnt/batch/tasks/shared/LS_root/jobs/opendatasetspmworkspace/azureml/8a4a9fb4-e9f5-4527-bb9f-9916c3739be8/wd/tmprddnqazo
sample_output_data mounted path: /mnt/batch/tasks/shared/LS_root/jobs/opendatasetspmworkspace/azureml/8a4a9fb4-e9f5-4527-bb9f-9916c3739be8/wd/tmpytc2z3zb
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


files in sample_output_data mounted path: /mnt/batch/tasks/shared/LS_root/jobs/opendatasetspmworkspace/azureml/8a4a9fb4-e9f5-4527-bb9f-9916c3739be8/wd/tmpytc2z3zb before:
['sample1.csv', 'sample2.csv']
Writing file: /mnt/batch/tasks/shared/LS_root/jobs/opendatasetspmworkspace/azureml/8a4a9fb4-e9f5-4527-bb9f-9916c3739be8/wd/tmpytc2z3zb/file-May-05-2021-06-41-43.txt
files in sample_output_data mounted path: /mnt/batch/tasks/shared/LS_root/jobs/opendatasetspmworkspace/azureml/8a4a9fb4-e9f5-4527-bb9f-9916c3739be8/wd/tmpytc2z3zb after:
['file-May-05-2021-06-41-43.txt', 'sample1.csv', 'sample2.csv']
[2021-05-05T06:41:43.773808] Command finished with return code 0


[2021-05-05T06:41:43.774620] The experiment completed successfully. Finalizing run...
[2021-05-05T06:41:43.775009] Finished context manager injector.
2021/05/05 06:41:44 Attempt 1 of http call to http://10.0.0.6:16384/sendlogstoartifacts/status
2021/05/05 06:41:44 Not exporting to RunHistory as the exporter is either stopped or there is no data.
Stopped: false
OriginalData: 3
FilteredData: 0.
2021/05/05 06:41:44 Process Exiting with Code:  0
2021/05/05 06:41:45 All App Insights Logs was send successfully

