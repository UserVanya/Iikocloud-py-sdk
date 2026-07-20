# iikocloud_client.DraftsApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commit_delivery_draft**](DraftsApi.md#commit_delivery_draft) | **POST** /api/1/deliveries/drafts/commit | Admit order draft changes and send them to Front.
[**create_delivery_draft**](DraftsApi.md#create_delivery_draft) | **POST** /api/1/deliveries/drafts/create | Create delivery order draft.
[**delete_delivery_draft**](DraftsApi.md#delete_delivery_draft) | **POST** /api/1/deliveries/drafts/delete | Delete order draft.
[**get_delivery_draft_by_id**](DraftsApi.md#get_delivery_draft_by_id) | **POST** /api/1/deliveries/drafts/by_id | Retrieve order draft by ID.
[**get_delivery_drafts_by_filter**](DraftsApi.md#get_delivery_drafts_by_filter) | **POST** /api/1/deliveries/drafts/by_filter | Retrieve order drafts list by parameters.
[**lock_delivery_draft**](DraftsApi.md#lock_delivery_draft) | **POST** /api/1/deliveries/drafts/lock | Lock order draft.
[**save_delivery_draft**](DraftsApi.md#save_delivery_draft) | **POST** /api/1/deliveries/drafts/save | Update existing delivery order draft.
[**unlock_delivery_draft**](DraftsApi.md#unlock_delivery_draft) | **POST** /api/1/deliveries/drafts/unlock | Unlock order draft.


# **commit_delivery_draft**
> OrderResponse commit_delivery_draft(timeout=timeout, commit_draft_request=commit_draft_request)

Admit order draft changes and send them to Front.



 > Restriction group: `Drafts: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.commit_draft_request import CommitDraftRequest
from iikocloud_client.models.order_response import OrderResponse
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
    api_instance = iikocloud_client.DraftsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    commit_draft_request = iikocloud_client.CommitDraftRequest() # CommitDraftRequest |  (optional)

    try:
        # Admit order draft changes and send them to Front.
        api_response = await api_instance.commit_delivery_draft(timeout=timeout, commit_draft_request=commit_draft_request)
        print("The response of DraftsApi->commit_delivery_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->commit_delivery_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **commit_draft_request** | [**CommitDraftRequest**](CommitDraftRequest.md)|  | [optional] 

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_delivery_draft**
> CreateOrSaveDraftResponse create_delivery_draft(timeout=timeout, create_draft_request=create_draft_request)

Create delivery order draft.



 > Restriction group: `Drafts: creating`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.create_draft_request import CreateDraftRequest
from iikocloud_client.models.create_or_save_draft_response import CreateOrSaveDraftResponse
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
    api_instance = iikocloud_client.DraftsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    create_draft_request = iikocloud_client.CreateDraftRequest() # CreateDraftRequest |  (optional)

    try:
        # Create delivery order draft.
        api_response = await api_instance.create_delivery_draft(timeout=timeout, create_draft_request=create_draft_request)
        print("The response of DraftsApi->create_delivery_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->create_delivery_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **create_draft_request** | [**CreateDraftRequest**](CreateDraftRequest.md)|  | [optional] 

### Return type

[**CreateOrSaveDraftResponse**](CreateOrSaveDraftResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_delivery_draft**
> CorrelationIdResponse delete_delivery_draft(timeout=timeout, delete_draft_request=delete_draft_request)

Delete order draft.



 > Restriction group: `Drafts: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
from iikocloud_client.models.delete_draft_request import DeleteDraftRequest
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
    api_instance = iikocloud_client.DraftsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    delete_draft_request = iikocloud_client.DeleteDraftRequest() # DeleteDraftRequest |  (optional)

    try:
        # Delete order draft.
        api_response = await api_instance.delete_delivery_draft(timeout=timeout, delete_draft_request=delete_draft_request)
        print("The response of DraftsApi->delete_delivery_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->delete_delivery_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **delete_draft_request** | [**DeleteDraftRequest**](DeleteDraftRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delivery_draft_by_id**
> GetDraftResponse get_delivery_draft_by_id(timeout=timeout, get_draft_request=get_draft_request)

Retrieve order draft by ID.



 > Restriction group: `Drafts: receiving`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_draft_request import GetDraftRequest
from iikocloud_client.models.get_draft_response import GetDraftResponse
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
    api_instance = iikocloud_client.DraftsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_draft_request = iikocloud_client.GetDraftRequest() # GetDraftRequest |  (optional)

    try:
        # Retrieve order draft by ID.
        api_response = await api_instance.get_delivery_draft_by_id(timeout=timeout, get_draft_request=get_draft_request)
        print("The response of DraftsApi->get_delivery_draft_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->get_delivery_draft_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_draft_request** | [**GetDraftRequest**](GetDraftRequest.md)|  | [optional] 

### Return type

[**GetDraftResponse**](GetDraftResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delivery_drafts_by_filter**
> FilterDraftsResponse get_delivery_drafts_by_filter(timeout=timeout, filter_drafts_request=filter_drafts_request)

Retrieve order drafts list by parameters.



 > Restriction group: `Drafts: receiving`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.filter_drafts_request import FilterDraftsRequest
from iikocloud_client.models.filter_drafts_response import FilterDraftsResponse
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
    api_instance = iikocloud_client.DraftsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    filter_drafts_request = iikocloud_client.FilterDraftsRequest() # FilterDraftsRequest |  (optional)

    try:
        # Retrieve order drafts list by parameters.
        api_response = await api_instance.get_delivery_drafts_by_filter(timeout=timeout, filter_drafts_request=filter_drafts_request)
        print("The response of DraftsApi->get_delivery_drafts_by_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->get_delivery_drafts_by_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **filter_drafts_request** | [**FilterDraftsRequest**](FilterDraftsRequest.md)|  | [optional] 

### Return type

[**FilterDraftsResponse**](FilterDraftsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_delivery_draft**
> CorrelationIdResponse lock_delivery_draft(timeout=timeout, lock_or_unlock_draft_request=lock_or_unlock_draft_request)

Lock order draft.



 > Restriction group: `Drafts: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
from iikocloud_client.models.lock_or_unlock_draft_request import LockOrUnlockDraftRequest
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
    api_instance = iikocloud_client.DraftsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    lock_or_unlock_draft_request = iikocloud_client.LockOrUnlockDraftRequest() # LockOrUnlockDraftRequest |  (optional)

    try:
        # Lock order draft.
        api_response = await api_instance.lock_delivery_draft(timeout=timeout, lock_or_unlock_draft_request=lock_or_unlock_draft_request)
        print("The response of DraftsApi->lock_delivery_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->lock_delivery_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **lock_or_unlock_draft_request** | [**LockOrUnlockDraftRequest**](LockOrUnlockDraftRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_delivery_draft**
> CreateOrSaveDraftResponse save_delivery_draft(timeout=timeout, save_draft_request=save_draft_request)

Update existing delivery order draft.



 > Restriction group: `Drafts: creating`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.create_or_save_draft_response import CreateOrSaveDraftResponse
from iikocloud_client.models.save_draft_request import SaveDraftRequest
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
    api_instance = iikocloud_client.DraftsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    save_draft_request = iikocloud_client.SaveDraftRequest() # SaveDraftRequest |  (optional)

    try:
        # Update existing delivery order draft.
        api_response = await api_instance.save_delivery_draft(timeout=timeout, save_draft_request=save_draft_request)
        print("The response of DraftsApi->save_delivery_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->save_delivery_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **save_draft_request** | [**SaveDraftRequest**](SaveDraftRequest.md)|  | [optional] 

### Return type

[**CreateOrSaveDraftResponse**](CreateOrSaveDraftResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlock_delivery_draft**
> CorrelationIdResponse unlock_delivery_draft(timeout=timeout, lock_or_unlock_draft_request=lock_or_unlock_draft_request)

Unlock order draft.



 > Restriction group: `Drafts: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
from iikocloud_client.models.lock_or_unlock_draft_request import LockOrUnlockDraftRequest
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
    api_instance = iikocloud_client.DraftsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    lock_or_unlock_draft_request = iikocloud_client.LockOrUnlockDraftRequest() # LockOrUnlockDraftRequest |  (optional)

    try:
        # Unlock order draft.
        api_response = await api_instance.unlock_delivery_draft(timeout=timeout, lock_or_unlock_draft_request=lock_or_unlock_draft_request)
        print("The response of DraftsApi->unlock_delivery_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->unlock_delivery_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **lock_or_unlock_draft_request** | [**LockOrUnlockDraftRequest**](LockOrUnlockDraftRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

