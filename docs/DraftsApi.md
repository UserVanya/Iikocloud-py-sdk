# iikocloud_client.DraftsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_deliveries_drafts_by_filter_post**](DraftsApi.md#api1_deliveries_drafts_by_filter_post) | **POST** /api/1/deliveries/drafts/by_filter | Retrieve order drafts list by parameters.
[**api1_deliveries_drafts_by_id_post**](DraftsApi.md#api1_deliveries_drafts_by_id_post) | **POST** /api/1/deliveries/drafts/by_id | Retrieve order draft by ID.
[**api1_deliveries_drafts_commit_post**](DraftsApi.md#api1_deliveries_drafts_commit_post) | **POST** /api/1/deliveries/drafts/commit | Admit order draft changes and send them to Front.
[**api1_deliveries_drafts_create_post**](DraftsApi.md#api1_deliveries_drafts_create_post) | **POST** /api/1/deliveries/drafts/create | Create delivery order draft.
[**api1_deliveries_drafts_delete_post**](DraftsApi.md#api1_deliveries_drafts_delete_post) | **POST** /api/1/deliveries/drafts/delete | Delete order draft.
[**api1_deliveries_drafts_lock_post**](DraftsApi.md#api1_deliveries_drafts_lock_post) | **POST** /api/1/deliveries/drafts/lock | Lock order draft.
[**api1_deliveries_drafts_save_post**](DraftsApi.md#api1_deliveries_drafts_save_post) | **POST** /api/1/deliveries/drafts/save | Update existing delivery order draft.
[**api1_deliveries_drafts_unlock_post**](DraftsApi.md#api1_deliveries_drafts_unlock_post) | **POST** /api/1/deliveries/drafts/unlock | Unlock order draft.


# **api1_deliveries_drafts_by_filter_post**
> TransportDeliveriesDraftsFilterDraftsResponse api1_deliveries_drafts_by_filter_post(authorization, timeout=timeout, transport_deliveries_drafts_filter_drafts_request=transport_deliveries_drafts_filter_drafts_request)

Retrieve order drafts list by parameters.



 > Restriction group: `Drafts: receiving`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_deliveries_drafts_filter_drafts_request import TransportDeliveriesDraftsFilterDraftsRequest
from iikocloud_client.models.transport_deliveries_drafts_filter_drafts_response import TransportDeliveriesDraftsFilterDraftsResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DraftsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_drafts_filter_drafts_request = iikocloud_client.TransportDeliveriesDraftsFilterDraftsRequest() # TransportDeliveriesDraftsFilterDraftsRequest |  (optional)

    try:
        # Retrieve order drafts list by parameters.
        api_response = await api_instance.api1_deliveries_drafts_by_filter_post(authorization, timeout=timeout, transport_deliveries_drafts_filter_drafts_request=transport_deliveries_drafts_filter_drafts_request)
        print("The response of DraftsApi->api1_deliveries_drafts_by_filter_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->api1_deliveries_drafts_by_filter_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_drafts_filter_drafts_request** | [**TransportDeliveriesDraftsFilterDraftsRequest**](TransportDeliveriesDraftsFilterDraftsRequest.md)|  | [optional] 

### Return type

[**TransportDeliveriesDraftsFilterDraftsResponse**](TransportDeliveriesDraftsFilterDraftsResponse.md)

### Authorization

No authorization required

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

# **api1_deliveries_drafts_by_id_post**
> TransportDeliveriesDraftsGetDraftResponse api1_deliveries_drafts_by_id_post(authorization, timeout=timeout, transport_deliveries_drafts_get_draft_request=transport_deliveries_drafts_get_draft_request)

Retrieve order draft by ID.



 > Restriction group: `Drafts: receiving`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_deliveries_drafts_get_draft_request import TransportDeliveriesDraftsGetDraftRequest
from iikocloud_client.models.transport_deliveries_drafts_get_draft_response import TransportDeliveriesDraftsGetDraftResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DraftsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_drafts_get_draft_request = iikocloud_client.TransportDeliveriesDraftsGetDraftRequest() # TransportDeliveriesDraftsGetDraftRequest |  (optional)

    try:
        # Retrieve order draft by ID.
        api_response = await api_instance.api1_deliveries_drafts_by_id_post(authorization, timeout=timeout, transport_deliveries_drafts_get_draft_request=transport_deliveries_drafts_get_draft_request)
        print("The response of DraftsApi->api1_deliveries_drafts_by_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->api1_deliveries_drafts_by_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_drafts_get_draft_request** | [**TransportDeliveriesDraftsGetDraftRequest**](TransportDeliveriesDraftsGetDraftRequest.md)|  | [optional] 

### Return type

[**TransportDeliveriesDraftsGetDraftResponse**](TransportDeliveriesDraftsGetDraftResponse.md)

### Authorization

No authorization required

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

# **api1_deliveries_drafts_commit_post**
> TransportDeliveriesResponseOrderResponse api1_deliveries_drafts_commit_post(authorization, timeout=timeout, transport_deliveries_drafts_commit_draft_request=transport_deliveries_drafts_commit_draft_request)

Admit order draft changes and send them to Front.



 > Restriction group: `Drafts: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_deliveries_drafts_commit_draft_request import TransportDeliveriesDraftsCommitDraftRequest
from iikocloud_client.models.transport_deliveries_response_order_response import TransportDeliveriesResponseOrderResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DraftsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_drafts_commit_draft_request = iikocloud_client.TransportDeliveriesDraftsCommitDraftRequest() # TransportDeliveriesDraftsCommitDraftRequest |  (optional)

    try:
        # Admit order draft changes and send them to Front.
        api_response = await api_instance.api1_deliveries_drafts_commit_post(authorization, timeout=timeout, transport_deliveries_drafts_commit_draft_request=transport_deliveries_drafts_commit_draft_request)
        print("The response of DraftsApi->api1_deliveries_drafts_commit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->api1_deliveries_drafts_commit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_drafts_commit_draft_request** | [**TransportDeliveriesDraftsCommitDraftRequest**](TransportDeliveriesDraftsCommitDraftRequest.md)|  | [optional] 

### Return type

[**TransportDeliveriesResponseOrderResponse**](TransportDeliveriesResponseOrderResponse.md)

### Authorization

No authorization required

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

# **api1_deliveries_drafts_create_post**
> TransportDeliveriesDraftsCreateOrSaveDraftResponse api1_deliveries_drafts_create_post(authorization, timeout=timeout, transport_deliveries_drafts_create_draft_request=transport_deliveries_drafts_create_draft_request)

Create delivery order draft.



 > Restriction group: `Drafts: creating`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_deliveries_drafts_create_draft_request import TransportDeliveriesDraftsCreateDraftRequest
from iikocloud_client.models.transport_deliveries_drafts_create_or_save_draft_response import TransportDeliveriesDraftsCreateOrSaveDraftResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DraftsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_drafts_create_draft_request = iikocloud_client.TransportDeliveriesDraftsCreateDraftRequest() # TransportDeliveriesDraftsCreateDraftRequest |  (optional)

    try:
        # Create delivery order draft.
        api_response = await api_instance.api1_deliveries_drafts_create_post(authorization, timeout=timeout, transport_deliveries_drafts_create_draft_request=transport_deliveries_drafts_create_draft_request)
        print("The response of DraftsApi->api1_deliveries_drafts_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->api1_deliveries_drafts_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_drafts_create_draft_request** | [**TransportDeliveriesDraftsCreateDraftRequest**](TransportDeliveriesDraftsCreateDraftRequest.md)|  | [optional] 

### Return type

[**TransportDeliveriesDraftsCreateOrSaveDraftResponse**](TransportDeliveriesDraftsCreateOrSaveDraftResponse.md)

### Authorization

No authorization required

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

# **api1_deliveries_drafts_delete_post**
> TransportCommonCorrelationIdResponse api1_deliveries_drafts_delete_post(authorization, timeout=timeout, transport_deliveries_drafts_delete_draft_request=transport_deliveries_drafts_delete_draft_request)

Delete order draft.



 > Restriction group: `Drafts: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_deliveries_drafts_delete_draft_request import TransportDeliveriesDraftsDeleteDraftRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DraftsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_drafts_delete_draft_request = iikocloud_client.TransportDeliveriesDraftsDeleteDraftRequest() # TransportDeliveriesDraftsDeleteDraftRequest |  (optional)

    try:
        # Delete order draft.
        api_response = await api_instance.api1_deliveries_drafts_delete_post(authorization, timeout=timeout, transport_deliveries_drafts_delete_draft_request=transport_deliveries_drafts_delete_draft_request)
        print("The response of DraftsApi->api1_deliveries_drafts_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->api1_deliveries_drafts_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_drafts_delete_draft_request** | [**TransportDeliveriesDraftsDeleteDraftRequest**](TransportDeliveriesDraftsDeleteDraftRequest.md)|  | [optional] 

### Return type

[**TransportCommonCorrelationIdResponse**](TransportCommonCorrelationIdResponse.md)

### Authorization

No authorization required

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

# **api1_deliveries_drafts_lock_post**
> TransportCommonCorrelationIdResponse api1_deliveries_drafts_lock_post(authorization, timeout=timeout, transport_deliveries_drafts_lock_or_unlock_draft_request=transport_deliveries_drafts_lock_or_unlock_draft_request)

Lock order draft.



 > Restriction group: `Drafts: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_deliveries_drafts_lock_or_unlock_draft_request import TransportDeliveriesDraftsLockOrUnlockDraftRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DraftsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_drafts_lock_or_unlock_draft_request = iikocloud_client.TransportDeliveriesDraftsLockOrUnlockDraftRequest() # TransportDeliveriesDraftsLockOrUnlockDraftRequest |  (optional)

    try:
        # Lock order draft.
        api_response = await api_instance.api1_deliveries_drafts_lock_post(authorization, timeout=timeout, transport_deliveries_drafts_lock_or_unlock_draft_request=transport_deliveries_drafts_lock_or_unlock_draft_request)
        print("The response of DraftsApi->api1_deliveries_drafts_lock_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->api1_deliveries_drafts_lock_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_drafts_lock_or_unlock_draft_request** | [**TransportDeliveriesDraftsLockOrUnlockDraftRequest**](TransportDeliveriesDraftsLockOrUnlockDraftRequest.md)|  | [optional] 

### Return type

[**TransportCommonCorrelationIdResponse**](TransportCommonCorrelationIdResponse.md)

### Authorization

No authorization required

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

# **api1_deliveries_drafts_save_post**
> TransportDeliveriesDraftsCreateOrSaveDraftResponse api1_deliveries_drafts_save_post(authorization, timeout=timeout, transport_deliveries_drafts_save_draft_request=transport_deliveries_drafts_save_draft_request)

Update existing delivery order draft.



 > Restriction group: `Drafts: creating`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_deliveries_drafts_create_or_save_draft_response import TransportDeliveriesDraftsCreateOrSaveDraftResponse
from iikocloud_client.models.transport_deliveries_drafts_save_draft_request import TransportDeliveriesDraftsSaveDraftRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DraftsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_drafts_save_draft_request = iikocloud_client.TransportDeliveriesDraftsSaveDraftRequest() # TransportDeliveriesDraftsSaveDraftRequest |  (optional)

    try:
        # Update existing delivery order draft.
        api_response = await api_instance.api1_deliveries_drafts_save_post(authorization, timeout=timeout, transport_deliveries_drafts_save_draft_request=transport_deliveries_drafts_save_draft_request)
        print("The response of DraftsApi->api1_deliveries_drafts_save_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->api1_deliveries_drafts_save_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_drafts_save_draft_request** | [**TransportDeliveriesDraftsSaveDraftRequest**](TransportDeliveriesDraftsSaveDraftRequest.md)|  | [optional] 

### Return type

[**TransportDeliveriesDraftsCreateOrSaveDraftResponse**](TransportDeliveriesDraftsCreateOrSaveDraftResponse.md)

### Authorization

No authorization required

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

# **api1_deliveries_drafts_unlock_post**
> TransportCommonCorrelationIdResponse api1_deliveries_drafts_unlock_post(authorization, timeout=timeout, transport_deliveries_drafts_lock_or_unlock_draft_request=transport_deliveries_drafts_lock_or_unlock_draft_request)

Unlock order draft.



 > Restriction group: `Drafts: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_deliveries_drafts_lock_or_unlock_draft_request import TransportDeliveriesDraftsLockOrUnlockDraftRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DraftsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_drafts_lock_or_unlock_draft_request = iikocloud_client.TransportDeliveriesDraftsLockOrUnlockDraftRequest() # TransportDeliveriesDraftsLockOrUnlockDraftRequest |  (optional)

    try:
        # Unlock order draft.
        api_response = await api_instance.api1_deliveries_drafts_unlock_post(authorization, timeout=timeout, transport_deliveries_drafts_lock_or_unlock_draft_request=transport_deliveries_drafts_lock_or_unlock_draft_request)
        print("The response of DraftsApi->api1_deliveries_drafts_unlock_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftsApi->api1_deliveries_drafts_unlock_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_drafts_lock_or_unlock_draft_request** | [**TransportDeliveriesDraftsLockOrUnlockDraftRequest**](TransportDeliveriesDraftsLockOrUnlockDraftRequest.md)|  | [optional] 

### Return type

[**TransportCommonCorrelationIdResponse**](TransportCommonCorrelationIdResponse.md)

### Authorization

No authorization required

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

