# iikocloud_client.PublicApiInvoiceProcessingIncomingReturnedInvoiceApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_inventory_incoming_returned_invoice**](PublicApiInvoiceProcessingIncomingReturnedInvoiceApi.md#cancel_inventory_incoming_returned_invoice) | **POST** /api/inventory/v1/incoming_returned_invoice/cancel | Cancel incoming returned invoice draft
[**create_inventory_incoming_returned_invoice**](PublicApiInvoiceProcessingIncomingReturnedInvoiceApi.md#create_inventory_incoming_returned_invoice) | **POST** /api/inventory/v1/incoming_returned_invoice/create | Create incoming returned invoice
[**get_inventory_incoming_returned_invoice**](PublicApiInvoiceProcessingIncomingReturnedInvoiceApi.md#get_inventory_incoming_returned_invoice) | **POST** /api/inventory/v1/incoming_returned_invoice/get | Get incoming returned invoice by identifier
[**list_inventory_incoming_returned_invoices**](PublicApiInvoiceProcessingIncomingReturnedInvoiceApi.md#list_inventory_incoming_returned_invoices) | **POST** /api/inventory/v1/incoming_returned_invoice/list | Export incoming returned invoices
[**post_inventory_incoming_returned_invoice**](PublicApiInvoiceProcessingIncomingReturnedInvoiceApi.md#post_inventory_incoming_returned_invoice) | **POST** /api/inventory/v1/incoming_returned_invoice/post | Post incoming returned invoice
[**unpost_inventory_incoming_returned_invoice**](PublicApiInvoiceProcessingIncomingReturnedInvoiceApi.md#unpost_inventory_incoming_returned_invoice) | **POST** /api/inventory/v1/incoming_returned_invoice/unpost | Unpost incoming returned invoice
[**update_inventory_incoming_returned_invoice**](PublicApiInvoiceProcessingIncomingReturnedInvoiceApi.md#update_inventory_incoming_returned_invoice) | **POST** /api/inventory/v1/incoming_returned_invoice/update | Edit incoming returned invoice


# **cancel_inventory_incoming_returned_invoice**
> IncomingReturnedInvoiceSaveResponse cancel_inventory_incoming_returned_invoice(get_by_id_request)

Cancel incoming returned invoice draft

Changes the incoming returned invoice status from NEW to CANCELED

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.incoming_returned_invoice_save_response import IncomingReturnedInvoiceSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingReturnedInvoiceApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document draft cancellation request body

    try:
        # Cancel incoming returned invoice draft
        api_response = await api_instance.cancel_inventory_incoming_returned_invoice(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingIncomingReturnedInvoiceApi->cancel_inventory_incoming_returned_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingReturnedInvoiceApi->cancel_inventory_incoming_returned_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document draft cancellation request body | 

### Return type

[**IncomingReturnedInvoiceSaveResponse**](IncomingReturnedInvoiceSaveResponse.md)

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

# **create_inventory_incoming_returned_invoice**
> IncomingReturnedInvoiceSaveResponse create_inventory_incoming_returned_invoice(incoming_returned_invoice_create_request)

Create incoming returned invoice

Creates an incoming returned invoice from request parameters

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.incoming_returned_invoice_create_request import IncomingReturnedInvoiceCreateRequest
from iikocloud_client.models.incoming_returned_invoice_save_response import IncomingReturnedInvoiceSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingReturnedInvoiceApi(api_client)
    incoming_returned_invoice_create_request = iikocloud_client.IncomingReturnedInvoiceCreateRequest() # IncomingReturnedInvoiceCreateRequest | Document creation request body

    try:
        # Create incoming returned invoice
        api_response = await api_instance.create_inventory_incoming_returned_invoice(incoming_returned_invoice_create_request)
        print("The response of PublicApiInvoiceProcessingIncomingReturnedInvoiceApi->create_inventory_incoming_returned_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingReturnedInvoiceApi->create_inventory_incoming_returned_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incoming_returned_invoice_create_request** | [**IncomingReturnedInvoiceCreateRequest**](IncomingReturnedInvoiceCreateRequest.md)| Document creation request body | 

### Return type

[**IncomingReturnedInvoiceSaveResponse**](IncomingReturnedInvoiceSaveResponse.md)

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

# **get_inventory_incoming_returned_invoice**
> IncomingReturnedInvoiceGetResponse get_inventory_incoming_returned_invoice(get_by_id_request)

Get incoming returned invoice by identifier

Returns an incoming returned invoice by identifier

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.incoming_returned_invoice_get_response import IncomingReturnedInvoiceGetResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingReturnedInvoiceApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document retrieval by identifier request body

    try:
        # Get incoming returned invoice by identifier
        api_response = await api_instance.get_inventory_incoming_returned_invoice(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingIncomingReturnedInvoiceApi->get_inventory_incoming_returned_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingReturnedInvoiceApi->get_inventory_incoming_returned_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document retrieval by identifier request body | 

### Return type

[**IncomingReturnedInvoiceGetResponse**](IncomingReturnedInvoiceGetResponse.md)

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

# **list_inventory_incoming_returned_invoices**
> List[IncomingReturnedInvoiceListItem] list_inventory_incoming_returned_invoices(list_request)

Export incoming returned invoices

Exports incoming returned invoices from RMS for the specified period

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.incoming_returned_invoice_list_item import IncomingReturnedInvoiceListItem
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingReturnedInvoiceApi(api_client)
    list_request = iikocloud_client.ListRequest() # ListRequest | Document list retrieval request body

    try:
        # Export incoming returned invoices
        api_response = await api_instance.list_inventory_incoming_returned_invoices(list_request)
        print("The response of PublicApiInvoiceProcessingIncomingReturnedInvoiceApi->list_inventory_incoming_returned_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingReturnedInvoiceApi->list_inventory_incoming_returned_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_request** | [**ListRequest**](ListRequest.md)| Document list retrieval request body | 

### Return type

[**List[IncomingReturnedInvoiceListItem]**](IncomingReturnedInvoiceListItem.md)

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

# **post_inventory_incoming_returned_invoice**
> IncomingReturnedInvoiceSaveResponse post_inventory_incoming_returned_invoice(get_by_id_request)

Post incoming returned invoice

Changes the incoming returned invoice status from NEW to PROCESSED

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.incoming_returned_invoice_save_response import IncomingReturnedInvoiceSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingReturnedInvoiceApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document posting request body

    try:
        # Post incoming returned invoice
        api_response = await api_instance.post_inventory_incoming_returned_invoice(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingIncomingReturnedInvoiceApi->post_inventory_incoming_returned_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingReturnedInvoiceApi->post_inventory_incoming_returned_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document posting request body | 

### Return type

[**IncomingReturnedInvoiceSaveResponse**](IncomingReturnedInvoiceSaveResponse.md)

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

# **unpost_inventory_incoming_returned_invoice**
> IncomingReturnedInvoiceSaveResponse unpost_inventory_incoming_returned_invoice(get_by_id_request)

Unpost incoming returned invoice

Changes the incoming returned invoice status from PROCESSED to NEW

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.incoming_returned_invoice_save_response import IncomingReturnedInvoiceSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingReturnedInvoiceApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document unposting request body

    try:
        # Unpost incoming returned invoice
        api_response = await api_instance.unpost_inventory_incoming_returned_invoice(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingIncomingReturnedInvoiceApi->unpost_inventory_incoming_returned_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingReturnedInvoiceApi->unpost_inventory_incoming_returned_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document unposting request body | 

### Return type

[**IncomingReturnedInvoiceSaveResponse**](IncomingReturnedInvoiceSaveResponse.md)

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

# **update_inventory_incoming_returned_invoice**
> IncomingReturnedInvoiceSaveResponse update_inventory_incoming_returned_invoice(incoming_returned_invoice_update_request)

Edit incoming returned invoice

Updates an incoming returned invoice from request parameters

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.incoming_returned_invoice_save_response import IncomingReturnedInvoiceSaveResponse
from iikocloud_client.models.incoming_returned_invoice_update_request import IncomingReturnedInvoiceUpdateRequest
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingReturnedInvoiceApi(api_client)
    incoming_returned_invoice_update_request = iikocloud_client.IncomingReturnedInvoiceUpdateRequest() # IncomingReturnedInvoiceUpdateRequest | Document update request body

    try:
        # Edit incoming returned invoice
        api_response = await api_instance.update_inventory_incoming_returned_invoice(incoming_returned_invoice_update_request)
        print("The response of PublicApiInvoiceProcessingIncomingReturnedInvoiceApi->update_inventory_incoming_returned_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingReturnedInvoiceApi->update_inventory_incoming_returned_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incoming_returned_invoice_update_request** | [**IncomingReturnedInvoiceUpdateRequest**](IncomingReturnedInvoiceUpdateRequest.md)| Document update request body | 

### Return type

[**IncomingReturnedInvoiceSaveResponse**](IncomingReturnedInvoiceSaveResponse.md)

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

