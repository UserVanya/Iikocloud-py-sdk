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
> IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse deliveries_by_delivery_date_and_phone_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_phone_request=iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_phone_request)

Retrieve list of orders by telephone number, dates and revision.



 > Restriction group: `Orders: receiving`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_phone_request import IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_orders_with_revision_response import IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse
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
    api_instance = iikocloud_client.DeliveriesRetrieveApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_phone_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest() # IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest |  (optional)

    try:
        # Retrieve list of orders by telephone number, dates and revision.
        api_response = await api_instance.deliveries_by_delivery_date_and_phone_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_phone_request=iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_phone_request)
        print("The response of DeliveriesRetrieveApi->deliveries_by_delivery_date_and_phone_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->deliveries_by_delivery_date_and_phone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_phone_request** | [**IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest**](IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndPhoneRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse**](IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse.md)

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

# **deliveries_by_delivery_date_and_source_key_and_filter_post**
> IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse deliveries_by_delivery_date_and_source_key_and_filter_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_filter_request=iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_filter_request)

Search orders by search text and additional filters (date, problem, statuses and other).



 > Restriction group: `Orders: receiving`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_filter_request import IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndFilterRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_orders_with_revision_response import IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse
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
    api_instance = iikocloud_client.DeliveriesRetrieveApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_filter_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndFilterRequest() # IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndFilterRequest |  (optional)

    try:
        # Search orders by search text and additional filters (date, problem, statuses and other).
        api_response = await api_instance.deliveries_by_delivery_date_and_source_key_and_filter_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_filter_request=iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_filter_request)
        print("The response of DeliveriesRetrieveApi->deliveries_by_delivery_date_and_source_key_and_filter_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->deliveries_by_delivery_date_and_source_key_and_filter_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_filter_request** | [**IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndFilterRequest**](IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndFilterRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse**](IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse.md)

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

# **deliveries_by_delivery_date_and_status_post**
> IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse deliveries_by_delivery_date_and_status_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_status_request=iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_status_request)

Retrieve list of orders by statuses and dates.



 > Restriction group: `Orders: receiving`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_status_request import IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndStatusRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_orders_with_revision_response import IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse
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
    api_instance = iikocloud_client.DeliveriesRetrieveApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_status_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndStatusRequest() # IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndStatusRequest |  (optional)

    try:
        # Retrieve list of orders by statuses and dates.
        api_response = await api_instance.deliveries_by_delivery_date_and_status_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_status_request=iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_status_request)
        print("The response of DeliveriesRetrieveApi->deliveries_by_delivery_date_and_status_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->deliveries_by_delivery_date_and_status_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_status_request** | [**IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndStatusRequest**](IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndStatusRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse**](IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse.md)

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

# **deliveries_by_id_post**
> IikoTransportPublicApiContractsDeliveriesResponseOrdersResponse deliveries_by_id_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_orders_by_id_request=iiko_transport_public_api_contracts_deliveries_request_orders_by_id_request)

Retrieve orders by IDs.



 > Restriction group: `Orders: receiving`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_orders_by_id_request import IikoTransportPublicApiContractsDeliveriesRequestOrdersByIdRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_orders_response import IikoTransportPublicApiContractsDeliveriesResponseOrdersResponse
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
    api_instance = iikocloud_client.DeliveriesRetrieveApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_orders_by_id_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestOrdersByIdRequest() # IikoTransportPublicApiContractsDeliveriesRequestOrdersByIdRequest |  (optional)

    try:
        # Retrieve orders by IDs.
        api_response = await api_instance.deliveries_by_id_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_orders_by_id_request=iiko_transport_public_api_contracts_deliveries_request_orders_by_id_request)
        print("The response of DeliveriesRetrieveApi->deliveries_by_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->deliveries_by_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_orders_by_id_request** | [**IikoTransportPublicApiContractsDeliveriesRequestOrdersByIdRequest**](IikoTransportPublicApiContractsDeliveriesRequestOrdersByIdRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsDeliveriesResponseOrdersResponse**](IikoTransportPublicApiContractsDeliveriesResponseOrdersResponse.md)

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

# **deliveries_by_revision_post**
> IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse deliveries_by_revision_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_orders_by_revision_request=iiko_transport_public_api_contracts_deliveries_request_orders_by_revision_request)

Retrieve list of orders changed from the time revision was passed.



 > Restriction group: `Orders: receiving by revision`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_orders_by_revision_request import IikoTransportPublicApiContractsDeliveriesRequestOrdersByRevisionRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_orders_with_revision_response import IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse
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
    api_instance = iikocloud_client.DeliveriesRetrieveApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_orders_by_revision_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestOrdersByRevisionRequest() # IikoTransportPublicApiContractsDeliveriesRequestOrdersByRevisionRequest |  (optional)

    try:
        # Retrieve list of orders changed from the time revision was passed.
        api_response = await api_instance.deliveries_by_revision_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_orders_by_revision_request=iiko_transport_public_api_contracts_deliveries_request_orders_by_revision_request)
        print("The response of DeliveriesRetrieveApi->deliveries_by_revision_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->deliveries_by_revision_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_orders_by_revision_request** | [**IikoTransportPublicApiContractsDeliveriesRequestOrdersByRevisionRequest**](IikoTransportPublicApiContractsDeliveriesRequestOrdersByRevisionRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse**](IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse.md)

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

# **deliveries_history_by_delivery_date_and_phone_post**
> IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse deliveries_history_by_delivery_date_and_phone_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_orders_history_by_delivery_date_and_phone_request=iiko_transport_public_api_contracts_deliveries_request_orders_history_by_delivery_date_and_phone_request)

Retrieve list of history orders by telephone number, dates and revision.



 > Restriction group: `Orders: receiving`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_orders_history_by_delivery_date_and_phone_request import IikoTransportPublicApiContractsDeliveriesRequestOrdersHistoryByDeliveryDateAndPhoneRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_orders_with_revision_response import IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse
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
    api_instance = iikocloud_client.DeliveriesRetrieveApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_orders_history_by_delivery_date_and_phone_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestOrdersHistoryByDeliveryDateAndPhoneRequest() # IikoTransportPublicApiContractsDeliveriesRequestOrdersHistoryByDeliveryDateAndPhoneRequest |  (optional)

    try:
        # Retrieve list of history orders by telephone number, dates and revision.
        api_response = await api_instance.deliveries_history_by_delivery_date_and_phone_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_orders_history_by_delivery_date_and_phone_request=iiko_transport_public_api_contracts_deliveries_request_orders_history_by_delivery_date_and_phone_request)
        print("The response of DeliveriesRetrieveApi->deliveries_history_by_delivery_date_and_phone_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->deliveries_history_by_delivery_date_and_phone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_orders_history_by_delivery_date_and_phone_request** | [**IikoTransportPublicApiContractsDeliveriesRequestOrdersHistoryByDeliveryDateAndPhoneRequest**](IikoTransportPublicApiContractsDeliveriesRequestOrdersHistoryByDeliveryDateAndPhoneRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse**](IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse.md)

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

