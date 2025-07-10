# iiko_cloud_client.DeliveriesRetrieveApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_deliveries_by_delivery_date_and_phone_post**](DeliveriesRetrieveApi.md#api1_deliveries_by_delivery_date_and_phone_post) | **POST** /api/1/deliveries/by_delivery_date_and_phone | Retrieve list of orders by telephone number, dates and revision.
[**api1_deliveries_by_delivery_date_and_source_key_and_filter_post**](DeliveriesRetrieveApi.md#api1_deliveries_by_delivery_date_and_source_key_and_filter_post) | **POST** /api/1/deliveries/by_delivery_date_and_source_key_and_filter | Search orders by search text and additional filters (date, problem, statuses and other).
[**api1_deliveries_by_delivery_date_and_status_post**](DeliveriesRetrieveApi.md#api1_deliveries_by_delivery_date_and_status_post) | **POST** /api/1/deliveries/by_delivery_date_and_status | Retrieve list of orders by statuses and dates.
[**api1_deliveries_by_id_post**](DeliveriesRetrieveApi.md#api1_deliveries_by_id_post) | **POST** /api/1/deliveries/by_id | Retrieve orders by IDs.
[**api1_deliveries_by_revision_post**](DeliveriesRetrieveApi.md#api1_deliveries_by_revision_post) | **POST** /api/1/deliveries/by_revision | Retrieve list of orders changed from the time revision was passed.
[**api1_deliveries_history_by_delivery_date_and_phone_post**](DeliveriesRetrieveApi.md#api1_deliveries_history_by_delivery_date_and_phone_post) | **POST** /api/1/deliveries/history/by_delivery_date_and_phone | Retrieve list of history orders by telephone number, dates and revision.


# **api1_deliveries_by_delivery_date_and_phone_post**
> TransportDeliveriesResponseOrdersWithRevisionResponse api1_deliveries_by_delivery_date_and_phone_post(authorization, timeout=timeout, transport_deliveries_request_orders_by_delivery_date_and_phone_request=transport_deliveries_request_orders_by_delivery_date_and_phone_request)

Retrieve list of orders by telephone number, dates and revision.



 > Restriction group: `Orders: receiving`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_deliveries_request_orders_by_delivery_date_and_phone_request import TransportDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest
from iiko_cloud_client.models.transport_deliveries_response_orders_with_revision_response import TransportDeliveriesResponseOrdersWithRevisionResponse
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
    api_instance = iiko_cloud_client.DeliveriesRetrieveApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_orders_by_delivery_date_and_phone_request = iiko_cloud_client.TransportDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest() # TransportDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest |  (optional)

    try:
        # Retrieve list of orders by telephone number, dates and revision.
        api_response = await api_instance.api1_deliveries_by_delivery_date_and_phone_post(authorization, timeout=timeout, transport_deliveries_request_orders_by_delivery_date_and_phone_request=transport_deliveries_request_orders_by_delivery_date_and_phone_request)
        print("The response of DeliveriesRetrieveApi->api1_deliveries_by_delivery_date_and_phone_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->api1_deliveries_by_delivery_date_and_phone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_orders_by_delivery_date_and_phone_request** | [**TransportDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest**](TransportDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest.md)|  | [optional] 

### Return type

[**TransportDeliveriesResponseOrdersWithRevisionResponse**](TransportDeliveriesResponseOrdersWithRevisionResponse.md)

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

# **api1_deliveries_by_delivery_date_and_source_key_and_filter_post**
> TransportDeliveriesResponseOrdersWithRevisionResponse api1_deliveries_by_delivery_date_and_source_key_and_filter_post(authorization, timeout=timeout, transport_deliveries_request_orders_by_delivery_date_and_filter_request=transport_deliveries_request_orders_by_delivery_date_and_filter_request)

Search orders by search text and additional filters (date, problem, statuses and other).



 > Restriction group: `Orders: receiving`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_deliveries_request_orders_by_delivery_date_and_filter_request import TransportDeliveriesRequestOrdersByDeliveryDateAndFilterRequest
from iiko_cloud_client.models.transport_deliveries_response_orders_with_revision_response import TransportDeliveriesResponseOrdersWithRevisionResponse
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
    api_instance = iiko_cloud_client.DeliveriesRetrieveApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_orders_by_delivery_date_and_filter_request = iiko_cloud_client.TransportDeliveriesRequestOrdersByDeliveryDateAndFilterRequest() # TransportDeliveriesRequestOrdersByDeliveryDateAndFilterRequest |  (optional)

    try:
        # Search orders by search text and additional filters (date, problem, statuses and other).
        api_response = await api_instance.api1_deliveries_by_delivery_date_and_source_key_and_filter_post(authorization, timeout=timeout, transport_deliveries_request_orders_by_delivery_date_and_filter_request=transport_deliveries_request_orders_by_delivery_date_and_filter_request)
        print("The response of DeliveriesRetrieveApi->api1_deliveries_by_delivery_date_and_source_key_and_filter_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->api1_deliveries_by_delivery_date_and_source_key_and_filter_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_orders_by_delivery_date_and_filter_request** | [**TransportDeliveriesRequestOrdersByDeliveryDateAndFilterRequest**](TransportDeliveriesRequestOrdersByDeliveryDateAndFilterRequest.md)|  | [optional] 

### Return type

[**TransportDeliveriesResponseOrdersWithRevisionResponse**](TransportDeliveriesResponseOrdersWithRevisionResponse.md)

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

# **api1_deliveries_by_delivery_date_and_status_post**
> TransportDeliveriesResponseOrdersWithRevisionResponse api1_deliveries_by_delivery_date_and_status_post(authorization, timeout=timeout, transport_deliveries_request_orders_by_delivery_date_and_status_request=transport_deliveries_request_orders_by_delivery_date_and_status_request)

Retrieve list of orders by statuses and dates.



 > Restriction group: `Orders: receiving`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_deliveries_request_orders_by_delivery_date_and_status_request import TransportDeliveriesRequestOrdersByDeliveryDateAndStatusRequest
from iiko_cloud_client.models.transport_deliveries_response_orders_with_revision_response import TransportDeliveriesResponseOrdersWithRevisionResponse
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
    api_instance = iiko_cloud_client.DeliveriesRetrieveApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_orders_by_delivery_date_and_status_request = iiko_cloud_client.TransportDeliveriesRequestOrdersByDeliveryDateAndStatusRequest() # TransportDeliveriesRequestOrdersByDeliveryDateAndStatusRequest |  (optional)

    try:
        # Retrieve list of orders by statuses and dates.
        api_response = await api_instance.api1_deliveries_by_delivery_date_and_status_post(authorization, timeout=timeout, transport_deliveries_request_orders_by_delivery_date_and_status_request=transport_deliveries_request_orders_by_delivery_date_and_status_request)
        print("The response of DeliveriesRetrieveApi->api1_deliveries_by_delivery_date_and_status_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->api1_deliveries_by_delivery_date_and_status_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_orders_by_delivery_date_and_status_request** | [**TransportDeliveriesRequestOrdersByDeliveryDateAndStatusRequest**](TransportDeliveriesRequestOrdersByDeliveryDateAndStatusRequest.md)|  | [optional] 

### Return type

[**TransportDeliveriesResponseOrdersWithRevisionResponse**](TransportDeliveriesResponseOrdersWithRevisionResponse.md)

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

# **api1_deliveries_by_id_post**
> TransportDeliveriesResponseOrdersResponse api1_deliveries_by_id_post(authorization, timeout=timeout, transport_deliveries_request_orders_by_id_request=transport_deliveries_request_orders_by_id_request)

Retrieve orders by IDs.



 > Restriction group: `Orders: receiving`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_deliveries_request_orders_by_id_request import TransportDeliveriesRequestOrdersByIdRequest
from iiko_cloud_client.models.transport_deliveries_response_orders_response import TransportDeliveriesResponseOrdersResponse
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
    api_instance = iiko_cloud_client.DeliveriesRetrieveApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_orders_by_id_request = iiko_cloud_client.TransportDeliveriesRequestOrdersByIdRequest() # TransportDeliveriesRequestOrdersByIdRequest |  (optional)

    try:
        # Retrieve orders by IDs.
        api_response = await api_instance.api1_deliveries_by_id_post(authorization, timeout=timeout, transport_deliveries_request_orders_by_id_request=transport_deliveries_request_orders_by_id_request)
        print("The response of DeliveriesRetrieveApi->api1_deliveries_by_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->api1_deliveries_by_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_orders_by_id_request** | [**TransportDeliveriesRequestOrdersByIdRequest**](TransportDeliveriesRequestOrdersByIdRequest.md)|  | [optional] 

### Return type

[**TransportDeliveriesResponseOrdersResponse**](TransportDeliveriesResponseOrdersResponse.md)

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

# **api1_deliveries_by_revision_post**
> TransportDeliveriesResponseOrdersWithRevisionResponse api1_deliveries_by_revision_post(authorization, timeout=timeout, transport_deliveries_request_orders_by_revision_request=transport_deliveries_request_orders_by_revision_request)

Retrieve list of orders changed from the time revision was passed.



 > Restriction group: `Orders: receiving by revision`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_deliveries_request_orders_by_revision_request import TransportDeliveriesRequestOrdersByRevisionRequest
from iiko_cloud_client.models.transport_deliveries_response_orders_with_revision_response import TransportDeliveriesResponseOrdersWithRevisionResponse
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
    api_instance = iiko_cloud_client.DeliveriesRetrieveApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_orders_by_revision_request = iiko_cloud_client.TransportDeliveriesRequestOrdersByRevisionRequest() # TransportDeliveriesRequestOrdersByRevisionRequest |  (optional)

    try:
        # Retrieve list of orders changed from the time revision was passed.
        api_response = await api_instance.api1_deliveries_by_revision_post(authorization, timeout=timeout, transport_deliveries_request_orders_by_revision_request=transport_deliveries_request_orders_by_revision_request)
        print("The response of DeliveriesRetrieveApi->api1_deliveries_by_revision_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->api1_deliveries_by_revision_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_orders_by_revision_request** | [**TransportDeliveriesRequestOrdersByRevisionRequest**](TransportDeliveriesRequestOrdersByRevisionRequest.md)|  | [optional] 

### Return type

[**TransportDeliveriesResponseOrdersWithRevisionResponse**](TransportDeliveriesResponseOrdersWithRevisionResponse.md)

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

# **api1_deliveries_history_by_delivery_date_and_phone_post**
> TransportDeliveriesResponseOrdersWithRevisionResponse api1_deliveries_history_by_delivery_date_and_phone_post(authorization, timeout=timeout, transport_deliveries_request_orders_history_by_delivery_date_and_phone_request=transport_deliveries_request_orders_history_by_delivery_date_and_phone_request)

Retrieve list of history orders by telephone number, dates and revision.



 > Restriction group: `Orders: receiving`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_deliveries_request_orders_history_by_delivery_date_and_phone_request import TransportDeliveriesRequestOrdersHistoryByDeliveryDateAndPhoneRequest
from iiko_cloud_client.models.transport_deliveries_response_orders_with_revision_response import TransportDeliveriesResponseOrdersWithRevisionResponse
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
    api_instance = iiko_cloud_client.DeliveriesRetrieveApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_orders_history_by_delivery_date_and_phone_request = iiko_cloud_client.TransportDeliveriesRequestOrdersHistoryByDeliveryDateAndPhoneRequest() # TransportDeliveriesRequestOrdersHistoryByDeliveryDateAndPhoneRequest |  (optional)

    try:
        # Retrieve list of history orders by telephone number, dates and revision.
        api_response = await api_instance.api1_deliveries_history_by_delivery_date_and_phone_post(authorization, timeout=timeout, transport_deliveries_request_orders_history_by_delivery_date_and_phone_request=transport_deliveries_request_orders_history_by_delivery_date_and_phone_request)
        print("The response of DeliveriesRetrieveApi->api1_deliveries_history_by_delivery_date_and_phone_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->api1_deliveries_history_by_delivery_date_and_phone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_orders_history_by_delivery_date_and_phone_request** | [**TransportDeliveriesRequestOrdersHistoryByDeliveryDateAndPhoneRequest**](TransportDeliveriesRequestOrdersHistoryByDeliveryDateAndPhoneRequest.md)|  | [optional] 

### Return type

[**TransportDeliveriesResponseOrdersWithRevisionResponse**](TransportDeliveriesResponseOrdersWithRevisionResponse.md)

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

