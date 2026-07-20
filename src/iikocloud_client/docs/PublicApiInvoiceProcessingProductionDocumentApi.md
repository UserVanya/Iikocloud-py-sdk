# iikocloud_client.PublicApiInvoiceProcessingProductionDocumentApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_inventory_production_document**](PublicApiInvoiceProcessingProductionDocumentApi.md#cancel_inventory_production_document) | **POST** /api/inventory/v1/production_document/cancel | Cancel production document draft
[**create_inventory_production_document**](PublicApiInvoiceProcessingProductionDocumentApi.md#create_inventory_production_document) | **POST** /api/inventory/v1/production_document/create | Create production document
[**get_inventory_production_document**](PublicApiInvoiceProcessingProductionDocumentApi.md#get_inventory_production_document) | **POST** /api/inventory/v1/production_document/get | Get production document
[**list_inventory_production_documents**](PublicApiInvoiceProcessingProductionDocumentApi.md#list_inventory_production_documents) | **POST** /api/inventory/v1/production_document/list | Export production documents
[**post_inventory_production_document**](PublicApiInvoiceProcessingProductionDocumentApi.md#post_inventory_production_document) | **POST** /api/inventory/v1/production_document/post | Post production document
[**unpost_inventory_production_document**](PublicApiInvoiceProcessingProductionDocumentApi.md#unpost_inventory_production_document) | **POST** /api/inventory/v1/production_document/unpost | Unpost production document
[**update_inventory_production_document**](PublicApiInvoiceProcessingProductionDocumentApi.md#update_inventory_production_document) | **POST** /api/inventory/v1/production_document/update | Edit production document


# **cancel_inventory_production_document**
> ProductionDocumentSaveResponse cancel_inventory_production_document(get_by_id_request)

Cancel production document draft

Changes the production document status from NEW to CANCELED

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.production_document_save_response import ProductionDocumentSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingProductionDocumentApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document draft cancellation request body

    try:
        # Cancel production document draft
        api_response = await api_instance.cancel_inventory_production_document(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingProductionDocumentApi->cancel_inventory_production_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingProductionDocumentApi->cancel_inventory_production_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document draft cancellation request body | 

### Return type

[**ProductionDocumentSaveResponse**](ProductionDocumentSaveResponse.md)

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

# **create_inventory_production_document**
> ProductionDocumentSaveResponse create_inventory_production_document(production_document_create_request)

Create production document

Creates a new production document in RMS

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.production_document_create_request import ProductionDocumentCreateRequest
from iikocloud_client.models.production_document_save_response import ProductionDocumentSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingProductionDocumentApi(api_client)
    production_document_create_request = iikocloud_client.ProductionDocumentCreateRequest() # ProductionDocumentCreateRequest | Document creation request body

    try:
        # Create production document
        api_response = await api_instance.create_inventory_production_document(production_document_create_request)
        print("The response of PublicApiInvoiceProcessingProductionDocumentApi->create_inventory_production_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingProductionDocumentApi->create_inventory_production_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_document_create_request** | [**ProductionDocumentCreateRequest**](ProductionDocumentCreateRequest.md)| Document creation request body | 

### Return type

[**ProductionDocumentSaveResponse**](ProductionDocumentSaveResponse.md)

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
**405** | Method not allowed (POST expected) |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_production_document**
> ProductionDocumentGetResponse get_inventory_production_document(get_by_id_request)

Get production document

Gets a production document by identifier from RMS

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.production_document_get_response import ProductionDocumentGetResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingProductionDocumentApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document retrieval by identifier request body

    try:
        # Get production document
        api_response = await api_instance.get_inventory_production_document(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingProductionDocumentApi->get_inventory_production_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingProductionDocumentApi->get_inventory_production_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document retrieval by identifier request body | 

### Return type

[**ProductionDocumentGetResponse**](ProductionDocumentGetResponse.md)

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

# **list_inventory_production_documents**
> List[ProductionDocumentListItem] list_inventory_production_documents(list_request)

Export production documents

Exports production documents from RMS for the specified period

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.list_request import ListRequest
from iikocloud_client.models.production_document_list_item import ProductionDocumentListItem
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingProductionDocumentApi(api_client)
    list_request = iikocloud_client.ListRequest() # ListRequest | Document list retrieval request body

    try:
        # Export production documents
        api_response = await api_instance.list_inventory_production_documents(list_request)
        print("The response of PublicApiInvoiceProcessingProductionDocumentApi->list_inventory_production_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingProductionDocumentApi->list_inventory_production_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_request** | [**ListRequest**](ListRequest.md)| Document list retrieval request body | 

### Return type

[**List[ProductionDocumentListItem]**](ProductionDocumentListItem.md)

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

# **post_inventory_production_document**
> ProductionDocumentSaveResponse post_inventory_production_document(get_by_id_request)

Post production document

Changes the production document status from NEW to PROCESSED

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.production_document_save_response import ProductionDocumentSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingProductionDocumentApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document posting request body

    try:
        # Post production document
        api_response = await api_instance.post_inventory_production_document(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingProductionDocumentApi->post_inventory_production_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingProductionDocumentApi->post_inventory_production_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document posting request body | 

### Return type

[**ProductionDocumentSaveResponse**](ProductionDocumentSaveResponse.md)

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

# **unpost_inventory_production_document**
> ProductionDocumentSaveResponse unpost_inventory_production_document(get_by_id_request)

Unpost production document

Changes the production document status from PROCESSED to NEW

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.production_document_save_response import ProductionDocumentSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingProductionDocumentApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document unposting request body

    try:
        # Unpost production document
        api_response = await api_instance.unpost_inventory_production_document(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingProductionDocumentApi->unpost_inventory_production_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingProductionDocumentApi->unpost_inventory_production_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document unposting request body | 

### Return type

[**ProductionDocumentSaveResponse**](ProductionDocumentSaveResponse.md)

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

# **update_inventory_production_document**
> ProductionDocumentSaveResponse update_inventory_production_document(production_document_update_request)

Edit production document

Edits an existing production document in RMS

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.production_document_save_response import ProductionDocumentSaveResponse
from iikocloud_client.models.production_document_update_request import ProductionDocumentUpdateRequest
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingProductionDocumentApi(api_client)
    production_document_update_request = iikocloud_client.ProductionDocumentUpdateRequest() # ProductionDocumentUpdateRequest | Document update request body

    try:
        # Edit production document
        api_response = await api_instance.update_inventory_production_document(production_document_update_request)
        print("The response of PublicApiInvoiceProcessingProductionDocumentApi->update_inventory_production_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingProductionDocumentApi->update_inventory_production_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_document_update_request** | [**ProductionDocumentUpdateRequest**](ProductionDocumentUpdateRequest.md)| Document update request body | 

### Return type

[**ProductionDocumentSaveResponse**](ProductionDocumentSaveResponse.md)

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
**405** | Method not allowed (POST expected) |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

