# iikocloud_client.PublicApiInvoiceProcessingIncomingServiceApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_finance_incoming_service**](PublicApiInvoiceProcessingIncomingServiceApi.md#cancel_finance_incoming_service) | **POST** /api/finance/v1/incoming_service/cancel | Cancel incoming service act draft
[**create_finance_incoming_service**](PublicApiInvoiceProcessingIncomingServiceApi.md#create_finance_incoming_service) | **POST** /api/finance/v1/incoming_service/create | Create incoming service act
[**get_finance_incoming_service**](PublicApiInvoiceProcessingIncomingServiceApi.md#get_finance_incoming_service) | **POST** /api/finance/v1/incoming_service/get | Get incoming service act
[**list_finance_incoming_services**](PublicApiInvoiceProcessingIncomingServiceApi.md#list_finance_incoming_services) | **POST** /api/finance/v1/incoming_service/list | Export incoming service acts
[**post_finance_incoming_service**](PublicApiInvoiceProcessingIncomingServiceApi.md#post_finance_incoming_service) | **POST** /api/finance/v1/incoming_service/post | Post incoming service act
[**unpost_finance_incoming_service**](PublicApiInvoiceProcessingIncomingServiceApi.md#unpost_finance_incoming_service) | **POST** /api/finance/v1/incoming_service/unpost | Unpost incoming service act
[**update_finance_incoming_service**](PublicApiInvoiceProcessingIncomingServiceApi.md#update_finance_incoming_service) | **POST** /api/finance/v1/incoming_service/update | Edit incoming service act


# **cancel_finance_incoming_service**
> IncomingServiceSaveResponse cancel_finance_incoming_service(get_by_id_request)

Cancel incoming service act draft

Changes the incoming service act status from NEW to CANCELED

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.incoming_service_save_response import IncomingServiceSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingServiceApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Draft cancellation request body

    try:
        # Cancel incoming service act draft
        api_response = await api_instance.cancel_finance_incoming_service(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingIncomingServiceApi->cancel_finance_incoming_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingServiceApi->cancel_finance_incoming_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Draft cancellation request body | 

### Return type

[**IncomingServiceSaveResponse**](IncomingServiceSaveResponse.md)

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

# **create_finance_incoming_service**
> IncomingServiceSaveResponse create_finance_incoming_service(incoming_service_create_request)

Create incoming service act

Creates a new incoming service act in RMS

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.incoming_service_create_request import IncomingServiceCreateRequest
from iikocloud_client.models.incoming_service_save_response import IncomingServiceSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingServiceApi(api_client)
    incoming_service_create_request = iikocloud_client.IncomingServiceCreateRequest() # IncomingServiceCreateRequest | Document creation request body

    try:
        # Create incoming service act
        api_response = await api_instance.create_finance_incoming_service(incoming_service_create_request)
        print("The response of PublicApiInvoiceProcessingIncomingServiceApi->create_finance_incoming_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingServiceApi->create_finance_incoming_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incoming_service_create_request** | [**IncomingServiceCreateRequest**](IncomingServiceCreateRequest.md)| Document creation request body | 

### Return type

[**IncomingServiceSaveResponse**](IncomingServiceSaveResponse.md)

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

# **get_finance_incoming_service**
> IncomingServiceGetResponse get_finance_incoming_service(get_by_id_request)

Get incoming service act

Gets an incoming service act by identifier from RMS

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.incoming_service_get_response import IncomingServiceGetResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingServiceApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document retrieval by identifier request body

    try:
        # Get incoming service act
        api_response = await api_instance.get_finance_incoming_service(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingIncomingServiceApi->get_finance_incoming_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingServiceApi->get_finance_incoming_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document retrieval by identifier request body | 

### Return type

[**IncomingServiceGetResponse**](IncomingServiceGetResponse.md)

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

# **list_finance_incoming_services**
> List[IncomingServiceListItem] list_finance_incoming_services(list_request)

Export incoming service acts

Exports incoming service acts from RMS for the specified period

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.incoming_service_list_item import IncomingServiceListItem
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingServiceApi(api_client)
    list_request = iikocloud_client.ListRequest() # ListRequest | Document list retrieval request body

    try:
        # Export incoming service acts
        api_response = await api_instance.list_finance_incoming_services(list_request)
        print("The response of PublicApiInvoiceProcessingIncomingServiceApi->list_finance_incoming_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingServiceApi->list_finance_incoming_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_request** | [**ListRequest**](ListRequest.md)| Document list retrieval request body | 

### Return type

[**List[IncomingServiceListItem]**](IncomingServiceListItem.md)

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

# **post_finance_incoming_service**
> IncomingServiceSaveResponse post_finance_incoming_service(get_by_id_request)

Post incoming service act

Changes the incoming service act status from NEW to PROCESSED

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.incoming_service_save_response import IncomingServiceSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingServiceApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document posting request body

    try:
        # Post incoming service act
        api_response = await api_instance.post_finance_incoming_service(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingIncomingServiceApi->post_finance_incoming_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingServiceApi->post_finance_incoming_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document posting request body | 

### Return type

[**IncomingServiceSaveResponse**](IncomingServiceSaveResponse.md)

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

# **unpost_finance_incoming_service**
> IncomingServiceSaveResponse unpost_finance_incoming_service(get_by_id_request)

Unpost incoming service act

Changes the incoming service act status from PROCESSED to NEW

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.incoming_service_save_response import IncomingServiceSaveResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingServiceApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Document unposting request body

    try:
        # Unpost incoming service act
        api_response = await api_instance.unpost_finance_incoming_service(get_by_id_request)
        print("The response of PublicApiInvoiceProcessingIncomingServiceApi->unpost_finance_incoming_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingServiceApi->unpost_finance_incoming_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Document unposting request body | 

### Return type

[**IncomingServiceSaveResponse**](IncomingServiceSaveResponse.md)

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

# **update_finance_incoming_service**
> IncomingServiceSaveResponse update_finance_incoming_service(incoming_service_update_request)

Edit incoming service act

Edits an existing incoming service act in RMS

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.incoming_service_save_response import IncomingServiceSaveResponse
from iikocloud_client.models.incoming_service_update_request import IncomingServiceUpdateRequest
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingIncomingServiceApi(api_client)
    incoming_service_update_request = iikocloud_client.IncomingServiceUpdateRequest() # IncomingServiceUpdateRequest | Document update request body

    try:
        # Edit incoming service act
        api_response = await api_instance.update_finance_incoming_service(incoming_service_update_request)
        print("The response of PublicApiInvoiceProcessingIncomingServiceApi->update_finance_incoming_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingIncomingServiceApi->update_finance_incoming_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incoming_service_update_request** | [**IncomingServiceUpdateRequest**](IncomingServiceUpdateRequest.md)| Document update request body | 

### Return type

[**IncomingServiceSaveResponse**](IncomingServiceSaveResponse.md)

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

