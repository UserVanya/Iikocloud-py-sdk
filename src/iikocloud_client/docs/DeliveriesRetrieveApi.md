# iikocloud_client.DeliveriesRetrieveApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_deliveries_by_delivery_date_and_phone**](DeliveriesRetrieveApi.md#get_deliveries_by_delivery_date_and_phone) | **POST** /api/1/deliveries/by_delivery_date_and_phone | Retrieve list of orders by telephone number, dates and revision.
[**get_deliveries_by_delivery_date_and_status**](DeliveriesRetrieveApi.md#get_deliveries_by_delivery_date_and_status) | **POST** /api/1/deliveries/by_delivery_date_and_status | Retrieve list of orders by statuses and dates.
[**get_deliveries_by_id**](DeliveriesRetrieveApi.md#get_deliveries_by_id) | **POST** /api/1/deliveries/by_id | Retrieve orders by IDs.
[**get_deliveries_by_revision**](DeliveriesRetrieveApi.md#get_deliveries_by_revision) | **POST** /api/1/deliveries/by_revision | Retrieve list of orders changed from the time revision was passed.
[**get_delivery_history_by_delivery_date_and_phone**](DeliveriesRetrieveApi.md#get_delivery_history_by_delivery_date_and_phone) | **POST** /api/1/deliveries/history/by_delivery_date_and_phone | Retrieve list of history orders by telephone number, dates and revision.
[**search_deliveries**](DeliveriesRetrieveApi.md#search_deliveries) | **POST** /api/1/deliveries/by_delivery_date_and_source_key_and_filter | Search orders by search text and additional filters (date, problem, statuses and other).


# **get_deliveries_by_delivery_date_and_phone**
> OrdersWithRevisionResponse get_deliveries_by_delivery_date_and_phone(timeout=timeout, orders_by_delivery_date_and_phone_request=orders_by_delivery_date_and_phone_request)

Retrieve list of orders by telephone number, dates and revision.



 > Restriction group: `Orders: receiving`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.orders_by_delivery_date_and_phone_request import OrdersByDeliveryDateAndPhoneRequest
from iikocloud_client.models.orders_with_revision_response import OrdersWithRevisionResponse
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
    api_instance = iikocloud_client.DeliveriesRetrieveApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    orders_by_delivery_date_and_phone_request = iikocloud_client.OrdersByDeliveryDateAndPhoneRequest() # OrdersByDeliveryDateAndPhoneRequest |  (optional)

    try:
        # Retrieve list of orders by telephone number, dates and revision.
        api_response = await api_instance.get_deliveries_by_delivery_date_and_phone(timeout=timeout, orders_by_delivery_date_and_phone_request=orders_by_delivery_date_and_phone_request)
        print("The response of DeliveriesRetrieveApi->get_deliveries_by_delivery_date_and_phone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->get_deliveries_by_delivery_date_and_phone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **orders_by_delivery_date_and_phone_request** | [**OrdersByDeliveryDateAndPhoneRequest**](OrdersByDeliveryDateAndPhoneRequest.md)|  | [optional] 

### Return type

[**OrdersWithRevisionResponse**](OrdersWithRevisionResponse.md)

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

# **get_deliveries_by_delivery_date_and_status**
> OrdersWithRevisionResponse get_deliveries_by_delivery_date_and_status(timeout=timeout, orders_by_delivery_date_and_status_request=orders_by_delivery_date_and_status_request)

Retrieve list of orders by statuses and dates.



 > Restriction group: `Orders: receiving`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.orders_by_delivery_date_and_status_request import OrdersByDeliveryDateAndStatusRequest
from iikocloud_client.models.orders_with_revision_response import OrdersWithRevisionResponse
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
    api_instance = iikocloud_client.DeliveriesRetrieveApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    orders_by_delivery_date_and_status_request = iikocloud_client.OrdersByDeliveryDateAndStatusRequest() # OrdersByDeliveryDateAndStatusRequest |  (optional)

    try:
        # Retrieve list of orders by statuses and dates.
        api_response = await api_instance.get_deliveries_by_delivery_date_and_status(timeout=timeout, orders_by_delivery_date_and_status_request=orders_by_delivery_date_and_status_request)
        print("The response of DeliveriesRetrieveApi->get_deliveries_by_delivery_date_and_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->get_deliveries_by_delivery_date_and_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **orders_by_delivery_date_and_status_request** | [**OrdersByDeliveryDateAndStatusRequest**](OrdersByDeliveryDateAndStatusRequest.md)|  | [optional] 

### Return type

[**OrdersWithRevisionResponse**](OrdersWithRevisionResponse.md)

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

# **get_deliveries_by_id**
> OrdersResponse get_deliveries_by_id(timeout=timeout, orders_by_id_request=orders_by_id_request)

Retrieve orders by IDs.



 > Restriction group: `Orders: receiving`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.orders_by_id_request import OrdersByIdRequest
from iikocloud_client.models.orders_response import OrdersResponse
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
    api_instance = iikocloud_client.DeliveriesRetrieveApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    orders_by_id_request = iikocloud_client.OrdersByIdRequest() # OrdersByIdRequest |  (optional)

    try:
        # Retrieve orders by IDs.
        api_response = await api_instance.get_deliveries_by_id(timeout=timeout, orders_by_id_request=orders_by_id_request)
        print("The response of DeliveriesRetrieveApi->get_deliveries_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->get_deliveries_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **orders_by_id_request** | [**OrdersByIdRequest**](OrdersByIdRequest.md)|  | [optional] 

### Return type

[**OrdersResponse**](OrdersResponse.md)

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

# **get_deliveries_by_revision**
> OrdersWithRevisionResponse get_deliveries_by_revision(timeout=timeout, orders_by_revision_request=orders_by_revision_request)

Retrieve list of orders changed from the time revision was passed.



 > Restriction group: `Orders: receiving by revision`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.orders_by_revision_request import OrdersByRevisionRequest
from iikocloud_client.models.orders_with_revision_response import OrdersWithRevisionResponse
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
    api_instance = iikocloud_client.DeliveriesRetrieveApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    orders_by_revision_request = iikocloud_client.OrdersByRevisionRequest() # OrdersByRevisionRequest |  (optional)

    try:
        # Retrieve list of orders changed from the time revision was passed.
        api_response = await api_instance.get_deliveries_by_revision(timeout=timeout, orders_by_revision_request=orders_by_revision_request)
        print("The response of DeliveriesRetrieveApi->get_deliveries_by_revision:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->get_deliveries_by_revision: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **orders_by_revision_request** | [**OrdersByRevisionRequest**](OrdersByRevisionRequest.md)|  | [optional] 

### Return type

[**OrdersWithRevisionResponse**](OrdersWithRevisionResponse.md)

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

# **get_delivery_history_by_delivery_date_and_phone**
> OrdersWithRevisionResponse get_delivery_history_by_delivery_date_and_phone(timeout=timeout, orders_history_by_delivery_date_and_phone_request=orders_history_by_delivery_date_and_phone_request)

Retrieve list of history orders by telephone number, dates and revision.



 > Restriction group: `Orders: receiving`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.orders_history_by_delivery_date_and_phone_request import OrdersHistoryByDeliveryDateAndPhoneRequest
from iikocloud_client.models.orders_with_revision_response import OrdersWithRevisionResponse
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
    api_instance = iikocloud_client.DeliveriesRetrieveApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    orders_history_by_delivery_date_and_phone_request = iikocloud_client.OrdersHistoryByDeliveryDateAndPhoneRequest() # OrdersHistoryByDeliveryDateAndPhoneRequest |  (optional)

    try:
        # Retrieve list of history orders by telephone number, dates and revision.
        api_response = await api_instance.get_delivery_history_by_delivery_date_and_phone(timeout=timeout, orders_history_by_delivery_date_and_phone_request=orders_history_by_delivery_date_and_phone_request)
        print("The response of DeliveriesRetrieveApi->get_delivery_history_by_delivery_date_and_phone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->get_delivery_history_by_delivery_date_and_phone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **orders_history_by_delivery_date_and_phone_request** | [**OrdersHistoryByDeliveryDateAndPhoneRequest**](OrdersHistoryByDeliveryDateAndPhoneRequest.md)|  | [optional] 

### Return type

[**OrdersWithRevisionResponse**](OrdersWithRevisionResponse.md)

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

# **search_deliveries**
> OrdersWithRevisionResponse search_deliveries(timeout=timeout, orders_by_delivery_date_and_filter_request=orders_by_delivery_date_and_filter_request)

Search orders by search text and additional filters (date, problem, statuses and other).



 > Restriction group: `Orders: receiving`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.orders_by_delivery_date_and_filter_request import OrdersByDeliveryDateAndFilterRequest
from iikocloud_client.models.orders_with_revision_response import OrdersWithRevisionResponse
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
    api_instance = iikocloud_client.DeliveriesRetrieveApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    orders_by_delivery_date_and_filter_request = iikocloud_client.OrdersByDeliveryDateAndFilterRequest() # OrdersByDeliveryDateAndFilterRequest |  (optional)

    try:
        # Search orders by search text and additional filters (date, problem, statuses and other).
        api_response = await api_instance.search_deliveries(timeout=timeout, orders_by_delivery_date_and_filter_request=orders_by_delivery_date_and_filter_request)
        print("The response of DeliveriesRetrieveApi->search_deliveries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesRetrieveApi->search_deliveries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **orders_by_delivery_date_and_filter_request** | [**OrdersByDeliveryDateAndFilterRequest**](OrdersByDeliveryDateAndFilterRequest.md)|  | [optional] 

### Return type

[**OrdersWithRevisionResponse**](OrdersWithRevisionResponse.md)

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

