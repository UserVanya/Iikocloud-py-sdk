# iikocloud_client.DraftsApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deliveries_drafts_by_filter_post**](DraftsApi.md#deliveries_drafts_by_filter_post) | **POST** /deliveries/drafts/by_filter | Retrieve order drafts list by parameters.
[**deliveries_drafts_by_id_post**](DraftsApi.md#deliveries_drafts_by_id_post) | **POST** /deliveries/drafts/by_id | Retrieve order draft by ID.
[**deliveries_drafts_commit_post**](DraftsApi.md#deliveries_drafts_commit_post) | **POST** /deliveries/drafts/commit | Admit order draft changes and send them to Front.
[**deliveries_drafts_create_post**](DraftsApi.md#deliveries_drafts_create_post) | **POST** /deliveries/drafts/create | Create delivery order draft.
[**deliveries_drafts_delete_post**](DraftsApi.md#deliveries_drafts_delete_post) | **POST** /deliveries/drafts/delete | Delete order draft.
[**deliveries_drafts_lock_post**](DraftsApi.md#deliveries_drafts_lock_post) | **POST** /deliveries/drafts/lock | Lock order draft.
[**deliveries_drafts_save_post**](DraftsApi.md#deliveries_drafts_save_post) | **POST** /deliveries/drafts/save | Update existing delivery order draft.
[**deliveries_drafts_unlock_post**](DraftsApi.md#deliveries_drafts_unlock_post) | **POST** /deliveries/drafts/unlock | Unlock order draft.


# **deliveries_drafts_by_filter_post**
> IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsResponse deliveries_drafts_by_filter_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_drafts_filter_drafts_request=iiko_transport_public_api_contracts_deliveries_drafts_filter_drafts_request)

Retrieve order drafts list by parameters.



 > Restriction group: `Drafts: receiving`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_drafts_filter_drafts_request import IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_drafts_filter_drafts_response import IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DraftsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_drafts_filter_drafts_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsRequest() # IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsRequest |  (optional)

    try:
        # Retrieve order drafts list by parameters.
        api_response = await api_instance.deliveries_drafts_by_filter_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_drafts_filter_drafts_request=iiko_transport_public_api_contracts_deliveries_drafts_filter_drafts_request)
        print("The response of DraftsApi->deliveries_drafts_by_filter_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->deliveries_drafts_by_filter_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_drafts_filter_drafts_request** | [**IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsRequest**](IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsResponse**](IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Server Error |  -  |
**408** | Request Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deliveries_drafts_by_id_post**
> IikoTransportPublicApiContractsDeliveriesDraftsGetDraftResponse deliveries_drafts_by_id_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_drafts_get_draft_request=iiko_transport_public_api_contracts_deliveries_drafts_get_draft_request)

Retrieve order draft by ID.



 > Restriction group: `Drafts: receiving`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_drafts_get_draft_request import IikoTransportPublicApiContractsDeliveriesDraftsGetDraftRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_drafts_get_draft_response import IikoTransportPublicApiContractsDeliveriesDraftsGetDraftResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DraftsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_drafts_get_draft_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesDraftsGetDraftRequest() # IikoTransportPublicApiContractsDeliveriesDraftsGetDraftRequest |  (optional)

    try:
        # Retrieve order draft by ID.
        api_response = await api_instance.deliveries_drafts_by_id_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_drafts_get_draft_request=iiko_transport_public_api_contracts_deliveries_drafts_get_draft_request)
        print("The response of DraftsApi->deliveries_drafts_by_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->deliveries_drafts_by_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_drafts_get_draft_request** | [**IikoTransportPublicApiContractsDeliveriesDraftsGetDraftRequest**](IikoTransportPublicApiContractsDeliveriesDraftsGetDraftRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsDeliveriesDraftsGetDraftResponse**](IikoTransportPublicApiContractsDeliveriesDraftsGetDraftResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Server Error |  -  |
**408** | Request Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deliveries_drafts_commit_post**
> IikoTransportPublicApiContractsDeliveriesResponseOrderResponse deliveries_drafts_commit_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_drafts_commit_draft_request=iiko_transport_public_api_contracts_deliveries_drafts_commit_draft_request)

Admit order draft changes and send them to Front.



 > Restriction group: `Drafts: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_drafts_commit_draft_request import IikoTransportPublicApiContractsDeliveriesDraftsCommitDraftRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_response import IikoTransportPublicApiContractsDeliveriesResponseOrderResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DraftsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_drafts_commit_draft_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesDraftsCommitDraftRequest() # IikoTransportPublicApiContractsDeliveriesDraftsCommitDraftRequest |  (optional)

    try:
        # Admit order draft changes and send them to Front.
        api_response = await api_instance.deliveries_drafts_commit_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_drafts_commit_draft_request=iiko_transport_public_api_contracts_deliveries_drafts_commit_draft_request)
        print("The response of DraftsApi->deliveries_drafts_commit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->deliveries_drafts_commit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_drafts_commit_draft_request** | [**IikoTransportPublicApiContractsDeliveriesDraftsCommitDraftRequest**](IikoTransportPublicApiContractsDeliveriesDraftsCommitDraftRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsDeliveriesResponseOrderResponse**](IikoTransportPublicApiContractsDeliveriesResponseOrderResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Server Error |  -  |
**408** | Request Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deliveries_drafts_create_post**
> IikoTransportPublicApiContractsDeliveriesDraftsCreateOrSaveDraftResponse deliveries_drafts_create_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_drafts_create_draft_request=iiko_transport_public_api_contracts_deliveries_drafts_create_draft_request)

Create delivery order draft.



 > Restriction group: `Drafts: creating`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_drafts_create_draft_request import IikoTransportPublicApiContractsDeliveriesDraftsCreateDraftRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_drafts_create_or_save_draft_response import IikoTransportPublicApiContractsDeliveriesDraftsCreateOrSaveDraftResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DraftsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_drafts_create_draft_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesDraftsCreateDraftRequest() # IikoTransportPublicApiContractsDeliveriesDraftsCreateDraftRequest |  (optional)

    try:
        # Create delivery order draft.
        api_response = await api_instance.deliveries_drafts_create_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_drafts_create_draft_request=iiko_transport_public_api_contracts_deliveries_drafts_create_draft_request)
        print("The response of DraftsApi->deliveries_drafts_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->deliveries_drafts_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_drafts_create_draft_request** | [**IikoTransportPublicApiContractsDeliveriesDraftsCreateDraftRequest**](IikoTransportPublicApiContractsDeliveriesDraftsCreateDraftRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsDeliveriesDraftsCreateOrSaveDraftResponse**](IikoTransportPublicApiContractsDeliveriesDraftsCreateOrSaveDraftResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Server Error |  -  |
**408** | Request Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deliveries_drafts_delete_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_drafts_delete_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_drafts_delete_draft_request=iiko_transport_public_api_contracts_deliveries_drafts_delete_draft_request)

Delete order draft.



 > Restriction group: `Drafts: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_drafts_delete_draft_request import IikoTransportPublicApiContractsDeliveriesDraftsDeleteDraftRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DraftsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_drafts_delete_draft_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesDraftsDeleteDraftRequest() # IikoTransportPublicApiContractsDeliveriesDraftsDeleteDraftRequest |  (optional)

    try:
        # Delete order draft.
        api_response = await api_instance.deliveries_drafts_delete_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_drafts_delete_draft_request=iiko_transport_public_api_contracts_deliveries_drafts_delete_draft_request)
        print("The response of DraftsApi->deliveries_drafts_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->deliveries_drafts_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_drafts_delete_draft_request** | [**IikoTransportPublicApiContractsDeliveriesDraftsDeleteDraftRequest**](IikoTransportPublicApiContractsDeliveriesDraftsDeleteDraftRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Server Error |  -  |
**408** | Request Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deliveries_drafts_lock_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_drafts_lock_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_drafts_lock_or_unlock_draft_request=iiko_transport_public_api_contracts_deliveries_drafts_lock_or_unlock_draft_request)

Lock order draft.



 > Restriction group: `Drafts: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_drafts_lock_or_unlock_draft_request import IikoTransportPublicApiContractsDeliveriesDraftsLockOrUnlockDraftRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DraftsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_drafts_lock_or_unlock_draft_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesDraftsLockOrUnlockDraftRequest() # IikoTransportPublicApiContractsDeliveriesDraftsLockOrUnlockDraftRequest |  (optional)

    try:
        # Lock order draft.
        api_response = await api_instance.deliveries_drafts_lock_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_drafts_lock_or_unlock_draft_request=iiko_transport_public_api_contracts_deliveries_drafts_lock_or_unlock_draft_request)
        print("The response of DraftsApi->deliveries_drafts_lock_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->deliveries_drafts_lock_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_drafts_lock_or_unlock_draft_request** | [**IikoTransportPublicApiContractsDeliveriesDraftsLockOrUnlockDraftRequest**](IikoTransportPublicApiContractsDeliveriesDraftsLockOrUnlockDraftRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Server Error |  -  |
**408** | Request Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deliveries_drafts_save_post**
> IikoTransportPublicApiContractsDeliveriesDraftsCreateOrSaveDraftResponse deliveries_drafts_save_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_drafts_save_draft_request=iiko_transport_public_api_contracts_deliveries_drafts_save_draft_request)

Update existing delivery order draft.



 > Restriction group: `Drafts: creating`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_drafts_create_or_save_draft_response import IikoTransportPublicApiContractsDeliveriesDraftsCreateOrSaveDraftResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_drafts_save_draft_request import IikoTransportPublicApiContractsDeliveriesDraftsSaveDraftRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DraftsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_drafts_save_draft_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesDraftsSaveDraftRequest() # IikoTransportPublicApiContractsDeliveriesDraftsSaveDraftRequest |  (optional)

    try:
        # Update existing delivery order draft.
        api_response = await api_instance.deliveries_drafts_save_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_drafts_save_draft_request=iiko_transport_public_api_contracts_deliveries_drafts_save_draft_request)
        print("The response of DraftsApi->deliveries_drafts_save_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->deliveries_drafts_save_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_drafts_save_draft_request** | [**IikoTransportPublicApiContractsDeliveriesDraftsSaveDraftRequest**](IikoTransportPublicApiContractsDeliveriesDraftsSaveDraftRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsDeliveriesDraftsCreateOrSaveDraftResponse**](IikoTransportPublicApiContractsDeliveriesDraftsCreateOrSaveDraftResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Server Error |  -  |
**408** | Request Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deliveries_drafts_unlock_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_drafts_unlock_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_drafts_lock_or_unlock_draft_request=iiko_transport_public_api_contracts_deliveries_drafts_lock_or_unlock_draft_request)

Unlock order draft.



 > Restriction group: `Drafts: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_drafts_lock_or_unlock_draft_request import IikoTransportPublicApiContractsDeliveriesDraftsLockOrUnlockDraftRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DraftsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_drafts_lock_or_unlock_draft_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesDraftsLockOrUnlockDraftRequest() # IikoTransportPublicApiContractsDeliveriesDraftsLockOrUnlockDraftRequest |  (optional)

    try:
        # Unlock order draft.
        api_response = await api_instance.deliveries_drafts_unlock_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_drafts_lock_or_unlock_draft_request=iiko_transport_public_api_contracts_deliveries_drafts_lock_or_unlock_draft_request)
        print("The response of DraftsApi->deliveries_drafts_unlock_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->deliveries_drafts_unlock_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_drafts_lock_or_unlock_draft_request** | [**IikoTransportPublicApiContractsDeliveriesDraftsLockOrUnlockDraftRequest**](IikoTransportPublicApiContractsDeliveriesDraftsLockOrUnlockDraftRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Server Error |  -  |
**408** | Request Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

