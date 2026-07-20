# iikocloud_client.PublicApiInvoiceProcessingInternalTransferApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_inventory_internal_transfer**](PublicApiInvoiceProcessingInternalTransferApi.md#cancel_inventory_internal_transfer) | **POST** /api/inventory/v1/internal_transfer/cancel | Cancel internal transfer act draft
[**create_inventory_internal_transfer**](PublicApiInvoiceProcessingInternalTransferApi.md#create_inventory_internal_transfer) | **POST** /api/inventory/v1/internal_transfer/create | Create internal transfer act
[**get_inventory_internal_transfer**](PublicApiInvoiceProcessingInternalTransferApi.md#get_inventory_internal_transfer) | **POST** /api/inventory/v1/internal_transfer/get | Get internal transfer act by identifier
[**list_inventory_internal_transfers**](PublicApiInvoiceProcessingInternalTransferApi.md#list_inventory_internal_transfers) | **POST** /api/inventory/v1/internal_transfer/list | Export internal transfer acts
[**post_inventory_internal_transfer**](PublicApiInvoiceProcessingInternalTransferApi.md#post_inventory_internal_transfer) | **POST** /api/inventory/v1/internal_transfer/post | Post internal transfer act
[**unpost_inventory_internal_transfer**](PublicApiInvoiceProcessingInternalTransferApi.md#unpost_inventory_internal_transfer) | **POST** /api/inventory/v1/internal_transfer/unpost | Unpost internal transfer act
[**update_inventory_internal_transfer**](PublicApiInvoiceProcessingInternalTransferApi.md#update_inventory_internal_transfer) | **POST** /api/inventory/v1/internal_transfer/update | Edit internal transfer act


# **cancel_inventory_internal_transfer**
> InternalTransferSaveResponse cancel_inventory_internal_transfer(get_by_id_request)

Cancel internal transfer act draft

Changes the internal transfer act status from NEW to CANCELED

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.internal_transfer_save_response import InternalTransferSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingInternalTransferApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document draft cancellation request body

    try:
        # Cancel internal transfer act draft
        api_response = await api_instance.cancel_inventory_internal_transfer(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingInternalTransferApi->cancel_inventory_internal_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingInternalTransferApi->cancel_inventory_internal_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document draft cancellation request body | 

### Return type

[**InternalTransferSaveResponse**](InternalTransferSaveResponse.md)

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

# **create_inventory_internal_transfer**
> InternalTransferSaveResponse create_inventory_internal_transfer(internal_transfer_create_request)

Create internal transfer act

Creates a new internal transfer act

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.internal_transfer_create_request import InternalTransferCreateRequest
from iikocloud_client.models.internal_transfer_save_response import InternalTransferSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingInternalTransferApi(api_client)
    internal_transfer_create_request = iikocloud_client.InternalTransferCreateRequest() # InternalTransferCreateRequest | Document creation request body

    try:
        # Create internal transfer act
        api_response = await api_instance.create_inventory_internal_transfer(internal_transfer_create_request)
        print("The response of PublicApiInvoiceProcessingInternalTransferApi->create_inventory_internal_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingInternalTransferApi->create_inventory_internal_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_transfer_create_request** | [**InternalTransferCreateRequest**](InternalTransferCreateRequest.md)| Document creation request body | 

### Return type

[**InternalTransferSaveResponse**](InternalTransferSaveResponse.md)

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

# **get_inventory_internal_transfer**
> InternalTransferGetResponse get_inventory_internal_transfer(get_by_id_request)

Get internal transfer act by identifier

Gets an internal transfer act by its unique identifier

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.internal_transfer_get_response import InternalTransferGetResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingInternalTransferApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document retrieval by identifier request body

    try:
        # Get internal transfer act by identifier
        api_response = await api_instance.get_inventory_internal_transfer(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingInternalTransferApi->get_inventory_internal_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingInternalTransferApi->get_inventory_internal_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document retrieval by identifier request body | 

### Return type

[**InternalTransferGetResponse**](InternalTransferGetResponse.md)

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
**405** | Method not allowed (POST expected) |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | RMS request error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inventory_internal_transfers**
> List[InternalTransferListItem] list_inventory_internal_transfers(list_request)

Export internal transfer acts

Gets a list of internal transfer acts for the specified period

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.internal_transfer_list_item import InternalTransferListItem
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingInternalTransferApi(api_client)
    list_request = iikocloud_client.ListRequest() # ListRequest | Document list retrieval request body

    try:
        # Export internal transfer acts
        api_response = await api_instance.list_inventory_internal_transfers(list_request)
        print("The response of PublicApiInvoiceProcessingInternalTransferApi->list_inventory_internal_transfers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingInternalTransferApi->list_inventory_internal_transfers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_request** | [**ListRequest**](ListRequest.md)| Document list retrieval request body | 

### Return type

[**List[InternalTransferListItem]**](InternalTransferListItem.md)

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

# **post_inventory_internal_transfer**
> InternalTransferSaveResponse post_inventory_internal_transfer(get_by_id_request)

Post internal transfer act

Changes the internal transfer act status from NEW to PROCESSED

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.internal_transfer_save_response import InternalTransferSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingInternalTransferApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document posting request body

    try:
        # Post internal transfer act
        api_response = await api_instance.post_inventory_internal_transfer(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingInternalTransferApi->post_inventory_internal_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingInternalTransferApi->post_inventory_internal_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document posting request body | 

### Return type

[**InternalTransferSaveResponse**](InternalTransferSaveResponse.md)

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

# **unpost_inventory_internal_transfer**
> InternalTransferSaveResponse unpost_inventory_internal_transfer(get_by_id_request)

Unpost internal transfer act

Changes the internal transfer act status from PROCESSED to NEW

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.internal_transfer_save_response import InternalTransferSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingInternalTransferApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document unposting request body

    try:
        # Unpost internal transfer act
        api_response = await api_instance.unpost_inventory_internal_transfer(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingInternalTransferApi->unpost_inventory_internal_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingInternalTransferApi->unpost_inventory_internal_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document unposting request body | 

### Return type

[**InternalTransferSaveResponse**](InternalTransferSaveResponse.md)

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

# **update_inventory_internal_transfer**
> InternalTransferSaveResponse update_inventory_internal_transfer(internal_transfer_update_request)

Edit internal transfer act

Edits an existing internal transfer act

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.internal_transfer_save_response import InternalTransferSaveResponse
from iikocloud_client.models.internal_transfer_update_request import InternalTransferUpdateRequest
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingInternalTransferApi(api_client)
    internal_transfer_update_request = iikocloud_client.InternalTransferUpdateRequest() # InternalTransferUpdateRequest | Document update request body

    try:
        # Edit internal transfer act
        api_response = await api_instance.update_inventory_internal_transfer(internal_transfer_update_request)
        print("The response of PublicApiInvoiceProcessingInternalTransferApi->update_inventory_internal_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingInternalTransferApi->update_inventory_internal_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_transfer_update_request** | [**InternalTransferUpdateRequest**](InternalTransferUpdateRequest.md)| Document update request body | 

### Return type

[**InternalTransferSaveResponse**](InternalTransferSaveResponse.md)

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

