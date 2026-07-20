# iikocloud_client.PublicApiInvoiceProcessingIncomingInvoicesApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_inventory_incoming_invoice_payment**](PublicApiInvoiceProcessingIncomingInvoicesApi.md#add_inventory_incoming_invoice_payment) | **POST** /api/inventory/v1/incoming_invoice/modify/add_payment | Pay incoming invoice
[**cancel_inventory_incoming_invoice**](PublicApiInvoiceProcessingIncomingInvoicesApi.md#cancel_inventory_incoming_invoice) | **POST** /api/inventory/v1/incoming_invoice/cancel | Cancel incoming invoice draft
[**create_inventory_incoming_invoice**](PublicApiInvoiceProcessingIncomingInvoicesApi.md#create_inventory_incoming_invoice) | **POST** /api/inventory/v1/incoming_invoice/create | Create incoming invoice
[**get_inventory_incoming_invoice**](PublicApiInvoiceProcessingIncomingInvoicesApi.md#get_inventory_incoming_invoice) | **POST** /api/inventory/v1/incoming_invoice/get | Get incoming invoice by identifier
[**list_inventory_incoming_invoices**](PublicApiInvoiceProcessingIncomingInvoicesApi.md#list_inventory_incoming_invoices) | **POST** /api/inventory/v1/incoming_invoice/list | Export incoming invoices
[**post_inventory_incoming_invoice**](PublicApiInvoiceProcessingIncomingInvoicesApi.md#post_inventory_incoming_invoice) | **POST** /api/inventory/v1/incoming_invoice/post | Post incoming invoice
[**set_inventory_incoming_invoice_payment_date**](PublicApiInvoiceProcessingIncomingInvoicesApi.md#set_inventory_incoming_invoice_payment_date) | **POST** /api/inventory/v1/incoming_invoice/patch/set_payment_date | Set payment date for incoming invoice
[**unpost_inventory_incoming_invoice**](PublicApiInvoiceProcessingIncomingInvoicesApi.md#unpost_inventory_incoming_invoice) | **POST** /api/inventory/v1/incoming_invoice/unpost | Unpost incoming invoice
[**update_inventory_incoming_invoice**](PublicApiInvoiceProcessingIncomingInvoicesApi.md#update_inventory_incoming_invoice) | **POST** /api/inventory/v1/incoming_invoice/update | Edit incoming invoice


# **add_inventory_incoming_invoice_payment**
> AccountingTransactionUserResponse add_inventory_incoming_invoice_payment(pay_request)

Pay incoming invoice

Creates a payment for an incoming invoice in RMS

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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingInvoicesApi(api_client)
    pay_request = iikocloud_client.PayRequest() # PayRequest | Incoming invoice payment parameters

    try:
        # Pay incoming invoice
        api_response = await api_instance.add_inventory_incoming_invoice_payment(pay_request)
        print("The response of PublicApiInvoiceProcessingIncomingInvoicesApi->add_inventory_incoming_invoice_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingInvoicesApi->add_inventory_incoming_invoice_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_request** | [**PayRequest**](PayRequest.md)| Incoming invoice payment parameters | 

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
> IncomingInvoiceSaveResponse cancel_inventory_incoming_invoice(get_by_id_request)

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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingInvoicesApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document draft cancellation request body

    try:
        # Cancel incoming invoice draft
        api_response = await api_instance.cancel_inventory_incoming_invoice(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingIncomingInvoicesApi->cancel_inventory_incoming_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingInvoicesApi->cancel_inventory_incoming_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document draft cancellation request body | 

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
> IncomingInvoiceSaveResponse create_inventory_incoming_invoice(incoming_invoice_request)

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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingInvoicesApi(api_client)
    incoming_invoice_request = iikocloud_client.IncomingInvoiceRequest() # IncomingInvoiceRequest | Document creation request body

    try:
        # Create incoming invoice
        api_response = await api_instance.create_inventory_incoming_invoice(incoming_invoice_request)
        print("The response of PublicApiInvoiceProcessingIncomingInvoicesApi->create_inventory_incoming_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingInvoicesApi->create_inventory_incoming_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incoming_invoice_request** | [**IncomingInvoiceRequest**](IncomingInvoiceRequest.md)| Document creation request body | 

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
> IncomingInvoice get_inventory_incoming_invoice(get_by_id_request)

Get incoming invoice by identifier

Gets an incoming invoice by identifier from RMS

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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingInvoicesApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document retrieval by identifier request body

    try:
        # Get incoming invoice by identifier
        api_response = await api_instance.get_inventory_incoming_invoice(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingIncomingInvoicesApi->get_inventory_incoming_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingInvoicesApi->get_inventory_incoming_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document retrieval by identifier request body | 

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
> List[IncomingInvoice] list_inventory_incoming_invoices(list_request)

Export incoming invoices

Exports incoming invoices from RMS for the specified period

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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingInvoicesApi(api_client)
    list_request = iikocloud_client.ListRequest() # ListRequest | Document list retrieval request body

    try:
        # Export incoming invoices
        api_response = await api_instance.list_inventory_incoming_invoices(list_request)
        print("The response of PublicApiInvoiceProcessingIncomingInvoicesApi->list_inventory_incoming_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingInvoicesApi->list_inventory_incoming_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_request** | [**ListRequest**](ListRequest.md)| Document list retrieval request body | 

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
> IncomingInvoiceSaveResponse post_inventory_incoming_invoice(get_by_id_request)

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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingInvoicesApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document posting request body

    try:
        # Post incoming invoice
        api_response = await api_instance.post_inventory_incoming_invoice(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingIncomingInvoicesApi->post_inventory_incoming_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingInvoicesApi->post_inventory_incoming_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document posting request body | 

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
> SetPaymentDateResponse set_inventory_incoming_invoice_payment_date(set_payment_date_request)

Set payment date for incoming invoice

Sets the payment date for an incoming invoice in RMS. The operation is available only for an already paid invoice (unpaid sum = 0).

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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingInvoicesApi(api_client)
    set_payment_date_request = iikocloud_client.SetPaymentDateRequest() # SetPaymentDateRequest | Request parameters

    try:
        # Set payment date for incoming invoice
        api_response = await api_instance.set_inventory_incoming_invoice_payment_date(set_payment_date_request)
        print("The response of PublicApiInvoiceProcessingIncomingInvoicesApi->set_inventory_incoming_invoice_payment_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingInvoicesApi->set_inventory_incoming_invoice_payment_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_payment_date_request** | [**SetPaymentDateRequest**](SetPaymentDateRequest.md)| Request parameters | 

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
> IncomingInvoiceSaveResponse unpost_inventory_incoming_invoice(get_by_id_request)

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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingInvoicesApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document unposting request body

    try:
        # Unpost incoming invoice
        api_response = await api_instance.unpost_inventory_incoming_invoice(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingIncomingInvoicesApi->unpost_inventory_incoming_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingInvoicesApi->unpost_inventory_incoming_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document unposting request body | 

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
> IncomingInvoiceSaveResponse update_inventory_incoming_invoice(incoming_invoice_request)

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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingInvoicesApi(api_client)
    incoming_invoice_request = iikocloud_client.IncomingInvoiceRequest() # IncomingInvoiceRequest | Document update request body

    try:
        # Edit incoming invoice
        api_response = await api_instance.update_inventory_incoming_invoice(incoming_invoice_request)
        print("The response of PublicApiInvoiceProcessingIncomingInvoicesApi->update_inventory_incoming_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingInvoicesApi->update_inventory_incoming_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incoming_invoice_request** | [**IncomingInvoiceRequest**](IncomingInvoiceRequest.md)| Document update request body | 

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

