# iikocloud_client.PublicApiInvoiceProcessingDisassembleDocumentApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_inventory_disassemble_document**](PublicApiInvoiceProcessingDisassembleDocumentApi.md#cancel_inventory_disassemble_document) | **POST** /api/inventory/v1/disassemble_document/cancel | Cancel disassemble document draft
[**create_inventory_disassemble_document**](PublicApiInvoiceProcessingDisassembleDocumentApi.md#create_inventory_disassemble_document) | **POST** /api/inventory/v1/disassemble_document/create | Create disassemble document
[**get_inventory_disassemble_document**](PublicApiInvoiceProcessingDisassembleDocumentApi.md#get_inventory_disassemble_document) | **POST** /api/inventory/v1/disassemble_document/get | Get disassemble document by identifier
[**list_inventory_disassemble_documents**](PublicApiInvoiceProcessingDisassembleDocumentApi.md#list_inventory_disassemble_documents) | **POST** /api/inventory/v1/disassemble_document/list | Export disassemble documents
[**post_inventory_disassemble_document**](PublicApiInvoiceProcessingDisassembleDocumentApi.md#post_inventory_disassemble_document) | **POST** /api/inventory/v1/disassemble_document/post | Post disassemble document
[**unpost_inventory_disassemble_document**](PublicApiInvoiceProcessingDisassembleDocumentApi.md#unpost_inventory_disassemble_document) | **POST** /api/inventory/v1/disassemble_document/unpost | Unpost disassemble document
[**update_inventory_disassemble_document**](PublicApiInvoiceProcessingDisassembleDocumentApi.md#update_inventory_disassemble_document) | **POST** /api/inventory/v1/disassemble_document/update | Edit disassemble document


# **cancel_inventory_disassemble_document**
> DisassembleDocumentSaveResponse cancel_inventory_disassemble_document(get_by_id_request)

Cancel disassemble document draft

Changes the disassemble document status from NEW to CANCELED

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.disassemble_document_save_response import DisassembleDocumentSaveResponse
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.PublicApiInvoiceProcessingDisassembleDocumentApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document draft cancellation request body

    try:
        # Cancel disassemble document draft
        api_response = await api_instance.cancel_inventory_disassemble_document(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingDisassembleDocumentApi->cancel_inventory_disassemble_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingDisassembleDocumentApi->cancel_inventory_disassemble_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document draft cancellation request body | 

### Return type

[**DisassembleDocumentSaveResponse**](DisassembleDocumentSaveResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request (validation/invalid JSON) |  -  |
**401** | Unauthorized |  -  |
**405** | Method not allowed (POST expected) |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_inventory_disassemble_document**
> DisassembleDocumentSaveResponse create_inventory_disassemble_document(disassemble_document_create_request)

Create disassemble document

Creates a disassemble document from request parameters

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.disassemble_document_create_request import DisassembleDocumentCreateRequest
from iikocloud_client.models.disassemble_document_save_response import DisassembleDocumentSaveResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.PublicApiInvoiceProcessingDisassembleDocumentApi(api_client)
    disassemble_document_create_request = iikocloud_client.DisassembleDocumentCreateRequest() # DisassembleDocumentCreateRequest | Document creation request body

    try:
        # Create disassemble document
        api_response = await api_instance.create_inventory_disassemble_document(disassemble_document_create_request)
        print("The response of PublicApiInvoiceProcessingDisassembleDocumentApi->create_inventory_disassemble_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingDisassembleDocumentApi->create_inventory_disassemble_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disassemble_document_create_request** | [**DisassembleDocumentCreateRequest**](DisassembleDocumentCreateRequest.md)| Document creation request body | 

### Return type

[**DisassembleDocumentSaveResponse**](DisassembleDocumentSaveResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created |  -  |
**400** | Invalid request (validation/empty body/invalid JSON) |  -  |
**401** | Unauthorized |  -  |
**403** | Access forbidden |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_disassemble_document**
> DisassembleDocumentGetResponse get_inventory_disassemble_document(get_by_id_request)

Get disassemble document by identifier

Returns a disassemble document by identifier

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.disassemble_document_get_response import DisassembleDocumentGetResponse
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.PublicApiInvoiceProcessingDisassembleDocumentApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document retrieval by identifier request body

    try:
        # Get disassemble document by identifier
        api_response = await api_instance.get_inventory_disassemble_document(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingDisassembleDocumentApi->get_inventory_disassemble_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingDisassembleDocumentApi->get_inventory_disassemble_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document retrieval by identifier request body | 

### Return type

[**DisassembleDocumentGetResponse**](DisassembleDocumentGetResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request (validation/invalid JSON) |  -  |
**401** | Unauthorized |  -  |
**403** | Access forbidden |  -  |
**404** | Document not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inventory_disassemble_documents**
> List[DisassembleDocumentListItem] list_inventory_disassemble_documents(list_request)

Export disassemble documents

Exports disassemble documents from RMS for the specified period

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.disassemble_document_list_item import DisassembleDocumentListItem
from iikocloud_client.models.list_request import ListRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.PublicApiInvoiceProcessingDisassembleDocumentApi(api_client)
    list_request = iikocloud_client.ListRequest() # ListRequest | Document list retrieval request body

    try:
        # Export disassemble documents
        api_response = await api_instance.list_inventory_disassemble_documents(list_request)
        print("The response of PublicApiInvoiceProcessingDisassembleDocumentApi->list_inventory_disassemble_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingDisassembleDocumentApi->list_inventory_disassemble_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_request** | [**ListRequest**](ListRequest.md)| Document list retrieval request body | 

### Return type

[**List[DisassembleDocumentListItem]**](DisassembleDocumentListItem.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request (validation/invalid JSON) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_inventory_disassemble_document**
> DisassembleDocumentSaveResponse post_inventory_disassemble_document(get_by_id_request)

Post disassemble document

Changes the disassemble document status from NEW to PROCESSED

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.disassemble_document_save_response import DisassembleDocumentSaveResponse
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.PublicApiInvoiceProcessingDisassembleDocumentApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document posting request body

    try:
        # Post disassemble document
        api_response = await api_instance.post_inventory_disassemble_document(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingDisassembleDocumentApi->post_inventory_disassemble_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingDisassembleDocumentApi->post_inventory_disassemble_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document posting request body | 

### Return type

[**DisassembleDocumentSaveResponse**](DisassembleDocumentSaveResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request (validation/invalid JSON) |  -  |
**401** | Unauthorized |  -  |
**405** | Method not allowed (POST expected) |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpost_inventory_disassemble_document**
> DisassembleDocumentSaveResponse unpost_inventory_disassemble_document(get_by_id_request)

Unpost disassemble document

Changes the disassemble document status from PROCESSED to NEW

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.disassemble_document_save_response import DisassembleDocumentSaveResponse
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.PublicApiInvoiceProcessingDisassembleDocumentApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document unposting request body

    try:
        # Unpost disassemble document
        api_response = await api_instance.unpost_inventory_disassemble_document(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingDisassembleDocumentApi->unpost_inventory_disassemble_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingDisassembleDocumentApi->unpost_inventory_disassemble_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document unposting request body | 

### Return type

[**DisassembleDocumentSaveResponse**](DisassembleDocumentSaveResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request (validation/invalid JSON) |  -  |
**401** | Unauthorized |  -  |
**405** | Method not allowed (POST expected) |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inventory_disassemble_document**
> DisassembleDocumentSaveResponse update_inventory_disassemble_document(disassemble_document_update_request)

Edit disassemble document

Updates a disassemble document from request parameters

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.disassemble_document_save_response import DisassembleDocumentSaveResponse
from iikocloud_client.models.disassemble_document_update_request import DisassembleDocumentUpdateRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.PublicApiInvoiceProcessingDisassembleDocumentApi(api_client)
    disassemble_document_update_request = iikocloud_client.DisassembleDocumentUpdateRequest() # DisassembleDocumentUpdateRequest | Document update request body

    try:
        # Edit disassemble document
        api_response = await api_instance.update_inventory_disassemble_document(disassemble_document_update_request)
        print("The response of PublicApiInvoiceProcessingDisassembleDocumentApi->update_inventory_disassemble_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingDisassembleDocumentApi->update_inventory_disassemble_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disassemble_document_update_request** | [**DisassembleDocumentUpdateRequest**](DisassembleDocumentUpdateRequest.md)| Document update request body | 

### Return type

[**DisassembleDocumentSaveResponse**](DisassembleDocumentSaveResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated |  -  |
**400** | Invalid request (validation/empty body/invalid JSON/document not found) |  -  |
**401** | Unauthorized |  -  |
**403** | Access forbidden |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

