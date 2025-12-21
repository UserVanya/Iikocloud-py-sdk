# iikocloud_client.DictionariesApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_causes_post**](DictionariesApi.md#cancel_causes_post) | **POST** /cancel_causes | Delivery cancel causes.
[**deliveries_order_types_post**](DictionariesApi.md#deliveries_order_types_post) | **POST** /deliveries/order_types | Order types.
[**discounts_post**](DictionariesApi.md#discounts_post) | **POST** /discounts | Discounts / surcharges.
[**payment_types_post**](DictionariesApi.md#payment_types_post) | **POST** /payment_types | Payment types.
[**removal_types_post**](DictionariesApi.md#removal_types_post) | **POST** /removal_types | Removal types (reasons for deletion).
[**tips_types_post**](DictionariesApi.md#tips_types_post) | **POST** /tips_types | Get tips types for api-login&#x60;s rms group.


# **cancel_causes_post**
> CancelCausesCancelCausesResponse cancel_causes_post(timeout=timeout, cancel_causes_cancel_causes_request=cancel_causes_cancel_causes_request)

Delivery cancel causes.



 > Allowed from version `7.7.1`.

 > Restriction group: `Data: dictionaries`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.cancel_causes_cancel_causes_request import CancelCausesCancelCausesRequest
from iikocloud_client.models.cancel_causes_cancel_causes_response import CancelCausesCancelCausesResponse
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
    api_instance = iikocloud_client.DictionariesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    cancel_causes_cancel_causes_request = iikocloud_client.CancelCausesCancelCausesRequest() # CancelCausesCancelCausesRequest |  (optional)

    try:
        # Delivery cancel causes.
        api_response = await api_instance.cancel_causes_post(timeout=timeout, cancel_causes_cancel_causes_request=cancel_causes_cancel_causes_request)
        print("The response of DictionariesApi->cancel_causes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->cancel_causes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **cancel_causes_cancel_causes_request** | [**CancelCausesCancelCausesRequest**](CancelCausesCancelCausesRequest.md)|  | [optional] 

### Return type

[**CancelCausesCancelCausesResponse**](CancelCausesCancelCausesResponse.md)

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

# **deliveries_order_types_post**
> OrderTypesOrderTypesResponse deliveries_order_types_post(timeout=timeout, order_types_order_types_request=order_types_order_types_request)

Order types.



 > Restriction group: `Data: dictionaries`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.order_types_order_types_request import OrderTypesOrderTypesRequest
from iikocloud_client.models.order_types_order_types_response import OrderTypesOrderTypesResponse
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
    api_instance = iikocloud_client.DictionariesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    order_types_order_types_request = iikocloud_client.OrderTypesOrderTypesRequest() # OrderTypesOrderTypesRequest |  (optional)

    try:
        # Order types.
        api_response = await api_instance.deliveries_order_types_post(timeout=timeout, order_types_order_types_request=order_types_order_types_request)
        print("The response of DictionariesApi->deliveries_order_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->deliveries_order_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **order_types_order_types_request** | [**OrderTypesOrderTypesRequest**](OrderTypesOrderTypesRequest.md)|  | [optional] 

### Return type

[**OrderTypesOrderTypesResponse**](OrderTypesOrderTypesResponse.md)

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

# **discounts_post**
> DiscountsDiscountsResponse discounts_post(timeout=timeout, discounts_discounts_request=discounts_discounts_request)

Discounts / surcharges.



 > Restriction group: `Data: dictionaries`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.discounts_discounts_request import DiscountsDiscountsRequest
from iikocloud_client.models.discounts_discounts_response import DiscountsDiscountsResponse
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
    api_instance = iikocloud_client.DictionariesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    discounts_discounts_request = iikocloud_client.DiscountsDiscountsRequest() # DiscountsDiscountsRequest |  (optional)

    try:
        # Discounts / surcharges.
        api_response = await api_instance.discounts_post(timeout=timeout, discounts_discounts_request=discounts_discounts_request)
        print("The response of DictionariesApi->discounts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->discounts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **discounts_discounts_request** | [**DiscountsDiscountsRequest**](DiscountsDiscountsRequest.md)|  | [optional] 

### Return type

[**DiscountsDiscountsResponse**](DiscountsDiscountsResponse.md)

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

# **payment_types_post**
> PaymentTypesPaymentTypesResponse payment_types_post(timeout=timeout, payment_types_payment_types_request=payment_types_payment_types_request)

Payment types.



 > Restriction group: `Data: dictionaries`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.payment_types_payment_types_request import PaymentTypesPaymentTypesRequest
from iikocloud_client.models.payment_types_payment_types_response import PaymentTypesPaymentTypesResponse
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
    api_instance = iikocloud_client.DictionariesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    payment_types_payment_types_request = iikocloud_client.PaymentTypesPaymentTypesRequest() # PaymentTypesPaymentTypesRequest |  (optional)

    try:
        # Payment types.
        api_response = await api_instance.payment_types_post(timeout=timeout, payment_types_payment_types_request=payment_types_payment_types_request)
        print("The response of DictionariesApi->payment_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->payment_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **payment_types_payment_types_request** | [**PaymentTypesPaymentTypesRequest**](PaymentTypesPaymentTypesRequest.md)|  | [optional] 

### Return type

[**PaymentTypesPaymentTypesResponse**](PaymentTypesPaymentTypesResponse.md)

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

# **removal_types_post**
> RemovalTypesRemovalTypesResponse removal_types_post(timeout=timeout, removal_types_removal_types_request=removal_types_removal_types_request)

Removal types (reasons for deletion).



 > Allowed from version `7.5.3`.

 > Restriction group: `Data: dictionaries`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.removal_types_removal_types_request import RemovalTypesRemovalTypesRequest
from iikocloud_client.models.removal_types_removal_types_response import RemovalTypesRemovalTypesResponse
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
    api_instance = iikocloud_client.DictionariesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    removal_types_removal_types_request = iikocloud_client.RemovalTypesRemovalTypesRequest() # RemovalTypesRemovalTypesRequest |  (optional)

    try:
        # Removal types (reasons for deletion).
        api_response = await api_instance.removal_types_post(timeout=timeout, removal_types_removal_types_request=removal_types_removal_types_request)
        print("The response of DictionariesApi->removal_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->removal_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **removal_types_removal_types_request** | [**RemovalTypesRemovalTypesRequest**](RemovalTypesRemovalTypesRequest.md)|  | [optional] 

### Return type

[**RemovalTypesRemovalTypesResponse**](RemovalTypesRemovalTypesResponse.md)

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

# **tips_types_post**
> TipsTypesTipsTypesResponse tips_types_post(timeout=timeout)

Get tips types for api-login`s rms group.



 > Allowed from version `7.7.4`.

 > Restriction group: `Data: dictionaries`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.tips_types_tips_types_response import TipsTypesTipsTypesResponse
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
    api_instance = iikocloud_client.DictionariesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)

    try:
        # Get tips types for api-login`s rms group.
        api_response = await api_instance.tips_types_post(timeout=timeout)
        print("The response of DictionariesApi->tips_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->tips_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]

### Return type

[**TipsTypesTipsTypesResponse**](TipsTypesTipsTypesResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

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

