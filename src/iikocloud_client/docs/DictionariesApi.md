# iikocloud_client.DictionariesApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cancel_causes**](DictionariesApi.md#get_cancel_causes) | **POST** /api/1/cancel_causes | Delivery cancel causes.
[**get_delivery_order_types**](DictionariesApi.md#get_delivery_order_types) | **POST** /api/1/deliveries/order_types | Order types.
[**get_discounts**](DictionariesApi.md#get_discounts) | **POST** /api/1/discounts | Discounts / surcharges.
[**get_payment_types**](DictionariesApi.md#get_payment_types) | **POST** /api/1/payment_types | Payment types.
[**get_removal_types**](DictionariesApi.md#get_removal_types) | **POST** /api/1/removal_types | Removal types (reasons for deletion).
[**get_tips_types**](DictionariesApi.md#get_tips_types) | **POST** /api/1/tips_types | Get tips types for api-login&#x60;s rms group.


# **get_cancel_causes**
> CancelCausesResponse get_cancel_causes(timeout=timeout, cancel_causes_request=cancel_causes_request)

Delivery cancel causes.



 > Allowed from version `7.7.1`.

 > Restriction group: `Data: dictionaries`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.cancel_causes_request import CancelCausesRequest
from iikocloud_client.models.cancel_causes_response import CancelCausesResponse
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
    api_instance = iikocloud_client.DictionariesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    cancel_causes_request = iikocloud_client.CancelCausesRequest() # CancelCausesRequest |  (optional)

    try:
        # Delivery cancel causes.
        api_response = await api_instance.get_cancel_causes(timeout=timeout, cancel_causes_request=cancel_causes_request)
        print("The response of DictionariesApi->get_cancel_causes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->get_cancel_causes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **cancel_causes_request** | [**CancelCausesRequest**](CancelCausesRequest.md)|  | [optional] 

### Return type

[**CancelCausesResponse**](CancelCausesResponse.md)

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

# **get_delivery_order_types**
> OrderTypesResponse get_delivery_order_types(timeout=timeout, order_types_request=order_types_request)

Order types.



 > Restriction group: `Data: dictionaries`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.order_types_request import OrderTypesRequest
from iikocloud_client.models.order_types_response import OrderTypesResponse
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
    api_instance = iikocloud_client.DictionariesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    order_types_request = iikocloud_client.OrderTypesRequest() # OrderTypesRequest |  (optional)

    try:
        # Order types.
        api_response = await api_instance.get_delivery_order_types(timeout=timeout, order_types_request=order_types_request)
        print("The response of DictionariesApi->get_delivery_order_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->get_delivery_order_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **order_types_request** | [**OrderTypesRequest**](OrderTypesRequest.md)|  | [optional] 

### Return type

[**OrderTypesResponse**](OrderTypesResponse.md)

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

# **get_discounts**
> DiscountsResponse get_discounts(timeout=timeout, discounts_request=discounts_request)

Discounts / surcharges.



 > Restriction group: `Data: dictionaries`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.discounts_request import DiscountsRequest
from iikocloud_client.models.discounts_response import DiscountsResponse
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
    api_instance = iikocloud_client.DictionariesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    discounts_request = iikocloud_client.DiscountsRequest() # DiscountsRequest |  (optional)

    try:
        # Discounts / surcharges.
        api_response = await api_instance.get_discounts(timeout=timeout, discounts_request=discounts_request)
        print("The response of DictionariesApi->get_discounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->get_discounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **discounts_request** | [**DiscountsRequest**](DiscountsRequest.md)|  | [optional] 

### Return type

[**DiscountsResponse**](DiscountsResponse.md)

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

# **get_payment_types**
> PaymentTypesResponse get_payment_types(timeout=timeout, payment_types_request=payment_types_request)

Payment types.



 > Restriction group: `Data: dictionaries`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.payment_types_request import PaymentTypesRequest
from iikocloud_client.models.payment_types_response import PaymentTypesResponse
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
    api_instance = iikocloud_client.DictionariesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    payment_types_request = iikocloud_client.PaymentTypesRequest() # PaymentTypesRequest |  (optional)

    try:
        # Payment types.
        api_response = await api_instance.get_payment_types(timeout=timeout, payment_types_request=payment_types_request)
        print("The response of DictionariesApi->get_payment_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->get_payment_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **payment_types_request** | [**PaymentTypesRequest**](PaymentTypesRequest.md)|  | [optional] 

### Return type

[**PaymentTypesResponse**](PaymentTypesResponse.md)

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

# **get_removal_types**
> RemovalTypesResponse get_removal_types(timeout=timeout, removal_types_request=removal_types_request)

Removal types (reasons for deletion).



 > Allowed from version `7.5.3`.

 > Restriction group: `Data: dictionaries`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.removal_types_request import RemovalTypesRequest
from iikocloud_client.models.removal_types_response import RemovalTypesResponse
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
    api_instance = iikocloud_client.DictionariesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    removal_types_request = iikocloud_client.RemovalTypesRequest() # RemovalTypesRequest |  (optional)

    try:
        # Removal types (reasons for deletion).
        api_response = await api_instance.get_removal_types(timeout=timeout, removal_types_request=removal_types_request)
        print("The response of DictionariesApi->get_removal_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->get_removal_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **removal_types_request** | [**RemovalTypesRequest**](RemovalTypesRequest.md)|  | [optional] 

### Return type

[**RemovalTypesResponse**](RemovalTypesResponse.md)

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

# **get_tips_types**
> TipsTypesResponse get_tips_types(timeout=timeout)

Get tips types for api-login`s rms group.



 > Allowed from version `7.7.4`.

 > Restriction group: `Data: dictionaries`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.tips_types_response import TipsTypesResponse
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
    api_instance = iikocloud_client.DictionariesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)

    try:
        # Get tips types for api-login`s rms group.
        api_response = await api_instance.get_tips_types(timeout=timeout)
        print("The response of DictionariesApi->get_tips_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->get_tips_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]

### Return type

[**TipsTypesResponse**](TipsTypesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

