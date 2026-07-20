# iikocloud_client.PublicApiInvoiceProcessingOutgoingServiceApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_finance_outgoing_service**](PublicApiInvoiceProcessingOutgoingServiceApi.md#cancel_finance_outgoing_service) | **POST** /api/finance/v1/outgoing_service/cancel | Cancel outgoing service act draft
[**create_finance_outgoing_service**](PublicApiInvoiceProcessingOutgoingServiceApi.md#create_finance_outgoing_service) | **POST** /api/finance/v1/outgoing_service/create | Create outgoing service act
[**get_finance_outgoing_service**](PublicApiInvoiceProcessingOutgoingServiceApi.md#get_finance_outgoing_service) | **POST** /api/finance/v1/outgoing_service/get | Get outgoing service act
[**list_finance_outgoing_services**](PublicApiInvoiceProcessingOutgoingServiceApi.md#list_finance_outgoing_services) | **POST** /api/finance/v1/outgoing_service/list | Export outgoing service acts
[**post_finance_outgoing_service**](PublicApiInvoiceProcessingOutgoingServiceApi.md#post_finance_outgoing_service) | **POST** /api/finance/v1/outgoing_service/post | Post outgoing service act
[**unpost_finance_outgoing_service**](PublicApiInvoiceProcessingOutgoingServiceApi.md#unpost_finance_outgoing_service) | **POST** /api/finance/v1/outgoing_service/unpost | Unpost outgoing service act
[**update_finance_outgoing_service**](PublicApiInvoiceProcessingOutgoingServiceApi.md#update_finance_outgoing_service) | **POST** /api/finance/v1/outgoing_service/update | Edit outgoing service act


# **cancel_finance_outgoing_service**
> OutgoingServiceSaveResponse cancel_finance_outgoing_service(get_by_id_request)

Cancel outgoing service act draft

Changes the outgoing service act status from NEW to CANCELED

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.outgoing_service_save_response import OutgoingServiceSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingOutgoingServiceApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Draft cancellation request body

    try:
        # Cancel outgoing service act draft
        api_response = await api_instance.cancel_finance_outgoing_service(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingOutgoingServiceApi->cancel_finance_outgoing_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingOutgoingServiceApi->cancel_finance_outgoing_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Draft cancellation request body | 

### Return type

[**OutgoingServiceSaveResponse**](OutgoingServiceSaveResponse.md)

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

# **create_finance_outgoing_service**
> OutgoingServiceSaveResponse create_finance_outgoing_service(outgoing_service_create_request)

Create outgoing service act

Creates a new outgoing service act in RMS

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.outgoing_service_create_request import OutgoingServiceCreateRequest
from iikocloud_client.models.outgoing_service_save_response import OutgoingServiceSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingOutgoingServiceApi(api_client)
    outgoing_service_create_request = iikocloud_client.OutgoingServiceCreateRequest() # OutgoingServiceCreateRequest | Document creation request body

    try:
        # Create outgoing service act
        api_response = await api_instance.create_finance_outgoing_service(outgoing_service_create_request)
        print("The response of PublicApiInvoiceProcessingOutgoingServiceApi->create_finance_outgoing_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingOutgoingServiceApi->create_finance_outgoing_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outgoing_service_create_request** | [**OutgoingServiceCreateRequest**](OutgoingServiceCreateRequest.md)| Document creation request body | 

### Return type

[**OutgoingServiceSaveResponse**](OutgoingServiceSaveResponse.md)

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

# **get_finance_outgoing_service**
> OutgoingServiceGetResponse get_finance_outgoing_service(get_by_id_request)

Get outgoing service act

Gets an outgoing service act by identifier from RMS

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.outgoing_service_get_response import OutgoingServiceGetResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingOutgoingServiceApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document retrieval by identifier request body

    try:
        # Get outgoing service act
        api_response = await api_instance.get_finance_outgoing_service(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingOutgoingServiceApi->get_finance_outgoing_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingOutgoingServiceApi->get_finance_outgoing_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document retrieval by identifier request body | 

### Return type

[**OutgoingServiceGetResponse**](OutgoingServiceGetResponse.md)

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

# **list_finance_outgoing_services**
> List[OutgoingServiceListItem] list_finance_outgoing_services(list_request)

Export outgoing service acts

Exports outgoing service acts from RMS for the specified period

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.list_request import ListRequest
from iikocloud_client.models.outgoing_service_list_item import OutgoingServiceListItem
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingOutgoingServiceApi(api_client)
    list_request = iikocloud_client.ListRequest() # ListRequest | Document list retrieval request body

    try:
        # Export outgoing service acts
        api_response = await api_instance.list_finance_outgoing_services(list_request)
        print("The response of PublicApiInvoiceProcessingOutgoingServiceApi->list_finance_outgoing_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingOutgoingServiceApi->list_finance_outgoing_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_request** | [**ListRequest**](ListRequest.md)| Document list retrieval request body | 

### Return type

[**List[OutgoingServiceListItem]**](OutgoingServiceListItem.md)

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

# **post_finance_outgoing_service**
> OutgoingServiceSaveResponse post_finance_outgoing_service(get_by_id_request)

Post outgoing service act

Changes the outgoing service act status from NEW to PROCESSED

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.outgoing_service_save_response import OutgoingServiceSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingOutgoingServiceApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document posting request body

    try:
        # Post outgoing service act
        api_response = await api_instance.post_finance_outgoing_service(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingOutgoingServiceApi->post_finance_outgoing_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingOutgoingServiceApi->post_finance_outgoing_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document posting request body | 

### Return type

[**OutgoingServiceSaveResponse**](OutgoingServiceSaveResponse.md)

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

# **unpost_finance_outgoing_service**
> OutgoingServiceSaveResponse unpost_finance_outgoing_service(get_by_id_request)

Unpost outgoing service act

Changes the outgoing service act status from PROCESSED to NEW

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.outgoing_service_save_response import OutgoingServiceSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingOutgoingServiceApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document unposting request body

    try:
        # Unpost outgoing service act
        api_response = await api_instance.unpost_finance_outgoing_service(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingOutgoingServiceApi->unpost_finance_outgoing_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingOutgoingServiceApi->unpost_finance_outgoing_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document unposting request body | 

### Return type

[**OutgoingServiceSaveResponse**](OutgoingServiceSaveResponse.md)

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

# **update_finance_outgoing_service**
> OutgoingServiceSaveResponse update_finance_outgoing_service(outgoing_service_update_request)

Edit outgoing service act

Edits an existing outgoing service act in RMS

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.outgoing_service_save_response import OutgoingServiceSaveResponse
from iikocloud_client.models.outgoing_service_update_request import OutgoingServiceUpdateRequest
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingOutgoingServiceApi(api_client)
    outgoing_service_update_request = iikocloud_client.OutgoingServiceUpdateRequest() # OutgoingServiceUpdateRequest | Document update request body

    try:
        # Edit outgoing service act
        api_response = await api_instance.update_finance_outgoing_service(outgoing_service_update_request)
        print("The response of PublicApiInvoiceProcessingOutgoingServiceApi->update_finance_outgoing_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingOutgoingServiceApi->update_finance_outgoing_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outgoing_service_update_request** | [**OutgoingServiceUpdateRequest**](OutgoingServiceUpdateRequest.md)| Document update request body | 

### Return type

[**OutgoingServiceSaveResponse**](OutgoingServiceSaveResponse.md)

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

