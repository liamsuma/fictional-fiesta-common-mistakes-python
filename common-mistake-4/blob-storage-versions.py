# Answer Updated for 2019 and going forward 

There are 2 ways to upload and delete a blob, the first using the new `azure-storage-blob` library (2019) and the second using the old `azure-storage` library (pre-2019).

> **Use Method 1 if you are a new user from 2019 onward following the [updated Quick Start guide][1].**

---

## Method 1. Using the new `azure-storage-blob` library (2019)

Uninstall the old `azure-storage` library first if you have installed it, then install the new `azure-storage-blob` library. Use `pip3` for Python 3 or `pip` for Python 2:

```
pip3 uninstall azure-storage
pip3 install azure-storage-blob
```

Depending on your Python version, `pip freeze` or `pip3 freeze` should reveal the following:

```
azure-common==1.1.23
azure-core==1.0.0
azure-nspkg==3.0.2
azure-storage-blob==12.0.0
```
> If you want to upload files and delete blobs using the same client, use `ContainerClient`. The documentation can be found [here][2].

Code for uploading file using `ContainerClient`:

```python3
from azure.storage.blob import ContainerClient

CONNECT_STR = ""
CONTAINER_NAME = ""
input_file_path = "/path/to/your/input_file.csv"
output_blob_name = "output_blob.csv"

container_client = ContainerClient.from_connection_string(conn_str=CONNECT_STR, container_name=CONTAINER_NAME)

# Upload file
with open(input_file_path, "rb") as data:
    container_client.upload_blob(name=output_blob_name, data=data)

```
Code for deleting blob using `ContainerClient`:

```python3
from azure.storage.blob import ContainerClient

CONNECT_STR = ""
CONTAINER_NAME = ""
blob_name = "output_blob.csv"

container_client = ContainerClient.from_connection_string(conn_str=CONNECT_STR, container_name=CONTAINER_NAME)

# Delete blob
container_client.delete_blob(blob=blob_name)
```
> Alternatively, you can use `BlobServiceClient` to upload files as per the [Quick Start guide][1].

Code for uploading file using `BlobServiceClient`:

```python3
from azure.storage.blob import BlobServiceClient

CONNECT_STR = ""
CONTAINER_NAME = ""
input_file_path = "/path/to/your/input_file.csv"
output_blob_name = "output_blob.csv"

blob_service_client = BlobServiceClient.from_connection_string(CONNECT_STR)
blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=output_blob_name)

# Upload file
with open(input_file_path, "rb") as data:
    blob_client.upload_blob(data=data)
```

---

## Method 2. Using the old `azure-storage` library (pre-2019)

Uninstall the new `azure-storage-blob` library first if you have installed it, then install the old `azure-storage` library. Use `pip3` for Python 3 or `pip` for Python 2:

```
pip3 uninstall azure-storage-blob
pip3 install azure-storage
```

Depending on your Python version, `pip freeze` or `pip3 freeze` should reveal the following:

```
azure-common==1.1.23
azure-core==1.0.0
azure-nspkg==3.0.2
azure-storage==0.36.0
```
> We can use `BlockBlobService` client to upload files and delete blobs.

Code for uploading file using `BlockBlobService`:

```python3
from azure.storage.blob import BlockBlobService

AZURE_STORAGE_ACCOUNT_NAME = ""
AZURE_STORAGE_ACCOUNT_KEY = ""
CONTAINER_NAME = ""
input_file_path = "/path/to/your/input_file.csv"
output_blob_name = "output_blob.csv"

block_blob_service = BlockBlobService(account_name=AZURE_STORAGE_ACCOUNT_NAME, account_key=AZURE_STORAGE_ACCOUNT_KEY)

# Upload file
block_blob_service.create_blob_from_path(CONTAINER_NAME, output_blob_name, input_file_path)

```
Code for deleting blob using `BlockBlobService`:

```python3
from azure.storage.blob import BlockBlobService

AZURE_STORAGE_ACCOUNT_NAME = ""
AZURE_STORAGE_ACCOUNT_KEY = ""
CONTAINER_NAME = ""
blob_name = "output_blob.csv"

block_blob_service = BlockBlobService(account_name=AZURE_STORAGE_ACCOUNT_NAME, account_key=AZURE_STORAGE_ACCOUNT_KEY)

# Delete blob
block_blob_service.delete_blob(CONTAINER_NAME, blob_name)
```

---

## Background

As mentioned in this [answer][3], there were breaking changes introduced to the `azure-storage` library since 0.37.0. According to the [change log][4], not only has the namespaces been changed, but the library has also been split into 5 different packages:

1. azure-storage-common
2. azure-storage-blob
3. azure-storage-file
4. azure-storage-queue
5. azure-storage-nspkg

Despite many answers already available on other posts, I wanted to point out that for new users trying this out in 2019 onward, trying to find the correct code for the library is complicated by the fact that many if not most answers offered here on Stackoverflow still reference the old library `azure-storage`, but new users follow the new tutorial by Microsoft updated in May 2019 which uses the new `azure-storage-blob` instead. New users searching for help will inadvertently stumble upon the old answers using the old `azure-storage` library but those do not work for them.


  [1]: https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python
  [2]: https://azuresdkdocs.blob.core.windows.net/$web/python/azure-storage-blob/12.0.0b5/azure.storage.blob.html#azure.storage.blob.ContainerClient
  [3]: https://stackoverflow.com/a/46717244/5305519
  [4]: https://github.com/Azure/azure-storage-python/blob/master/BreakingChanges.md
