# iikocloud_client.InventoryIncomingReturnedInvoiceApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_inventory_incoming_returned_invoice**](InventoryIncomingReturnedInvoiceApi.md#cancel_inventory_incoming_returned_invoice) | **POST** /api/inventory/v1/incoming_returned_invoice/cancel | Cancel incoming returned invoice draft
[**create_inventory_incoming_returned_invoice**](InventoryIncomingReturnedInvoiceApi.md#create_inventory_incoming_returned_invoice) | **POST** /api/inventory/v1/incoming_returned_invoice/create | Create incoming returned invoice
[**get_inventory_incoming_returned_invoice**](InventoryIncomingReturnedInvoiceApi.md#get_inventory_incoming_returned_invoice) | **POST** /api/inventory/v1/incoming_returned_invoice/get | Get incoming returned invoice by identifier
[**list_inventory_incoming_returned_invoices**](InventoryIncomingReturnedInvoiceApi.md#list_inventory_incoming_returned_invoices) | **POST** /api/inventory/v1/incoming_returned_invoice/list | Export incoming returned invoices
[**post_inventory_incoming_returned_invoice**](InventoryIncomingReturnedInvoiceApi.md#post_inventory_incoming_returned_invoice) | **POST** /api/inventory/v1/incoming_returned_invoice/post | Post incoming returned invoice
[**unpost_inventory_incoming_returned_invoice**](InventoryIncomingReturnedInvoiceApi.md#unpost_inventory_incoming_returned_invoice) | **POST** /api/inventory/v1/incoming_returned_invoice/unpost | Unpost incoming returned invoice
[**update_inventory_incoming_returned_invoice**](InventoryIncomingReturnedInvoiceApi.md#update_inventory_incoming_returned_invoice) | **POST** /api/inventory/v1/incoming_returned_invoice/update | Edit incoming returned invoice


# **cancel_inventory_incoming_returned_invoice**
> IncomingReturnedInvoiceSaveResponse cancel_inventory_incoming_returned_invoice(get_by_id_request, timeout=timeout)

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
    api_instance = iikocloud_client.InventoryIncomingReturnedInvoiceApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document draft cancellation request body
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Cancel incoming returned invoice draft
        api_response = await api_instance.cancel_inventory_incoming_returned_invoice(get_by_id_request, timeout=timeout)
        print("The response of InventoryIncomingReturnedInvoiceApi->cancel_inventory_incoming_returned_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingReturnedInvoiceApi->cancel_inventory_incoming_returned_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document draft cancellation request body | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

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
> IncomingReturnedInvoiceSaveResponse create_inventory_incoming_returned_invoice(incoming_returned_invoice_create_request, timeout=timeout)

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
    api_instance = iikocloud_client.InventoryIncomingReturnedInvoiceApi(api_client)
    incoming_returned_invoice_create_request = iikocloud_client.IncomingReturnedInvoiceCreateRequest() # IncomingReturnedInvoiceCreateRequest | Document creation request body
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Create incoming returned invoice
        api_response = await api_instance.create_inventory_incoming_returned_invoice(incoming_returned_invoice_create_request, timeout=timeout)
        print("The response of InventoryIncomingReturnedInvoiceApi->create_inventory_incoming_returned_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingReturnedInvoiceApi->create_inventory_incoming_returned_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incoming_returned_invoice_create_request** | [**IncomingReturnedInvoiceCreateRequest**](IncomingReturnedInvoiceCreateRequest.md)| Document creation request body | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

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
> IncomingReturnedInvoiceGetResponse get_inventory_incoming_returned_invoice(get_by_id_request, timeout=timeout)

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
    api_instance = iikocloud_client.InventoryIncomingReturnedInvoiceApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document retrieval by identifier request body
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get incoming returned invoice by identifier
        api_response = await api_instance.get_inventory_incoming_returned_invoice(get_by_id_request, timeout=timeout)
        print("The response of InventoryIncomingReturnedInvoiceApi->get_inventory_incoming_returned_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingReturnedInvoiceApi->get_inventory_incoming_returned_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document retrieval by identifier request body | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

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
> List[IncomingReturnedInvoiceListItem] list_inventory_incoming_returned_invoices(list_request, timeout=timeout)

Export incoming returned invoices

Exports incoming returned invoices for the specified period

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
    api_instance = iikocloud_client.InventoryIncomingReturnedInvoiceApi(api_client)
    list_request = iikocloud_client.ListRequest() # ListRequest | Document list retrieval request body
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Export incoming returned invoices
        api_response = await api_instance.list_inventory_incoming_returned_invoices(list_request, timeout=timeout)
        print("The response of InventoryIncomingReturnedInvoiceApi->list_inventory_incoming_returned_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingReturnedInvoiceApi->list_inventory_incoming_returned_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_request** | [**ListRequest**](ListRequest.md)| Document list retrieval request body | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

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
> IncomingReturnedInvoiceSaveResponse post_inventory_incoming_returned_invoice(get_by_id_request, timeout=timeout)

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
    api_instance = iikocloud_client.InventoryIncomingReturnedInvoiceApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document posting request body
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Post incoming returned invoice
        api_response = await api_instance.post_inventory_incoming_returned_invoice(get_by_id_request, timeout=timeout)
        print("The response of InventoryIncomingReturnedInvoiceApi->post_inventory_incoming_returned_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingReturnedInvoiceApi->post_inventory_incoming_returned_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document posting request body | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

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
> IncomingReturnedInvoiceSaveResponse unpost_inventory_incoming_returned_invoice(get_by_id_request, timeout=timeout)

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
    api_instance = iikocloud_client.InventoryIncomingReturnedInvoiceApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document unposting request body
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Unpost incoming returned invoice
        api_response = await api_instance.unpost_inventory_incoming_returned_invoice(get_by_id_request, timeout=timeout)
        print("The response of InventoryIncomingReturnedInvoiceApi->unpost_inventory_incoming_returned_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingReturnedInvoiceApi->unpost_inventory_incoming_returned_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document unposting request body | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

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
> IncomingReturnedInvoiceSaveResponse update_inventory_incoming_returned_invoice(incoming_returned_invoice_update_request, timeout=timeout)

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
    api_instance = iikocloud_client.InventoryIncomingReturnedInvoiceApi(api_client)
    incoming_returned_invoice_update_request = iikocloud_client.IncomingReturnedInvoiceUpdateRequest() # IncomingReturnedInvoiceUpdateRequest | Document update request body
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Edit incoming returned invoice
        api_response = await api_instance.update_inventory_incoming_returned_invoice(incoming_returned_invoice_update_request, timeout=timeout)
        print("The response of InventoryIncomingReturnedInvoiceApi->update_inventory_incoming_returned_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingReturnedInvoiceApi->update_inventory_incoming_returned_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incoming_returned_invoice_update_request** | [**IncomingReturnedInvoiceUpdateRequest**](IncomingReturnedInvoiceUpdateRequest.md)| Document update request body | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

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

