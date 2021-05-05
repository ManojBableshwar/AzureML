manoj@Azure:~/clouddrive/repos/AzureML/v2/1e_component_input__output_mapped_to_pipeline_job$ az ml job create --file hello_pipeline_python.yml --name job2
Command group 'ml job' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus
datastore_name workspaceblobstore is not a full arm id. Proceed with a shortened name.
'NoneType' object has no attribute 'target'

70_driver_log.txt:


bash: /azureml-envs/azureml_873581932c94d3f04d256fdaa1d2d7c6/lib/libtinfo.so.5: no version information available (required by bash)
2021/05/05 06:31:48 Starting App Insight Logger for task:  runTaskLet
bash: /azureml-envs/azureml_873581932c94d3f04d256fdaa1d2d7c6/lib/libtinfo.so.5: no version information available (required by bash)
2021/05/05 06:31:48 Attempt 1 of http call to http://10.0.0.6:16384/sendlogstoartifacts/info
2021/05/05 06:31:48 Attempt 1 of http call to http://10.0.0.6:16384/sendlogstoartifacts/status
[2021-05-05T06:31:48.944402] Entering context manager injector.
[context_manager_injector.py] Command line Options: Namespace(inject=['ProjectPythonPath:context_managers.ProjectPythonPath', 'Dataset:context_managers.Datasets', 'TrackUserError:context_managers.TrackUserError', 'UserExceptions:context_managers.UserExceptions'], invocation=['python hello.py --sample_input_data /mnt/batch/tasks/shared/LS_root/jobs/opendatasetspmworkspace/azureml/0e6714ac-5030-42c2-b75a-ca9ba6fef59a/wd/tmpw8lt39bi --sample_input_string hello --sample_input_data DatasetOutputConfig:sample_output'])
Script type = COMMAND
[2021-05-05T06:31:50.209170] Command=python hello.py --sample_input_data /mnt/batch/tasks/shared/LS_root/jobs/opendatasetspmworkspace/azureml/0e6714ac-5030-42c2-b75a-ca9ba6fef59a/wd/tmpw8lt39bi --sample_input_string hello --sample_input_data DatasetOutputConfig:sample_output
[2021-05-05T06:31:50.211674] Command Working Directory=/mnt/batch/tasks/shared/LS_root/jobs/opendatasetspmworkspace/azureml/0e6714ac-5030-42c2-b75a-ca9ba6fef59a/mounts/workspaceblobstore/azureml/0e6714ac-5030-42c2-b75a-ca9ba6fef59a
[2021-05-05T06:31:50.214535] Starting Linux command : python hello.py --sample_input_data /mnt/batch/tasks/shared/LS_root/jobs/opendatasetspmworkspace/azureml/0e6714ac-5030-42c2-b75a-ca9ba6fef59a/wd/tmpw8lt39bi --sample_input_string hello --sample_input_data /mnt/batch/tasks/shared/LS_root/jobs/opendatasetspmworkspace/azureml/0e6714ac-5030-42c2-b75a-ca9ba6fef59a/wd/tmp80jin19j
Hello Python World
sample_input_string: hello
sample_input_data mounted path: /mnt/batch/tasks/shared/LS_root/jobs/opendatasetspmworkspace/azureml/0e6714ac-5030-42c2-b75a-ca9ba6fef59a/wd/tmp80jin19j
sample_output_data mounted path: None
mounted_path files: 
['sample1.csv', 'sample2.csv']
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


reading file: sample2.csv ...
"Month", "Average", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015"
"May",  0.1,  0,  0, 1, 1, 0, 0, 0, 2, 0,  0,  0
"Jun",  0.5,  2,  1, 1, 0, 0, 1, 1, 2, 2,  0,  1
"Jul",  0.7,  5,  1, 1, 2, 0, 1, 3, 0, 2,  2,  1
"Aug",  2.3,  6,  3, 2, 4, 4, 4, 7, 8, 2,  2,  3
"Sep",  3.5,  6,  4, 7, 4, 2, 8, 5, 2, 5,  2,  5
"Oct",  2.0,  8,  0, 1, 3, 2, 5, 1, 5, 2,  3,  0
"Nov",  0.5,  3,  0, 0, 1, 1, 0, 1, 0, 1,  0,  1
"Dec",  0.0,  1,  0, 1, 0, 0, 0, 0, 0, 0,  0,  1


files in sample_output_data mounted path: None before:
['azureml-logs', 'azureml_compute_logs', 'azureml-setup', 'hello.py', 'logs', 'extract_project.success', '.config', 'outputs']
Traceback (most recent call last):
  File "hello.py", line 35, in <module>
    print("Writing file: %s" % os.path.join(args.sample_output_data,"file-" + cur_time_str + ".txt"))
  File "/azureml-envs/azureml_873581932c94d3f04d256fdaa1d2d7c6/lib/python3.6/posixpath.py", line 78, in join
    a = os.fspath(a)
TypeError: expected str, bytes or os.PathLike object, not NoneType
[2021-05-05T06:31:51.093961] Command finished with return code 1


[2021-05-05T06:31:51.095578] The experiment failed with exit code: 1. Finalizing run...
[2021-05-05T06:31:51.096075] Writing error with error_code UserError and error_hierarchy UserError/SystemExit to hosttool error file located at /mnt/batch/tasks/workitems/a4cd3302-367b-45a1-8120-778edf64bf27/job-1/0e6714ac-5030-42c2-b_f8d277a9-812c-43d0-a832-2c5a003eca00/wd/runTaskLetTask_error.json
Starting the daemon thread to refresh tokens in background for process with pid = 80
Traceback (most recent call last):
  File "/mnt/batch/tasks/shared/LS_root/jobs/opendatasetspmworkspace/azureml/0e6714ac-5030-42c2-b75a-ca9ba6fef59a/mounts/workspaceblobstore/azureml/0e6714ac-5030-42c2-b75a-ca9ba6fef59a/azureml-setup/context_manager_injector.py", line 441, in <module>
    execute_with_context(cm_objects, options.invocation)
  File "/mnt/batch/tasks/shared/LS_root/jobs/opendatasetspmworkspace/azureml/0e6714ac-5030-42c2-b75a-ca9ba6fef59a/mounts/workspaceblobstore/azureml/0e6714ac-5030-42c2-b75a-ca9ba6fef59a/azureml-setup/context_manager_injector.py", line 222, in execute_with_context
    process_return_code(signedReturnCode)
  File "/mnt/batch/tasks/shared/LS_root/jobs/opendatasetspmworkspace/azureml/0e6714ac-5030-42c2-b75a-ca9ba6fef59a/mounts/workspaceblobstore/azureml/0e6714ac-5030-42c2-b75a-ca9ba6fef59a/azureml-setup/context_manager_injector.py", line 342, in process_return_code
    sys.exit(returnCode)
SystemExit: 1

[2021-05-05T06:31:51.174536] Finished context manager injector with SystemExit exception.
2021/05/05 06:31:52 Succeeded to parse control script error: /mnt/batch/tasks/workitems/a4cd3302-367b-45a1-8120-778edf64bf27/job-1/0e6714ac-5030-42c2-b_f8d277a9-812c-43d0-a832-2c5a003eca00/wd/runTaskLetTask_error.json to json
2021/05/05 06:31:52 Failed to run the wrapper cmd with err: exit status 1
2021/05/05 06:31:52 Attempt 1 of http call to http://10.0.0.6:16384/sendlogstoartifacts/status
2021/05/05 06:31:52 mpirun version string: {
Intel(R) MPI Library for Linux* OS, Version 2018 Update 3 Build 20180411 (id: 18329)
Copyright 2003-2018 Intel Corporation.
}
2021/05/05 06:31:52 MPI publisher: intel ; version: 2018
2021/05/05 06:31:52 Not exporting to RunHistory as the exporter is either stopped or there is no data.
Stopped: false
OriginalData: 3
FilteredData: 0.
2021/05/05 06:31:52 Process Exiting with Code:  1
2021/05/05 06:31:52 All App Insights Logs was send successfully

