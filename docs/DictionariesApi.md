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
> IikoTransportPublicApiContractsCancelCausesCancelCausesResponse cancel_causes_post(timeout=timeout, iiko_transport_public_api_contracts_cancel_causes_cancel_causes_request=iiko_transport_public_api_contracts_cancel_causes_cancel_causes_request)

Delivery cancel causes.



 > Allowed from version `7.7.1`.

 > Restriction group: `Data: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_cancel_causes_cancel_causes_request import IikoTransportPublicApiContractsCancelCausesCancelCausesRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_cancel_causes_cancel_causes_response import IikoTransportPublicApiContractsCancelCausesCancelCausesResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DictionariesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_cancel_causes_cancel_causes_request = iikocloud_client.IikoTransportPublicApiContractsCancelCausesCancelCausesRequest() # IikoTransportPublicApiContractsCancelCausesCancelCausesRequest |  (optional)

    try:
        # Delivery cancel causes.
        api_response = await api_instance.cancel_causes_post(timeout=timeout, iiko_transport_public_api_contracts_cancel_causes_cancel_causes_request=iiko_transport_public_api_contracts_cancel_causes_cancel_causes_request)
        print("The response of DictionariesApi->cancel_causes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->cancel_causes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_cancel_causes_cancel_causes_request** | [**IikoTransportPublicApiContractsCancelCausesCancelCausesRequest**](IikoTransportPublicApiContractsCancelCausesCancelCausesRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCancelCausesCancelCausesResponse**](IikoTransportPublicApiContractsCancelCausesCancelCausesResponse.md)

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

# **deliveries_order_types_post**
> IikoTransportPublicApiContractsOrderTypesOrderTypesResponse deliveries_order_types_post(timeout=timeout, iiko_transport_public_api_contracts_order_types_order_types_request=iiko_transport_public_api_contracts_order_types_order_types_request)

Order types.



 > Restriction group: `Data: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_order_types_order_types_request import IikoTransportPublicApiContractsOrderTypesOrderTypesRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_order_types_order_types_response import IikoTransportPublicApiContractsOrderTypesOrderTypesResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DictionariesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_order_types_order_types_request = iikocloud_client.IikoTransportPublicApiContractsOrderTypesOrderTypesRequest() # IikoTransportPublicApiContractsOrderTypesOrderTypesRequest |  (optional)

    try:
        # Order types.
        api_response = await api_instance.deliveries_order_types_post(timeout=timeout, iiko_transport_public_api_contracts_order_types_order_types_request=iiko_transport_public_api_contracts_order_types_order_types_request)
        print("The response of DictionariesApi->deliveries_order_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->deliveries_order_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_order_types_order_types_request** | [**IikoTransportPublicApiContractsOrderTypesOrderTypesRequest**](IikoTransportPublicApiContractsOrderTypesOrderTypesRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsOrderTypesOrderTypesResponse**](IikoTransportPublicApiContractsOrderTypesOrderTypesResponse.md)

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

# **discounts_post**
> IikoTransportPublicApiContractsDiscountsDiscountsResponse discounts_post(timeout=timeout, iiko_transport_public_api_contracts_discounts_discounts_request=iiko_transport_public_api_contracts_discounts_discounts_request)

Discounts / surcharges.



 > Restriction group: `Data: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_discounts_discounts_request import IikoTransportPublicApiContractsDiscountsDiscountsRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_discounts_discounts_response import IikoTransportPublicApiContractsDiscountsDiscountsResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DictionariesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_discounts_discounts_request = iikocloud_client.IikoTransportPublicApiContractsDiscountsDiscountsRequest() # IikoTransportPublicApiContractsDiscountsDiscountsRequest |  (optional)

    try:
        # Discounts / surcharges.
        api_response = await api_instance.discounts_post(timeout=timeout, iiko_transport_public_api_contracts_discounts_discounts_request=iiko_transport_public_api_contracts_discounts_discounts_request)
        print("The response of DictionariesApi->discounts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->discounts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_discounts_discounts_request** | [**IikoTransportPublicApiContractsDiscountsDiscountsRequest**](IikoTransportPublicApiContractsDiscountsDiscountsRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsDiscountsDiscountsResponse**](IikoTransportPublicApiContractsDiscountsDiscountsResponse.md)

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

# **payment_types_post**
> IikoTransportPublicApiContractsPaymentTypesPaymentTypesResponse payment_types_post(timeout=timeout, iiko_transport_public_api_contracts_payment_types_payment_types_request=iiko_transport_public_api_contracts_payment_types_payment_types_request)

Payment types.



 > Restriction group: `Data: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_payment_types_payment_types_request import IikoTransportPublicApiContractsPaymentTypesPaymentTypesRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_payment_types_payment_types_response import IikoTransportPublicApiContractsPaymentTypesPaymentTypesResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DictionariesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_payment_types_payment_types_request = iikocloud_client.IikoTransportPublicApiContractsPaymentTypesPaymentTypesRequest() # IikoTransportPublicApiContractsPaymentTypesPaymentTypesRequest |  (optional)

    try:
        # Payment types.
        api_response = await api_instance.payment_types_post(timeout=timeout, iiko_transport_public_api_contracts_payment_types_payment_types_request=iiko_transport_public_api_contracts_payment_types_payment_types_request)
        print("The response of DictionariesApi->payment_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->payment_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_payment_types_payment_types_request** | [**IikoTransportPublicApiContractsPaymentTypesPaymentTypesRequest**](IikoTransportPublicApiContractsPaymentTypesPaymentTypesRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsPaymentTypesPaymentTypesResponse**](IikoTransportPublicApiContractsPaymentTypesPaymentTypesResponse.md)

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

# **removal_types_post**
> IikoTransportPublicApiContractsRemovalTypesRemovalTypesResponse removal_types_post(timeout=timeout, iiko_transport_public_api_contracts_removal_types_removal_types_request=iiko_transport_public_api_contracts_removal_types_removal_types_request)

Removal types (reasons for deletion).



 > Allowed from version `7.5.3`.

 > Restriction group: `Data: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_removal_types_removal_types_request import IikoTransportPublicApiContractsRemovalTypesRemovalTypesRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_removal_types_removal_types_response import IikoTransportPublicApiContractsRemovalTypesRemovalTypesResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DictionariesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_removal_types_removal_types_request = iikocloud_client.IikoTransportPublicApiContractsRemovalTypesRemovalTypesRequest() # IikoTransportPublicApiContractsRemovalTypesRemovalTypesRequest |  (optional)

    try:
        # Removal types (reasons for deletion).
        api_response = await api_instance.removal_types_post(timeout=timeout, iiko_transport_public_api_contracts_removal_types_removal_types_request=iiko_transport_public_api_contracts_removal_types_removal_types_request)
        print("The response of DictionariesApi->removal_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DictionariesApi->removal_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_removal_types_removal_types_request** | [**IikoTransportPublicApiContractsRemovalTypesRemovalTypesRequest**](IikoTransportPublicApiContractsRemovalTypesRemovalTypesRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsRemovalTypesRemovalTypesResponse**](IikoTransportPublicApiContractsRemovalTypesRemovalTypesResponse.md)

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

# **tips_types_post**
> IikoTransportPublicApiContractsTipsTypesTipsTypesResponse tips_types_post(timeout=timeout)

Get tips types for api-login`s rms group.



 > Allowed from version `7.7.4`.

 > Restriction group: `Data: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_tips_types_tips_types_response import IikoTransportPublicApiContractsTipsTypesTipsTypesResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
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

[**IikoTransportPublicApiContractsTipsTypesTipsTypesResponse**](IikoTransportPublicApiContractsTipsTypesTipsTypesResponse.md)

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

