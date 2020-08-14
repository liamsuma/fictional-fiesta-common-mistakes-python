# Basically this script points out the differences between V11 Python SDK and V12 Python SDK 

# V12 uses azure-storage-blob library 
# V11 used azure-storage libray 
# These two versions can't communcate interchangeably

# ==================================== Method 1 - V12 version (Preferred) ==================================

# Code for uploading file using ContainerClient module 

from azure.storage.blob import ContainerClient

CONNECT_STR = "<connection string>"
CONTAINER_NAME = "abc"
input_file_path = "/path/to/your/input_file" # This could be csv or pdf
output_blob_name = "output_blob.csv"

container_client = ContainerClient.from_connection_string(conn_str=CONNECT_STR, container_name=CONTAINER_NAME)

# Upload file
with open(input_file_path, "rb") as data:
    container_client.upload_blob(name=output_blob_name, data=data)
    
# Code for deleting blob using ContainerClient

from azure.storage.blob import ContainerClient

CONNECT_STR = "<connection string>"
CONTAINER_NAME = "abc"
blob_name = "output_blob.csv"

container_client = ContainerClient.from_connection_string(conn_str=CONNECT_STR, container_name=CONTAINER_NAME)

# Delete blob
container_client.delete_blob(blob=blob_name)

# ======================== Alternation by using BlobServiceClient =============================================

from azure.storage.blob import BlobServiceClient

CONNECT_STR = "<connection string>"
CONTAINER_NAME = "abc"
input_file_path = "/path/to/your/input_file" # Again this could be csv or pdf 
output_blob_name = "output_blob.csv"

blob_service_client = BlobServiceClient.from_connection_string(CONNECT_STR)
blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=output_blob_name)

# Upload file
with open(input_file_path, "rb") as data:
    blob_client.upload_blob(data=data)

# ============================= Method 2 - V11 version (pre-2019) =============================================
# Code for uploading file using BlockBlobService
# This module will not work in V12 

from azure.storage.blob import BlockBlobService

AZURE_STORAGE_ACCOUNT_NAME = "" # de-compose from connection string 
AZURE_STORAGE_ACCOUNT_KEY = "" # de-compose from connection string 
CONTAINER_NAME = "abc"
input_file_path = "/path/to/your/input_file" # csv or pdf 
output_blob_name = "output_blob.csv"

block_blob_service = BlockBlobService(account_name=AZURE_STORAGE_ACCOUNT_NAME, account_key=AZURE_STORAGE_ACCOUNT_KEY)

# Upload file
block_blob_service.create_blob_from_path(CONTAINER_NAME, output_blob_name, input_file_path)

# Code for deleting blob using BlockBlobService 

from azure.storage.blob import BlockBlobService

AZURE_STORAGE_ACCOUNT_NAME = "" # de-compose from connection string 
AZURE_STORAGE_ACCOUNT_KEY = "" # de-compose from connection string 
CONTAINER_NAME = "abc"
blob_name = "output_blob.csv"

block_blob_service = BlockBlobService(account_name=AZURE_STORAGE_ACCOUNT_NAME, account_key=AZURE_STORAGE_ACCOUNT_KEY)

# Delete blob
block_blob_service.delete_blob(CONTAINER_NAME, blob_name)
