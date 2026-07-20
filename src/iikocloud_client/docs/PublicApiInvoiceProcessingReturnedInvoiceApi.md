# iikocloud_client.PublicApiInvoiceProcessingReturnedInvoiceApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_inventory_returned_invoice**](PublicApiInvoiceProcessingReturnedInvoiceApi.md#cancel_inventory_returned_invoice) | **POST** /api/inventory/v1/returned_invoice/cancel | Cancel returned invoice draft
[**create_inventory_returned_invoice**](PublicApiInvoiceProcessingReturnedInvoiceApi.md#create_inventory_returned_invoice) | **POST** /api/inventory/v1/returned_invoice/create | Create returned invoice
[**get_inventory_returned_invoice**](PublicApiInvoiceProcessingReturnedInvoiceApi.md#get_inventory_returned_invoice) | **POST** /api/inventory/v1/returned_invoice/get | Get returned invoice by identifier
[**list_inventory_returned_invoices**](PublicApiInvoiceProcessingReturnedInvoiceApi.md#list_inventory_returned_invoices) | **POST** /api/inventory/v1/returned_invoice/list | Export returned invoices
[**post_inventory_returned_invoice**](PublicApiInvoiceProcessingReturnedInvoiceApi.md#post_inventory_returned_invoice) | **POST** /api/inventory/v1/returned_invoice/post | Post returned invoice
[**unpost_inventory_returned_invoice**](PublicApiInvoiceProcessingReturnedInvoiceApi.md#unpost_inventory_returned_invoice) | **POST** /api/inventory/v1/returned_invoice/unpost | Unpost returned invoice
[**update_inventory_returned_invoice**](PublicApiInvoiceProcessingReturnedInvoiceApi.md#update_inventory_returned_invoice) | **POST** /api/inventory/v1/returned_invoice/update | Edit returned invoice


# **cancel_inventory_returned_invoice**
> ReturnedInvoiceSaveResponse cancel_inventory_returned_invoice(get_by_id_request)

Cancel returned invoice draft

Changes the returned invoice status from NEW to CANCELED

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.returned_invoice_save_response import ReturnedInvoiceSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingReturnedInvoiceApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document draft cancellation request body

    try:
        # Cancel returned invoice draft
        api_response = await api_instance.cancel_inventory_returned_invoice(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingReturnedInvoiceApi->cancel_inventory_returned_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingReturnedInvoiceApi->cancel_inventory_returned_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document draft cancellation request body | 

### Return type

[**ReturnedInvoiceSaveResponse**](ReturnedInvoiceSaveResponse.md)

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

# **create_inventory_returned_invoice**
> ReturnedInvoiceSaveResponse create_inventory_returned_invoice(returned_invoice_create_request)

Create returned invoice

Creates a returned invoice from request parameters

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.returned_invoice_create_request import ReturnedInvoiceCreateRequest
from iikocloud_client.models.returned_invoice_save_response import ReturnedInvoiceSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingReturnedInvoiceApi(api_client)
    returned_invoice_create_request = iikocloud_client.ReturnedInvoiceCreateRequest() # ReturnedInvoiceCreateRequest | Document creation request body

    try:
        # Create returned invoice
        api_response = await api_instance.create_inventory_returned_invoice(returned_invoice_create_request)
        print("The response of PublicApiInvoiceProcessingReturnedInvoiceApi->create_inventory_returned_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingReturnedInvoiceApi->create_inventory_returned_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returned_invoice_create_request** | [**ReturnedInvoiceCreateRequest**](ReturnedInvoiceCreateRequest.md)| Document creation request body | 

### Return type

[**ReturnedInvoiceSaveResponse**](ReturnedInvoiceSaveResponse.md)

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

# **get_inventory_returned_invoice**
> ReturnedInvoiceGetResponse get_inventory_returned_invoice(get_by_id_request)

Get returned invoice by identifier

Returns a returned invoice by identifier

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.returned_invoice_get_response import ReturnedInvoiceGetResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingReturnedInvoiceApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document retrieval by identifier request body

    try:
        # Get returned invoice by identifier
        api_response = await api_instance.get_inventory_returned_invoice(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingReturnedInvoiceApi->get_inventory_returned_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingReturnedInvoiceApi->get_inventory_returned_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document retrieval by identifier request body | 

### Return type

[**ReturnedInvoiceGetResponse**](ReturnedInvoiceGetResponse.md)

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
**404** | Document not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inventory_returned_invoices**
> List[ReturnedInvoiceListItem] list_inventory_returned_invoices(list_request)

Export returned invoices

Exports returned invoices from RMS for the specified period

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.list_request import ListRequest
from iikocloud_client.models.returned_invoice_list_item import ReturnedInvoiceListItem
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingReturnedInvoiceApi(api_client)
    list_request = iikocloud_client.ListRequest() # ListRequest | Document list retrieval request body

    try:
        # Export returned invoices
        api_response = await api_instance.list_inventory_returned_invoices(list_request)
        print("The response of PublicApiInvoiceProcessingReturnedInvoiceApi->list_inventory_returned_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingReturnedInvoiceApi->list_inventory_returned_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_request** | [**ListRequest**](ListRequest.md)| Document list retrieval request body | 

### Return type

[**List[ReturnedInvoiceListItem]**](ReturnedInvoiceListItem.md)

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

# **post_inventory_returned_invoice**
> ReturnedInvoiceSaveResponse post_inventory_returned_invoice(get_by_id_request)

Post returned invoice

Changes the returned invoice status from NEW to PROCESSED

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.returned_invoice_save_response import ReturnedInvoiceSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingReturnedInvoiceApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document posting request body

    try:
        # Post returned invoice
        api_response = await api_instance.post_inventory_returned_invoice(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingReturnedInvoiceApi->post_inventory_returned_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingReturnedInvoiceApi->post_inventory_returned_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document posting request body | 

### Return type

[**ReturnedInvoiceSaveResponse**](ReturnedInvoiceSaveResponse.md)

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

# **unpost_inventory_returned_invoice**
> ReturnedInvoiceSaveResponse unpost_inventory_returned_invoice(get_by_id_request)

Unpost returned invoice

Changes the returned invoice status from PROCESSED to NEW

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.returned_invoice_save_response import ReturnedInvoiceSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingReturnedInvoiceApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document unposting request body

    try:
        # Unpost returned invoice
        api_response = await api_instance.unpost_inventory_returned_invoice(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingReturnedInvoiceApi->unpost_inventory_returned_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingReturnedInvoiceApi->unpost_inventory_returned_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document unposting request body | 

### Return type

[**ReturnedInvoiceSaveResponse**](ReturnedInvoiceSaveResponse.md)

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

# **update_inventory_returned_invoice**
> ReturnedInvoiceSaveResponse update_inventory_returned_invoice(returned_invoice_update_request)

Edit returned invoice

Updates a returned invoice from request parameters

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.returned_invoice_save_response import ReturnedInvoiceSaveResponse
from iikocloud_client.models.returned_invoice_update_request import ReturnedInvoiceUpdateRequest
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingReturnedInvoiceApi(api_client)
    returned_invoice_update_request = iikocloud_client.ReturnedInvoiceUpdateRequest() # ReturnedInvoiceUpdateRequest | Document update request body

    try:
        # Edit returned invoice
        api_response = await api_instance.update_inventory_returned_invoice(returned_invoice_update_request)
        print("The response of PublicApiInvoiceProcessingReturnedInvoiceApi->update_inventory_returned_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingReturnedInvoiceApi->update_inventory_returned_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returned_invoice_update_request** | [**ReturnedInvoiceUpdateRequest**](ReturnedInvoiceUpdateRequest.md)| Document update request body | 

### Return type

[**ReturnedInvoiceSaveResponse**](ReturnedInvoiceSaveResponse.md)

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

