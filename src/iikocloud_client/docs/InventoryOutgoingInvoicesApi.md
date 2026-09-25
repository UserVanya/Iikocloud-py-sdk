# iikocloud_client.InventoryOutgoingInvoicesApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_inventory_outgoing_invoice_payment**](InventoryOutgoingInvoicesApi.md#add_inventory_outgoing_invoice_payment) | **POST** /api/inventory/v1/outgoing_invoice/modify/add_payment | Pay outgoing invoice
[**calculate_inventory_cost_prices**](InventoryOutgoingInvoicesApi.md#calculate_inventory_cost_prices) | **POST** /api/inventory/v1/costings/calculate | Get cost prices for nomenclature items
[**cancel_inventory_outgoing_invoice**](InventoryOutgoingInvoicesApi.md#cancel_inventory_outgoing_invoice) | **POST** /api/inventory/v1/outgoing_invoice/cancel | Cancel outgoing invoice draft
[**create_inventory_outgoing_invoice**](InventoryOutgoingInvoicesApi.md#create_inventory_outgoing_invoice) | **POST** /api/inventory/v1/outgoing_invoice/create | Create outgoing invoice
[**get_inventory_outgoing_invoice**](InventoryOutgoingInvoicesApi.md#get_inventory_outgoing_invoice) | **POST** /api/inventory/v1/outgoing_invoice/get | Get outgoing invoice by ID
[**list_inventory_outgoing_invoices**](InventoryOutgoingInvoicesApi.md#list_inventory_outgoing_invoices) | **POST** /api/inventory/v1/outgoing_invoice/list | Export outgoing invoices
[**post_inventory_outgoing_invoice**](InventoryOutgoingInvoicesApi.md#post_inventory_outgoing_invoice) | **POST** /api/inventory/v1/outgoing_invoice/post | Post outgoing invoice
[**set_inventory_outgoing_invoice_payment_date**](InventoryOutgoingInvoicesApi.md#set_inventory_outgoing_invoice_payment_date) | **POST** /api/inventory/v1/outgoing_invoice/patch/set_payment_date | Set payment date for outgoing invoice
[**unpost_inventory_outgoing_invoice**](InventoryOutgoingInvoicesApi.md#unpost_inventory_outgoing_invoice) | **POST** /api/inventory/v1/outgoing_invoice/unpost | Unpost outgoing invoice
[**update_inventory_outgoing_invoice**](InventoryOutgoingInvoicesApi.md#update_inventory_outgoing_invoice) | **POST** /api/inventory/v1/outgoing_invoice/update | Edit outgoing invoice


# **add_inventory_outgoing_invoice_payment**
> AccountingTransactionUserResponse add_inventory_outgoing_invoice_payment(pay_outgoing_invoice_request, timeout=timeout)

Pay outgoing invoice

Creates a payment for an outgoing invoice

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.accounting_transaction_user_response import AccountingTransactionUserResponse
from iikocloud_client.models.pay_outgoing_invoice_request import PayOutgoingInvoiceRequest
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
    api_instance = iikocloud_client.InventoryOutgoingInvoicesApi(api_client)
    pay_outgoing_invoice_request = iikocloud_client.PayOutgoingInvoiceRequest() # PayOutgoingInvoiceRequest | Outgoing invoice payment parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Pay outgoing invoice
        api_response = await api_instance.add_inventory_outgoing_invoice_payment(pay_outgoing_invoice_request, timeout=timeout)
        print("The response of InventoryOutgoingInvoicesApi->add_inventory_outgoing_invoice_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryOutgoingInvoicesApi->add_inventory_outgoing_invoice_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_outgoing_invoice_request** | [**PayOutgoingInvoiceRequest**](PayOutgoingInvoiceRequest.md)| Outgoing invoice payment parameters | 
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

# **calculate_inventory_cost_prices**
> GetCostPricesResponse calculate_inventory_cost_prices(get_cost_prices_request, timeout=timeout)

Get cost prices for nomenclature items

Gets cost prices for nomenclature items as of the specified date

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_cost_prices_request import GetCostPricesRequest
from iikocloud_client.models.get_cost_prices_response import GetCostPricesResponse
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
    api_instance = iikocloud_client.InventoryOutgoingInvoicesApi(api_client)
    get_cost_prices_request = iikocloud_client.GetCostPricesRequest() # GetCostPricesRequest | Cost prices request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get cost prices for nomenclature items
        api_response = await api_instance.calculate_inventory_cost_prices(get_cost_prices_request, timeout=timeout)
        print("The response of InventoryOutgoingInvoicesApi->calculate_inventory_cost_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryOutgoingInvoicesApi->calculate_inventory_cost_prices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_cost_prices_request** | [**GetCostPricesRequest**](GetCostPricesRequest.md)| Cost prices request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**GetCostPricesResponse**](GetCostPricesResponse.md)

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

# **cancel_inventory_outgoing_invoice**
> OutgoingInvoiceSaveResponse cancel_inventory_outgoing_invoice(get_by_id_request, timeout=timeout)

Cancel outgoing invoice draft

Changes the outgoing invoice status from NEW to CANCELED

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.outgoing_invoice_save_response import OutgoingInvoiceSaveResponse
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
    api_instance = iikocloud_client.InventoryOutgoingInvoicesApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document draft cancellation request body
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Cancel outgoing invoice draft
        api_response = await api_instance.cancel_inventory_outgoing_invoice(get_by_id_request, timeout=timeout)
        print("The response of InventoryOutgoingInvoicesApi->cancel_inventory_outgoing_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryOutgoingInvoicesApi->cancel_inventory_outgoing_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document draft cancellation request body | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**OutgoingInvoiceSaveResponse**](OutgoingInvoiceSaveResponse.md)

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

# **create_inventory_outgoing_invoice**
> OutgoingInvoiceSaveResponse create_inventory_outgoing_invoice(outgoing_invoice_request, timeout=timeout)

Create outgoing invoice

Creates an outgoing invoice from request parameters

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.outgoing_invoice_request import OutgoingInvoiceRequest
from iikocloud_client.models.outgoing_invoice_save_response import OutgoingInvoiceSaveResponse
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
    api_instance = iikocloud_client.InventoryOutgoingInvoicesApi(api_client)
    outgoing_invoice_request = iikocloud_client.OutgoingInvoiceRequest() # OutgoingInvoiceRequest | Document creation request body
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Create outgoing invoice
        api_response = await api_instance.create_inventory_outgoing_invoice(outgoing_invoice_request, timeout=timeout)
        print("The response of InventoryOutgoingInvoicesApi->create_inventory_outgoing_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryOutgoingInvoicesApi->create_inventory_outgoing_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outgoing_invoice_request** | [**OutgoingInvoiceRequest**](OutgoingInvoiceRequest.md)| Document creation request body | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**OutgoingInvoiceSaveResponse**](OutgoingInvoiceSaveResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_outgoing_invoice**
> OutgoingInvoice get_inventory_outgoing_invoice(get_by_id_request, timeout=timeout)

Get outgoing invoice by ID

Returns an outgoing invoice by identifier

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.outgoing_invoice import OutgoingInvoice
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
    api_instance = iikocloud_client.InventoryOutgoingInvoicesApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document retrieval by identifier request body
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get outgoing invoice by ID
        api_response = await api_instance.get_inventory_outgoing_invoice(get_by_id_request, timeout=timeout)
        print("The response of InventoryOutgoingInvoicesApi->get_inventory_outgoing_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryOutgoingInvoicesApi->get_inventory_outgoing_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document retrieval by identifier request body | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**OutgoingInvoice**](OutgoingInvoice.md)

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

# **list_inventory_outgoing_invoices**
> List[OutgoingInvoice] list_inventory_outgoing_invoices(list_request, timeout=timeout)

Export outgoing invoices

Exports outgoing invoices for the specified period

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.list_request import ListRequest
from iikocloud_client.models.outgoing_invoice import OutgoingInvoice
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
    api_instance = iikocloud_client.InventoryOutgoingInvoicesApi(api_client)
    list_request = iikocloud_client.ListRequest() # ListRequest | Document list retrieval request body
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Export outgoing invoices
        api_response = await api_instance.list_inventory_outgoing_invoices(list_request, timeout=timeout)
        print("The response of InventoryOutgoingInvoicesApi->list_inventory_outgoing_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryOutgoingInvoicesApi->list_inventory_outgoing_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_request** | [**ListRequest**](ListRequest.md)| Document list retrieval request body | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**List[OutgoingInvoice]**](OutgoingInvoice.md)

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

# **post_inventory_outgoing_invoice**
> OutgoingInvoiceSaveResponse post_inventory_outgoing_invoice(get_by_id_request, timeout=timeout)

Post outgoing invoice

Changes the outgoing invoice status from NEW to PROCESSED

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.outgoing_invoice_save_response import OutgoingInvoiceSaveResponse
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
    api_instance = iikocloud_client.InventoryOutgoingInvoicesApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document posting request body
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Post outgoing invoice
        api_response = await api_instance.post_inventory_outgoing_invoice(get_by_id_request, timeout=timeout)
        print("The response of InventoryOutgoingInvoicesApi->post_inventory_outgoing_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryOutgoingInvoicesApi->post_inventory_outgoing_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document posting request body | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**OutgoingInvoiceSaveResponse**](OutgoingInvoiceSaveResponse.md)

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

# **set_inventory_outgoing_invoice_payment_date**
> SetPaymentDateOutgoingResponse set_inventory_outgoing_invoice_payment_date(set_payment_date_outgoing_request, timeout=timeout)

Set payment date for outgoing invoice

Sets the payment date for an outgoing invoice. The operation is available only for an already paid invoice.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.set_payment_date_outgoing_request import SetPaymentDateOutgoingRequest
from iikocloud_client.models.set_payment_date_outgoing_response import SetPaymentDateOutgoingResponse
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
    api_instance = iikocloud_client.InventoryOutgoingInvoicesApi(api_client)
    set_payment_date_outgoing_request = iikocloud_client.SetPaymentDateOutgoingRequest() # SetPaymentDateOutgoingRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Set payment date for outgoing invoice
        api_response = await api_instance.set_inventory_outgoing_invoice_payment_date(set_payment_date_outgoing_request, timeout=timeout)
        print("The response of InventoryOutgoingInvoicesApi->set_inventory_outgoing_invoice_payment_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryOutgoingInvoicesApi->set_inventory_outgoing_invoice_payment_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_payment_date_outgoing_request** | [**SetPaymentDateOutgoingRequest**](SetPaymentDateOutgoingRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**SetPaymentDateOutgoingResponse**](SetPaymentDateOutgoingResponse.md)

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

# **unpost_inventory_outgoing_invoice**
> OutgoingInvoiceSaveResponse unpost_inventory_outgoing_invoice(get_by_id_request, timeout=timeout)

Unpost outgoing invoice

Changes the outgoing invoice status from PROCESSED to NEW

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.outgoing_invoice_save_response import OutgoingInvoiceSaveResponse
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
    api_instance = iikocloud_client.InventoryOutgoingInvoicesApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document unposting request body
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Unpost outgoing invoice
        api_response = await api_instance.unpost_inventory_outgoing_invoice(get_by_id_request, timeout=timeout)
        print("The response of InventoryOutgoingInvoicesApi->unpost_inventory_outgoing_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryOutgoingInvoicesApi->unpost_inventory_outgoing_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document unposting request body | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**OutgoingInvoiceSaveResponse**](OutgoingInvoiceSaveResponse.md)

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

# **update_inventory_outgoing_invoice**
> OutgoingInvoiceSaveResponse update_inventory_outgoing_invoice(outgoing_invoice_request, timeout=timeout)

Edit outgoing invoice

Updates an outgoing invoice from request parameters

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.outgoing_invoice_request import OutgoingInvoiceRequest
from iikocloud_client.models.outgoing_invoice_save_response import OutgoingInvoiceSaveResponse
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
    api_instance = iikocloud_client.InventoryOutgoingInvoicesApi(api_client)
    outgoing_invoice_request = iikocloud_client.OutgoingInvoiceRequest() # OutgoingInvoiceRequest | Document update request body
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Edit outgoing invoice
        api_response = await api_instance.update_inventory_outgoing_invoice(outgoing_invoice_request, timeout=timeout)
        print("The response of InventoryOutgoingInvoicesApi->update_inventory_outgoing_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryOutgoingInvoicesApi->update_inventory_outgoing_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outgoing_invoice_request** | [**OutgoingInvoiceRequest**](OutgoingInvoiceRequest.md)| Document update request body | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**OutgoingInvoiceSaveResponse**](OutgoingInvoiceSaveResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

