# iikocloud_client.InventoryIncomingInvoicesApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_inventory_incoming_invoice_payment**](InventoryIncomingInvoicesApi.md#add_inventory_incoming_invoice_payment) | **POST** /api/inventory/v1/incoming_invoice/modify/add_payment | Pay incoming invoice
[**cancel_inventory_incoming_invoice**](InventoryIncomingInvoicesApi.md#cancel_inventory_incoming_invoice) | **POST** /api/inventory/v1/incoming_invoice/cancel | Cancel incoming invoice draft
[**create_inventory_incoming_invoice**](InventoryIncomingInvoicesApi.md#create_inventory_incoming_invoice) | **POST** /api/inventory/v1/incoming_invoice/create | Create incoming invoice
[**get_inventory_incoming_invoice**](InventoryIncomingInvoicesApi.md#get_inventory_incoming_invoice) | **POST** /api/inventory/v1/incoming_invoice/get | Get incoming invoice by identifier
[**list_inventory_incoming_invoices**](InventoryIncomingInvoicesApi.md#list_inventory_incoming_invoices) | **POST** /api/inventory/v1/incoming_invoice/list | Export incoming invoices
[**post_inventory_incoming_invoice**](InventoryIncomingInvoicesApi.md#post_inventory_incoming_invoice) | **POST** /api/inventory/v1/incoming_invoice/post | Post incoming invoice
[**set_inventory_incoming_invoice_payment_date**](InventoryIncomingInvoicesApi.md#set_inventory_incoming_invoice_payment_date) | **POST** /api/inventory/v1/incoming_invoice/patch/set_payment_date | Set payment date for incoming invoice
[**unpost_inventory_incoming_invoice**](InventoryIncomingInvoicesApi.md#unpost_inventory_incoming_invoice) | **POST** /api/inventory/v1/incoming_invoice/unpost | Unpost incoming invoice
[**update_inventory_incoming_invoice**](InventoryIncomingInvoicesApi.md#update_inventory_incoming_invoice) | **POST** /api/inventory/v1/incoming_invoice/update | Edit incoming invoice


# **add_inventory_incoming_invoice_payment**
> AccountingTransactionUserResponse add_inventory_incoming_invoice_payment(pay_request, timeout=timeout)

Pay incoming invoice

Creates a payment for an incoming invoice

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.accounting_transaction_user_response import AccountingTransactionUserResponse
from iikocloud_client.models.pay_request import PayRequest
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
    api_instance = iikocloud_client.InventoryIncomingInvoicesApi(api_client)
    pay_request = iikocloud_client.PayRequest() # PayRequest | Incoming invoice payment parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Pay incoming invoice
        api_response = await api_instance.add_inventory_incoming_invoice_payment(pay_request, timeout=timeout)
        print("The response of InventoryIncomingInvoicesApi->add_inventory_incoming_invoice_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingInvoicesApi->add_inventory_incoming_invoice_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_request** | [**PayRequest**](PayRequest.md)| Incoming invoice payment parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AccountingTransactionUserResponse**](AccountingTransactionUserResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created |  -  |
**400** | Invalid request (validation/already paid/empty body/invalid JSON) |  -  |
**401** | Unauthorized |  -  |
**405** | Method not allowed (POST expected) |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_inventory_incoming_invoice**
> IncomingInvoiceSaveResponse cancel_inventory_incoming_invoice(get_by_id_request, timeout=timeout)

Cancel incoming invoice draft

Changes the incoming invoice status from NEW to CANCELED

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.incoming_invoice_save_response import IncomingInvoiceSaveResponse
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
    api_instance = iikocloud_client.InventoryIncomingInvoicesApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document draft cancellation request body
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Cancel incoming invoice draft
        api_response = await api_instance.cancel_inventory_incoming_invoice(get_by_id_request, timeout=timeout)
        print("The response of InventoryIncomingInvoicesApi->cancel_inventory_incoming_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingInvoicesApi->cancel_inventory_incoming_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document draft cancellation request body | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**IncomingInvoiceSaveResponse**](IncomingInvoiceSaveResponse.md)

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

# **create_inventory_incoming_invoice**
> IncomingInvoiceSaveResponse create_inventory_incoming_invoice(incoming_invoice_request, timeout=timeout)

Create incoming invoice

Creates an incoming invoice from request parameters

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.incoming_invoice_request import IncomingInvoiceRequest
from iikocloud_client.models.incoming_invoice_save_response import IncomingInvoiceSaveResponse
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
    api_instance = iikocloud_client.InventoryIncomingInvoicesApi(api_client)
    incoming_invoice_request = iikocloud_client.IncomingInvoiceRequest() # IncomingInvoiceRequest | Document creation request body
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Create incoming invoice
        api_response = await api_instance.create_inventory_incoming_invoice(incoming_invoice_request, timeout=timeout)
        print("The response of InventoryIncomingInvoicesApi->create_inventory_incoming_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingInvoicesApi->create_inventory_incoming_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incoming_invoice_request** | [**IncomingInvoiceRequest**](IncomingInvoiceRequest.md)| Document creation request body | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**IncomingInvoiceSaveResponse**](IncomingInvoiceSaveResponse.md)

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
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_incoming_invoice**
> IncomingInvoice get_inventory_incoming_invoice(get_by_id_request, timeout=timeout)

Get incoming invoice by identifier

Gets an incoming invoice by identifier

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.incoming_invoice import IncomingInvoice
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
    api_instance = iikocloud_client.InventoryIncomingInvoicesApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document retrieval by identifier request body
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get incoming invoice by identifier
        api_response = await api_instance.get_inventory_incoming_invoice(get_by_id_request, timeout=timeout)
        print("The response of InventoryIncomingInvoicesApi->get_inventory_incoming_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingInvoicesApi->get_inventory_incoming_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document retrieval by identifier request body | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**IncomingInvoice**](IncomingInvoice.md)

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
**404** | Document not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inventory_incoming_invoices**
> List[IncomingInvoice] list_inventory_incoming_invoices(list_request, timeout=timeout)

Export incoming invoices

Exports incoming invoices for the specified period

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.incoming_invoice import IncomingInvoice
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
    api_instance = iikocloud_client.InventoryIncomingInvoicesApi(api_client)
    list_request = iikocloud_client.ListRequest() # ListRequest | Document list retrieval request body
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Export incoming invoices
        api_response = await api_instance.list_inventory_incoming_invoices(list_request, timeout=timeout)
        print("The response of InventoryIncomingInvoicesApi->list_inventory_incoming_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingInvoicesApi->list_inventory_incoming_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_request** | [**ListRequest**](ListRequest.md)| Document list retrieval request body | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**List[IncomingInvoice]**](IncomingInvoice.md)

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
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_inventory_incoming_invoice**
> IncomingInvoiceSaveResponse post_inventory_incoming_invoice(get_by_id_request, timeout=timeout)

Post incoming invoice

Changes the incoming invoice status from NEW to PROCESSED

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.incoming_invoice_save_response import IncomingInvoiceSaveResponse
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
    api_instance = iikocloud_client.InventoryIncomingInvoicesApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document posting request body
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Post incoming invoice
        api_response = await api_instance.post_inventory_incoming_invoice(get_by_id_request, timeout=timeout)
        print("The response of InventoryIncomingInvoicesApi->post_inventory_incoming_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingInvoicesApi->post_inventory_incoming_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document posting request body | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**IncomingInvoiceSaveResponse**](IncomingInvoiceSaveResponse.md)

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

# **set_inventory_incoming_invoice_payment_date**
> SetPaymentDateResponse set_inventory_incoming_invoice_payment_date(set_payment_date_request, timeout=timeout)

Set payment date for incoming invoice

Sets the payment date for an incoming invoice. The operation is available only for an already paid invoice (unpaid sum = 0).

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.set_payment_date_request import SetPaymentDateRequest
from iikocloud_client.models.set_payment_date_response import SetPaymentDateResponse
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
    api_instance = iikocloud_client.InventoryIncomingInvoicesApi(api_client)
    set_payment_date_request = iikocloud_client.SetPaymentDateRequest() # SetPaymentDateRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Set payment date for incoming invoice
        api_response = await api_instance.set_inventory_incoming_invoice_payment_date(set_payment_date_request, timeout=timeout)
        print("The response of InventoryIncomingInvoicesApi->set_inventory_incoming_invoice_payment_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingInvoicesApi->set_inventory_incoming_invoice_payment_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_payment_date_request** | [**SetPaymentDateRequest**](SetPaymentDateRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**SetPaymentDateResponse**](SetPaymentDateResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request (validation/invalid JSON/invoice not paid) |  -  |
**401** | Unauthorized |  -  |
**405** | Method not allowed (POST expected) |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpost_inventory_incoming_invoice**
> IncomingInvoiceSaveResponse unpost_inventory_incoming_invoice(get_by_id_request, timeout=timeout)

Unpost incoming invoice

Changes the incoming invoice status from PROCESSED to NEW

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.incoming_invoice_save_response import IncomingInvoiceSaveResponse
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
    api_instance = iikocloud_client.InventoryIncomingInvoicesApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document unposting request body
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Unpost incoming invoice
        api_response = await api_instance.unpost_inventory_incoming_invoice(get_by_id_request, timeout=timeout)
        print("The response of InventoryIncomingInvoicesApi->unpost_inventory_incoming_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingInvoicesApi->unpost_inventory_incoming_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document unposting request body | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**IncomingInvoiceSaveResponse**](IncomingInvoiceSaveResponse.md)

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

# **update_inventory_incoming_invoice**
> IncomingInvoiceSaveResponse update_inventory_incoming_invoice(incoming_invoice_request, timeout=timeout)

Edit incoming invoice

Updates an incoming invoice from request parameters

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.incoming_invoice_request import IncomingInvoiceRequest
from iikocloud_client.models.incoming_invoice_save_response import IncomingInvoiceSaveResponse
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
    api_instance = iikocloud_client.InventoryIncomingInvoicesApi(api_client)
    incoming_invoice_request = iikocloud_client.IncomingInvoiceRequest() # IncomingInvoiceRequest | Document update request body
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Edit incoming invoice
        api_response = await api_instance.update_inventory_incoming_invoice(incoming_invoice_request, timeout=timeout)
        print("The response of InventoryIncomingInvoicesApi->update_inventory_incoming_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingInvoicesApi->update_inventory_incoming_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incoming_invoice_request** | [**IncomingInvoiceRequest**](IncomingInvoiceRequest.md)| Document update request body | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**IncomingInvoiceSaveResponse**](IncomingInvoiceSaveResponse.md)

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
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

