### Setup instructions for Pipeline Job with Command Components preview

Pre-reqs:
1. AzureML Workspce with a compute cluster created. 
2. If you do not have the Azure CLI installed, follow the installation instructions at https://docs.microsoft.com/cli/azure/install-azure-cli. You can use Azure Cloud Shell which has Azure CLI pre-installed: https://docs.microsoft.com/en-us/azure/cloud-shell/quickstart

Steps:

1. Remove any previous extension installations

```
az extension remove -n ml; az extension remove -n azure-cli-ml
```

2. Install the preview AzureML extension.

```
az extension add --source https://azuremlsdktestpypi.blob.core.windows.net/wheels/sdk-cli-v2/ml-0.0.77-py3-none-any.whl --pip-extra-index-urls https://azuremlsdktestpypi.azureedge.net/sdk-cli-v2 -y
```

Check if the installation was successful with `az version`

3. Login with `az login`

4. Set your workspace defaults

```
az config set defaults.workspace="<your_workspace>"
az config set defaults.location="<your_region>"
az config set defaults.group="<your_workspace_resource_group>"
```

5. Make sure your setup is working with either of the list commands: `az ml compute list`, `az ml jobs list`, or `az ml data list`

6. Enable private preview features: `export AZURE_ML_CLI_PRIVATE_FEATURES_ENABLED="true"`

7. Clone this samples repo: 

```
cd $HOME
mkdir repos
cd repos
git clone https://github.com/ManojBableshwar/AzureML.git
```


