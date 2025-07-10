# iiko_cloud_client.DictionariesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_cancel_causes_post**](DictionariesApi.md#api1_cancel_causes_post) | **POST** /api/1/cancel_causes | Delivery cancel causes.
[**api1_deliveries_order_types_post**](DictionariesApi.md#api1_deliveries_order_types_post) | **POST** /api/1/deliveries/order_types | Order types.
[**api1_discounts_post**](DictionariesApi.md#api1_discounts_post) | **POST** /api/1/discounts | Discounts / surcharges.
[**api1_payment_types_post**](DictionariesApi.md#api1_payment_types_post) | **POST** /api/1/payment_types | Payment types.
[**api1_removal_types_post**](DictionariesApi.md#api1_removal_types_post) | **POST** /api/1/removal_types | Removal types (reasons for deletion).
[**api1_tips_types_post**](DictionariesApi.md#api1_tips_types_post) | **POST** /api/1/tips_types | Get tips types for api-login&#x60;s rms group.


# **api1_cancel_causes_post**
> TransportCancelCausesCancelCausesResponse api1_cancel_causes_post(authorization, timeout=timeout, transport_cancel_causes_cancel_causes_request=transport_cancel_causes_cancel_causes_request)

Delivery cancel causes.



 > Allowed from version `7.7.1`.

 > Restriction group: `Data: dictionaries`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_cancel_causes_cancel_causes_request import TransportCancelCausesCancelCausesRequest
from iiko_cloud_client.models.transport_cancel_causes_cancel_causes_response import TransportCancelCausesCancelCausesResponse
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DictionariesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_cancel_causes_cancel_causes_request = iiko_cloud_client.TransportCancelCausesCancelCausesRequest() # TransportCancelCausesCancelCausesRequest |  (optional)

    try:
        # Delivery cancel causes.
        api_response = await api_instance.api1_cancel_causes_post(authorization, timeout=timeout, transport_cancel_causes_cancel_causes_request=transport_cancel_causes_cancel_causes_request)
        print("The response of DictionariesApi->api1_cancel_causes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->api1_cancel_causes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_cancel_causes_cancel_causes_request** | [**TransportCancelCausesCancelCausesRequest**](TransportCancelCausesCancelCausesRequest.md)|  | [optional] 

### Return type

[**TransportCancelCausesCancelCausesResponse**](TransportCancelCausesCancelCausesResponse.md)

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

# **api1_deliveries_order_types_post**
> TransportOrderTypesOrderTypesResponse api1_deliveries_order_types_post(authorization, timeout=timeout, transport_order_types_order_types_request=transport_order_types_order_types_request)

Order types.



 > Restriction group: `Data: dictionaries`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_order_types_order_types_request import TransportOrderTypesOrderTypesRequest
from iiko_cloud_client.models.transport_order_types_order_types_response import TransportOrderTypesOrderTypesResponse
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DictionariesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_order_types_order_types_request = iiko_cloud_client.TransportOrderTypesOrderTypesRequest() # TransportOrderTypesOrderTypesRequest |  (optional)

    try:
        # Order types.
        api_response = await api_instance.api1_deliveries_order_types_post(authorization, timeout=timeout, transport_order_types_order_types_request=transport_order_types_order_types_request)
        print("The response of DictionariesApi->api1_deliveries_order_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->api1_deliveries_order_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_order_types_order_types_request** | [**TransportOrderTypesOrderTypesRequest**](TransportOrderTypesOrderTypesRequest.md)|  | [optional] 

### Return type

[**TransportOrderTypesOrderTypesResponse**](TransportOrderTypesOrderTypesResponse.md)

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

# **api1_discounts_post**
> TransportDiscountsDiscountsResponse api1_discounts_post(authorization, timeout=timeout, transport_discounts_discounts_request=transport_discounts_discounts_request)

Discounts / surcharges.



 > Restriction group: `Data: dictionaries`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_discounts_discounts_request import TransportDiscountsDiscountsRequest
from iiko_cloud_client.models.transport_discounts_discounts_response import TransportDiscountsDiscountsResponse
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DictionariesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_discounts_discounts_request = iiko_cloud_client.TransportDiscountsDiscountsRequest() # TransportDiscountsDiscountsRequest |  (optional)

    try:
        # Discounts / surcharges.
        api_response = await api_instance.api1_discounts_post(authorization, timeout=timeout, transport_discounts_discounts_request=transport_discounts_discounts_request)
        print("The response of DictionariesApi->api1_discounts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->api1_discounts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_discounts_discounts_request** | [**TransportDiscountsDiscountsRequest**](TransportDiscountsDiscountsRequest.md)|  | [optional] 

### Return type

[**TransportDiscountsDiscountsResponse**](TransportDiscountsDiscountsResponse.md)

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

# **api1_payment_types_post**
> TransportPaymentTypesPaymentTypesResponse api1_payment_types_post(authorization, timeout=timeout, transport_payment_types_payment_types_request=transport_payment_types_payment_types_request)

Payment types.



 > Restriction group: `Data: dictionaries`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_payment_types_payment_types_request import TransportPaymentTypesPaymentTypesRequest
from iiko_cloud_client.models.transport_payment_types_payment_types_response import TransportPaymentTypesPaymentTypesResponse
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DictionariesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_payment_types_payment_types_request = iiko_cloud_client.TransportPaymentTypesPaymentTypesRequest() # TransportPaymentTypesPaymentTypesRequest |  (optional)

    try:
        # Payment types.
        api_response = await api_instance.api1_payment_types_post(authorization, timeout=timeout, transport_payment_types_payment_types_request=transport_payment_types_payment_types_request)
        print("The response of DictionariesApi->api1_payment_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->api1_payment_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_payment_types_payment_types_request** | [**TransportPaymentTypesPaymentTypesRequest**](TransportPaymentTypesPaymentTypesRequest.md)|  | [optional] 

### Return type

[**TransportPaymentTypesPaymentTypesResponse**](TransportPaymentTypesPaymentTypesResponse.md)

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

# **api1_removal_types_post**
> TransportRemovalTypesRemovalTypesResponse api1_removal_types_post(authorization, timeout=timeout, transport_removal_types_removal_types_request=transport_removal_types_removal_types_request)

Removal types (reasons for deletion).



 > Allowed from version `7.5.3`.

 > Restriction group: `Data: dictionaries`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_removal_types_removal_types_request import TransportRemovalTypesRemovalTypesRequest
from iiko_cloud_client.models.transport_removal_types_removal_types_response import TransportRemovalTypesRemovalTypesResponse
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DictionariesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_removal_types_removal_types_request = iiko_cloud_client.TransportRemovalTypesRemovalTypesRequest() # TransportRemovalTypesRemovalTypesRequest |  (optional)

    try:
        # Removal types (reasons for deletion).
        api_response = await api_instance.api1_removal_types_post(authorization, timeout=timeout, transport_removal_types_removal_types_request=transport_removal_types_removal_types_request)
        print("The response of DictionariesApi->api1_removal_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->api1_removal_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_removal_types_removal_types_request** | [**TransportRemovalTypesRemovalTypesRequest**](TransportRemovalTypesRemovalTypesRequest.md)|  | [optional] 

### Return type

[**TransportRemovalTypesRemovalTypesResponse**](TransportRemovalTypesRemovalTypesResponse.md)

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

# **api1_tips_types_post**
> TransportTipsTypesTipsTypesResponse api1_tips_types_post(authorization, timeout=timeout)

Get tips types for api-login`s rms group.



 > Allowed from version `7.7.4`.

 > Restriction group: `Data: dictionaries`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_tips_types_tips_types_response import TransportTipsTypesTipsTypesResponse
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DictionariesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)

    try:
        # Get tips types for api-login`s rms group.
        api_response = await api_instance.api1_tips_types_post(authorization, timeout=timeout)
        print("The response of DictionariesApi->api1_tips_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->api1_tips_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]

### Return type

[**TransportTipsTypesTipsTypesResponse**](TransportTipsTypesTipsTypesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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

