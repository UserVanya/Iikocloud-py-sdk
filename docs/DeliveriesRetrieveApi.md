# iikocloud_client.DeliveriesRetrieveApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deliveries_by_delivery_date_and_phone_post**](DeliveriesRetrieveApi.md#deliveries_by_delivery_date_and_phone_post) | **POST** /deliveries/by_delivery_date_and_phone | Retrieve list of orders by telephone number, dates and revision.
[**deliveries_by_delivery_date_and_source_key_and_filter_post**](DeliveriesRetrieveApi.md#deliveries_by_delivery_date_and_source_key_and_filter_post) | **POST** /deliveries/by_delivery_date_and_source_key_and_filter | Search orders by search text and additional filters (date, problem, statuses and other).
[**deliveries_by_delivery_date_and_status_post**](DeliveriesRetrieveApi.md#deliveries_by_delivery_date_and_status_post) | **POST** /deliveries/by_delivery_date_and_status | Retrieve list of orders by statuses and dates.
[**deliveries_by_id_post**](DeliveriesRetrieveApi.md#deliveries_by_id_post) | **POST** /deliveries/by_id | Retrieve orders by IDs.
[**deliveries_by_revision_post**](DeliveriesRetrieveApi.md#deliveries_by_revision_post) | **POST** /deliveries/by_revision | Retrieve list of orders changed from the time revision was passed.
[**deliveries_history_by_delivery_date_and_phone_post**](DeliveriesRetrieveApi.md#deliveries_history_by_delivery_date_and_phone_post) | **POST** /deliveries/history/by_delivery_date_and_phone | Retrieve list of history orders by telephone number, dates and revision.


# **deliveries_by_delivery_date_and_phone_post**
> TransportDeliveriesResponseOrdersWithRevisionResponse deliveries_by_delivery_date_and_phone_post(timeout=timeout, transport_deliveries_request_orders_by_delivery_date_and_phone_request=transport_deliveries_request_orders_by_delivery_date_and_phone_request)

Retrieve list of orders by telephone number, dates and revision.



 > Restriction group: `Orders: receiving`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_deliveries_request_orders_by_delivery_date_and_phone_request import TransportDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest
from iikocloud_client.models.transport_deliveries_response_orders_with_revision_response import TransportDeliveriesResponseOrdersWithRevisionResponse
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
    api_instance = iikocloud_client.DeliveriesRetrieveApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_orders_by_delivery_date_and_phone_request = iikocloud_client.TransportDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest() # TransportDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest |  (optional)

    try:
        # Retrieve list of orders by telephone number, dates and revision.
        api_response = await api_instance.deliveries_by_delivery_date_and_phone_post(timeout=timeout, transport_deliveries_request_orders_by_delivery_date_and_phone_request=transport_deliveries_request_orders_by_delivery_date_and_phone_request)
        print("The response of DeliveriesRetrieveApi->deliveries_by_delivery_date_and_phone_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->deliveries_by_delivery_date_and_phone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_orders_by_delivery_date_and_phone_request** | [**TransportDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest**](TransportDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest.md)|  | [optional] 

### Return type

[**TransportDeliveriesResponseOrdersWithRevisionResponse**](TransportDeliveriesResponseOrdersWithRevisionResponse.md)

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

# **deliveries_by_delivery_date_and_source_key_and_filter_post**
> TransportDeliveriesResponseOrdersWithRevisionResponse deliveries_by_delivery_date_and_source_key_and_filter_post(timeout=timeout, transport_deliveries_request_orders_by_delivery_date_and_filter_request=transport_deliveries_request_orders_by_delivery_date_and_filter_request)

Search orders by search text and additional filters (date, problem, statuses and other).



 > Restriction group: `Orders: receiving`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_deliveries_request_orders_by_delivery_date_and_filter_request import TransportDeliveriesRequestOrdersByDeliveryDateAndFilterRequest
from iikocloud_client.models.transport_deliveries_response_orders_with_revision_response import TransportDeliveriesResponseOrdersWithRevisionResponse
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
    api_instance = iikocloud_client.DeliveriesRetrieveApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_orders_by_delivery_date_and_filter_request = iikocloud_client.TransportDeliveriesRequestOrdersByDeliveryDateAndFilterRequest() # TransportDeliveriesRequestOrdersByDeliveryDateAndFilterRequest |  (optional)

    try:
        # Search orders by search text and additional filters (date, problem, statuses and other).
        api_response = await api_instance.deliveries_by_delivery_date_and_source_key_and_filter_post(timeout=timeout, transport_deliveries_request_orders_by_delivery_date_and_filter_request=transport_deliveries_request_orders_by_delivery_date_and_filter_request)
        print("The response of DeliveriesRetrieveApi->deliveries_by_delivery_date_and_source_key_and_filter_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->deliveries_by_delivery_date_and_source_key_and_filter_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_orders_by_delivery_date_and_filter_request** | [**TransportDeliveriesRequestOrdersByDeliveryDateAndFilterRequest**](TransportDeliveriesRequestOrdersByDeliveryDateAndFilterRequest.md)|  | [optional] 

### Return type

[**TransportDeliveriesResponseOrdersWithRevisionResponse**](TransportDeliveriesResponseOrdersWithRevisionResponse.md)

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

# **deliveries_by_delivery_date_and_status_post**
> TransportDeliveriesResponseOrdersWithRevisionResponse deliveries_by_delivery_date_and_status_post(timeout=timeout, transport_deliveries_request_orders_by_delivery_date_and_status_request=transport_deliveries_request_orders_by_delivery_date_and_status_request)

Retrieve list of orders by statuses and dates.



 > Restriction group: `Orders: receiving`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_deliveries_request_orders_by_delivery_date_and_status_request import TransportDeliveriesRequestOrdersByDeliveryDateAndStatusRequest
from iikocloud_client.models.transport_deliveries_response_orders_with_revision_response import TransportDeliveriesResponseOrdersWithRevisionResponse
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
    api_instance = iikocloud_client.DeliveriesRetrieveApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_orders_by_delivery_date_and_status_request = iikocloud_client.TransportDeliveriesRequestOrdersByDeliveryDateAndStatusRequest() # TransportDeliveriesRequestOrdersByDeliveryDateAndStatusRequest |  (optional)

    try:
        # Retrieve list of orders by statuses and dates.
        api_response = await api_instance.deliveries_by_delivery_date_and_status_post(timeout=timeout, transport_deliveries_request_orders_by_delivery_date_and_status_request=transport_deliveries_request_orders_by_delivery_date_and_status_request)
        print("The response of DeliveriesRetrieveApi->deliveries_by_delivery_date_and_status_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->deliveries_by_delivery_date_and_status_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_orders_by_delivery_date_and_status_request** | [**TransportDeliveriesRequestOrdersByDeliveryDateAndStatusRequest**](TransportDeliveriesRequestOrdersByDeliveryDateAndStatusRequest.md)|  | [optional] 

### Return type

[**TransportDeliveriesResponseOrdersWithRevisionResponse**](TransportDeliveriesResponseOrdersWithRevisionResponse.md)

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

# **deliveries_by_id_post**
> TransportDeliveriesResponseOrdersResponse deliveries_by_id_post(timeout=timeout, transport_deliveries_request_orders_by_id_request=transport_deliveries_request_orders_by_id_request)

Retrieve orders by IDs.



 > Restriction group: `Orders: receiving`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_deliveries_request_orders_by_id_request import TransportDeliveriesRequestOrdersByIdRequest
from iikocloud_client.models.transport_deliveries_response_orders_response import TransportDeliveriesResponseOrdersResponse
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
    api_instance = iikocloud_client.DeliveriesRetrieveApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_orders_by_id_request = iikocloud_client.TransportDeliveriesRequestOrdersByIdRequest() # TransportDeliveriesRequestOrdersByIdRequest |  (optional)

    try:
        # Retrieve orders by IDs.
        api_response = await api_instance.deliveries_by_id_post(timeout=timeout, transport_deliveries_request_orders_by_id_request=transport_deliveries_request_orders_by_id_request)
        print("The response of DeliveriesRetrieveApi->deliveries_by_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->deliveries_by_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_orders_by_id_request** | [**TransportDeliveriesRequestOrdersByIdRequest**](TransportDeliveriesRequestOrdersByIdRequest.md)|  | [optional] 

### Return type

[**TransportDeliveriesResponseOrdersResponse**](TransportDeliveriesResponseOrdersResponse.md)

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

# **deliveries_by_revision_post**
> TransportDeliveriesResponseOrdersWithRevisionResponse deliveries_by_revision_post(timeout=timeout, transport_deliveries_request_orders_by_revision_request=transport_deliveries_request_orders_by_revision_request)

Retrieve list of orders changed from the time revision was passed.



 > Restriction group: `Orders: receiving by revision`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_deliveries_request_orders_by_revision_request import TransportDeliveriesRequestOrdersByRevisionRequest
from iikocloud_client.models.transport_deliveries_response_orders_with_revision_response import TransportDeliveriesResponseOrdersWithRevisionResponse
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
    api_instance = iikocloud_client.DeliveriesRetrieveApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_orders_by_revision_request = iikocloud_client.TransportDeliveriesRequestOrdersByRevisionRequest() # TransportDeliveriesRequestOrdersByRevisionRequest |  (optional)

    try:
        # Retrieve list of orders changed from the time revision was passed.
        api_response = await api_instance.deliveries_by_revision_post(timeout=timeout, transport_deliveries_request_orders_by_revision_request=transport_deliveries_request_orders_by_revision_request)
        print("The response of DeliveriesRetrieveApi->deliveries_by_revision_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->deliveries_by_revision_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_orders_by_revision_request** | [**TransportDeliveriesRequestOrdersByRevisionRequest**](TransportDeliveriesRequestOrdersByRevisionRequest.md)|  | [optional] 

### Return type

[**TransportDeliveriesResponseOrdersWithRevisionResponse**](TransportDeliveriesResponseOrdersWithRevisionResponse.md)

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

# **deliveries_history_by_delivery_date_and_phone_post**
> TransportDeliveriesResponseOrdersWithRevisionResponse deliveries_history_by_delivery_date_and_phone_post(timeout=timeout, transport_deliveries_request_orders_history_by_delivery_date_and_phone_request=transport_deliveries_request_orders_history_by_delivery_date_and_phone_request)

Retrieve list of history orders by telephone number, dates and revision.



 > Restriction group: `Orders: receiving`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_deliveries_request_orders_history_by_delivery_date_and_phone_request import TransportDeliveriesRequestOrdersHistoryByDeliveryDateAndPhoneRequest
from iikocloud_client.models.transport_deliveries_response_orders_with_revision_response import TransportDeliveriesResponseOrdersWithRevisionResponse
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
    api_instance = iikocloud_client.DeliveriesRetrieveApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_orders_history_by_delivery_date_and_phone_request = iikocloud_client.TransportDeliveriesRequestOrdersHistoryByDeliveryDateAndPhoneRequest() # TransportDeliveriesRequestOrdersHistoryByDeliveryDateAndPhoneRequest |  (optional)

    try:
        # Retrieve list of history orders by telephone number, dates and revision.
        api_response = await api_instance.deliveries_history_by_delivery_date_and_phone_post(timeout=timeout, transport_deliveries_request_orders_history_by_delivery_date_and_phone_request=transport_deliveries_request_orders_history_by_delivery_date_and_phone_request)
        print("The response of DeliveriesRetrieveApi->deliveries_history_by_delivery_date_and_phone_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->deliveries_history_by_delivery_date_and_phone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_orders_history_by_delivery_date_and_phone_request** | [**TransportDeliveriesRequestOrdersHistoryByDeliveryDateAndPhoneRequest**](TransportDeliveriesRequestOrdersHistoryByDeliveryDateAndPhoneRequest.md)|  | [optional] 

### Return type

[**TransportDeliveriesResponseOrdersWithRevisionResponse**](TransportDeliveriesResponseOrdersWithRevisionResponse.md)

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

