# iikocloud_client.DeliveriesCreateAndUpdateApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_delivery_order_items**](DeliveriesCreateAndUpdateApi.md#add_delivery_order_items) | **POST** /api/1/deliveries/add_items | Add order items.
[**add_delivery_order_payments**](DeliveriesCreateAndUpdateApi.md#add_delivery_order_payments) | **POST** /api/1/deliveries/add_payments | Add order payments.
[**cancel_delivery_confirmation**](DeliveriesCreateAndUpdateApi.md#cancel_delivery_confirmation) | **POST** /api/1/deliveries/cancel_confirmation | Cancel delivery confirmation.
[**cancel_delivery_order**](DeliveriesCreateAndUpdateApi.md#cancel_delivery_order) | **POST** /api/1/deliveries/cancel | Cancel delivery order.
[**change_delivery_comment**](DeliveriesCreateAndUpdateApi.md#change_delivery_comment) | **POST** /api/1/deliveries/change_comment | Change delivery comment.
[**change_delivery_complete_before**](DeliveriesCreateAndUpdateApi.md#change_delivery_complete_before) | **POST** /api/1/deliveries/change_complete_before | Change time when client wants the order to be delivered.
[**change_delivery_driver_info**](DeliveriesCreateAndUpdateApi.md#change_delivery_driver_info) | **POST** /api/1/deliveries/change_driver_info | Change driver info.
[**change_delivery_external_data**](DeliveriesCreateAndUpdateApi.md#change_delivery_external_data) | **POST** /api/1/deliveries/change_external_data | Change delivery external data.
[**change_delivery_operator**](DeliveriesCreateAndUpdateApi.md#change_delivery_operator) | **POST** /api/1/deliveries/change_operator | Assign/change the order operator.
[**change_delivery_payments**](DeliveriesCreateAndUpdateApi.md#change_delivery_payments) | **POST** /api/1/deliveries/change_payments | Change order&#39;s payments.
[**change_delivery_point**](DeliveriesCreateAndUpdateApi.md#change_delivery_point) | **POST** /api/1/deliveries/change_delivery_point | Change order&#39;s delivery point information.
[**change_delivery_service_type**](DeliveriesCreateAndUpdateApi.md#change_delivery_service_type) | **POST** /api/1/deliveries/change_service_type | Change order&#39;s delivery type.
[**close_delivery_order**](DeliveriesCreateAndUpdateApi.md#close_delivery_order) | **POST** /api/1/deliveries/close | Close order.
[**confirm_delivery**](DeliveriesCreateAndUpdateApi.md#confirm_delivery) | **POST** /api/1/deliveries/confirm | Confirm delivery.
[**create_delivery_order**](DeliveriesCreateAndUpdateApi.md#create_delivery_order) | **POST** /api/1/deliveries/create | Create delivery.
[**print_delivery_bill**](DeliveriesCreateAndUpdateApi.md#print_delivery_bill) | **POST** /api/1/deliveries/print_delivery_bill | Print delivery bill.
[**print_table_order_bill**](DeliveriesCreateAndUpdateApi.md#print_table_order_bill) | **POST** /api/1/order/print_bill | Print bill.
[**update_delivery_order_courier**](DeliveriesCreateAndUpdateApi.md#update_delivery_order_courier) | **POST** /api/1/deliveries/update_order_courier | Update order courier.
[**update_delivery_order_payments**](DeliveriesCreateAndUpdateApi.md#update_delivery_order_payments) | **POST** /api/1/deliveries/update_order_payments | Update order payment details.
[**update_delivery_order_problem**](DeliveriesCreateAndUpdateApi.md#update_delivery_order_problem) | **POST** /api/1/deliveries/update_order_problem | Update order problem.
[**update_delivery_order_status**](DeliveriesCreateAndUpdateApi.md#update_delivery_order_status) | **POST** /api/1/deliveries/update_order_delivery_status | Update delivery status.
[**update_delivery_tracking_link**](DeliveriesCreateAndUpdateApi.md#update_delivery_tracking_link) | **POST** /api/1/deliveries/update_tracking_link | Update tracking link of an order.


# **add_delivery_order_items**
> CorrelationIdResponse add_delivery_order_items(timeout=timeout, add_order_items_request=add_order_items_request)

Add order items.



 > Allowed from version `7.4.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.add_order_items_request import AddOrderItemsRequest
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    add_order_items_request = iikocloud_client.AddOrderItemsRequest() # AddOrderItemsRequest |  (optional)

    try:
        # Add order items.
        api_response = await api_instance.add_delivery_order_items(timeout=timeout, add_order_items_request=add_order_items_request)
        print("The response of DeliveriesCreateAndUpdateApi->add_delivery_order_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->add_delivery_order_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **add_order_items_request** | [**AddOrderItemsRequest**](AddOrderItemsRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **add_delivery_order_payments**
> CorrelationIdResponse add_delivery_order_payments(timeout=timeout, add_order_payments_request=add_order_payments_request)

Add order payments.



 > Allowed from version `8.4.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order payments: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.add_order_payments_request import AddOrderPaymentsRequest
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    add_order_payments_request = iikocloud_client.AddOrderPaymentsRequest() # AddOrderPaymentsRequest |  (optional)

    try:
        # Add order payments.
        api_response = await api_instance.add_delivery_order_payments(timeout=timeout, add_order_payments_request=add_order_payments_request)
        print("The response of DeliveriesCreateAndUpdateApi->add_delivery_order_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->add_delivery_order_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **add_order_payments_request** | [**AddOrderPaymentsRequest**](AddOrderPaymentsRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **cancel_delivery_confirmation**
> CorrelationIdResponse cancel_delivery_confirmation(timeout=timeout, cancel_delivery_confirmation_request=cancel_delivery_confirmation_request)

Cancel delivery confirmation.



 > Allowed from version `7.6.1`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.cancel_delivery_confirmation_request import CancelDeliveryConfirmationRequest
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    cancel_delivery_confirmation_request = iikocloud_client.CancelDeliveryConfirmationRequest() # CancelDeliveryConfirmationRequest |  (optional)

    try:
        # Cancel delivery confirmation.
        api_response = await api_instance.cancel_delivery_confirmation(timeout=timeout, cancel_delivery_confirmation_request=cancel_delivery_confirmation_request)
        print("The response of DeliveriesCreateAndUpdateApi->cancel_delivery_confirmation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->cancel_delivery_confirmation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **cancel_delivery_confirmation_request** | [**CancelDeliveryConfirmationRequest**](CancelDeliveryConfirmationRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **cancel_delivery_order**
> CorrelationIdResponse cancel_delivery_order(timeout=timeout, cancel_order_request=cancel_order_request)

Cancel delivery order.



 > Allowed from version `7.5.4`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.cancel_order_request import CancelOrderRequest
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    cancel_order_request = iikocloud_client.CancelOrderRequest() # CancelOrderRequest |  (optional)

    try:
        # Cancel delivery order.
        api_response = await api_instance.cancel_delivery_order(timeout=timeout, cancel_order_request=cancel_order_request)
        print("The response of DeliveriesCreateAndUpdateApi->cancel_delivery_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->cancel_delivery_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **cancel_order_request** | [**CancelOrderRequest**](CancelOrderRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **change_delivery_comment**
> CorrelationIdResponse change_delivery_comment(timeout=timeout, change_delivery_comment_request=change_delivery_comment_request)

Change delivery comment.



 > Allowed from version `7.6.1`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.change_delivery_comment_request import ChangeDeliveryCommentRequest
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    change_delivery_comment_request = iikocloud_client.ChangeDeliveryCommentRequest() # ChangeDeliveryCommentRequest |  (optional)

    try:
        # Change delivery comment.
        api_response = await api_instance.change_delivery_comment(timeout=timeout, change_delivery_comment_request=change_delivery_comment_request)
        print("The response of DeliveriesCreateAndUpdateApi->change_delivery_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->change_delivery_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **change_delivery_comment_request** | [**ChangeDeliveryCommentRequest**](ChangeDeliveryCommentRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **change_delivery_complete_before**
> CorrelationIdResponse change_delivery_complete_before(timeout=timeout, change_complete_before_request=change_complete_before_request)

Change time when client wants the order to be delivered.



 > Allowed from version `7.5.4`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.change_complete_before_request import ChangeCompleteBeforeRequest
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    change_complete_before_request = iikocloud_client.ChangeCompleteBeforeRequest() # ChangeCompleteBeforeRequest |  (optional)

    try:
        # Change time when client wants the order to be delivered.
        api_response = await api_instance.change_delivery_complete_before(timeout=timeout, change_complete_before_request=change_complete_before_request)
        print("The response of DeliveriesCreateAndUpdateApi->change_delivery_complete_before:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->change_delivery_complete_before: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **change_complete_before_request** | [**ChangeCompleteBeforeRequest**](ChangeCompleteBeforeRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **change_delivery_driver_info**
> CorrelationIdResponse change_delivery_driver_info(timeout=timeout, change_driver_info_request=change_driver_info_request)

Change driver info.



 > Allowed from version `8.6.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order driver: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.change_driver_info_request import ChangeDriverInfoRequest
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    change_driver_info_request = iikocloud_client.ChangeDriverInfoRequest() # ChangeDriverInfoRequest |  (optional)

    try:
        # Change driver info.
        api_response = await api_instance.change_delivery_driver_info(timeout=timeout, change_driver_info_request=change_driver_info_request)
        print("The response of DeliveriesCreateAndUpdateApi->change_delivery_driver_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->change_delivery_driver_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **change_driver_info_request** | [**ChangeDriverInfoRequest**](ChangeDriverInfoRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **change_delivery_external_data**
> CorrelationIdResponse change_delivery_external_data(timeout=timeout, change_external_data_request=change_external_data_request)

Change delivery external data.



 > Restriction group: `Orders: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.change_external_data_request import ChangeExternalDataRequest
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    change_external_data_request = iikocloud_client.ChangeExternalDataRequest() # ChangeExternalDataRequest |  (optional)

    try:
        # Change delivery external data.
        api_response = await api_instance.change_delivery_external_data(timeout=timeout, change_external_data_request=change_external_data_request)
        print("The response of DeliveriesCreateAndUpdateApi->change_delivery_external_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->change_delivery_external_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **change_external_data_request** | [**ChangeExternalDataRequest**](ChangeExternalDataRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **change_delivery_operator**
> CorrelationIdResponse change_delivery_operator(timeout=timeout, change_delivery_operator_request=change_delivery_operator_request)

Assign/change the order operator.



 > Allowed from version `7.6.1`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.change_delivery_operator_request import ChangeDeliveryOperatorRequest
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    change_delivery_operator_request = iikocloud_client.ChangeDeliveryOperatorRequest() # ChangeDeliveryOperatorRequest |  (optional)

    try:
        # Assign/change the order operator.
        api_response = await api_instance.change_delivery_operator(timeout=timeout, change_delivery_operator_request=change_delivery_operator_request)
        print("The response of DeliveriesCreateAndUpdateApi->change_delivery_operator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->change_delivery_operator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **change_delivery_operator_request** | [**ChangeDeliveryOperatorRequest**](ChangeDeliveryOperatorRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **change_delivery_payments**
> CorrelationIdResponse change_delivery_payments(timeout=timeout, change_payments_request=change_payments_request)

Change order's payments.

> Method will fail if there are any processed payments in the order.
> If all payments in the order are unprocessed they will be removed and replaced with new ones.

 > Allowed from version `7.6.3`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order payments: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.change_payments_request import ChangePaymentsRequest
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    change_payments_request = iikocloud_client.ChangePaymentsRequest() # ChangePaymentsRequest |  (optional)

    try:
        # Change order's payments.
        api_response = await api_instance.change_delivery_payments(timeout=timeout, change_payments_request=change_payments_request)
        print("The response of DeliveriesCreateAndUpdateApi->change_delivery_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->change_delivery_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **change_payments_request** | [**ChangePaymentsRequest**](ChangePaymentsRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **change_delivery_point**
> CorrelationIdResponse change_delivery_point(timeout=timeout, change_delivery_point_request=change_delivery_point_request)

Change order's delivery point information.



 > Allowed from version `7.5.4`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.change_delivery_point_request import ChangeDeliveryPointRequest
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    change_delivery_point_request = iikocloud_client.ChangeDeliveryPointRequest() # ChangeDeliveryPointRequest |  (optional)

    try:
        # Change order's delivery point information.
        api_response = await api_instance.change_delivery_point(timeout=timeout, change_delivery_point_request=change_delivery_point_request)
        print("The response of DeliveriesCreateAndUpdateApi->change_delivery_point:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->change_delivery_point: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **change_delivery_point_request** | [**ChangeDeliveryPointRequest**](ChangeDeliveryPointRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **change_delivery_service_type**
> CorrelationIdResponse change_delivery_service_type(timeout=timeout, change_service_type_request=change_service_type_request)

Change order's delivery type.



 > Allowed from version `7.5.4`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.change_service_type_request import ChangeServiceTypeRequest
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    change_service_type_request = iikocloud_client.ChangeServiceTypeRequest() # ChangeServiceTypeRequest |  (optional)

    try:
        # Change order's delivery type.
        api_response = await api_instance.change_delivery_service_type(timeout=timeout, change_service_type_request=change_service_type_request)
        print("The response of DeliveriesCreateAndUpdateApi->change_delivery_service_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->change_delivery_service_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **change_service_type_request** | [**ChangeServiceTypeRequest**](ChangeServiceTypeRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **close_delivery_order**
> CorrelationIdResponse close_delivery_order(timeout=timeout, close_delivery_order_request=close_delivery_order_request)

Close order.

> Before version `8.0.6` it's possible to close deliveries with `DeliveryByClient`
orderServiceType only, starting from version `8.0.6` it's also possible to close
`DeliveryByCourier` deiveries in the DeliveryStatus `OnWay` or `Delivered` .

 > Allowed from version `7.4.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.close_delivery_order_request import CloseDeliveryOrderRequest
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    close_delivery_order_request = iikocloud_client.CloseDeliveryOrderRequest() # CloseDeliveryOrderRequest |  (optional)

    try:
        # Close order.
        api_response = await api_instance.close_delivery_order(timeout=timeout, close_delivery_order_request=close_delivery_order_request)
        print("The response of DeliveriesCreateAndUpdateApi->close_delivery_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->close_delivery_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **close_delivery_order_request** | [**CloseDeliveryOrderRequest**](CloseDeliveryOrderRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **confirm_delivery**
> CorrelationIdResponse confirm_delivery(timeout=timeout, confirm_delivery_request=confirm_delivery_request)

Confirm delivery.



 > Allowed from version `7.6.1`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.confirm_delivery_request import ConfirmDeliveryRequest
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    confirm_delivery_request = iikocloud_client.ConfirmDeliveryRequest() # ConfirmDeliveryRequest |  (optional)

    try:
        # Confirm delivery.
        api_response = await api_instance.confirm_delivery(timeout=timeout, confirm_delivery_request=confirm_delivery_request)
        print("The response of DeliveriesCreateAndUpdateApi->confirm_delivery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->confirm_delivery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **confirm_delivery_request** | [**ConfirmDeliveryRequest**](ConfirmDeliveryRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **create_delivery_order**
> OrderResponse create_delivery_order(timeout=timeout, create_order_request=create_order_request)

Create delivery.



 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: creating`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.create_order_request import CreateOrderRequest
from iikocloud_client.models.order_response import OrderResponse
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    create_order_request = iikocloud_client.CreateOrderRequest() # CreateOrderRequest |  (optional)

    try:
        # Create delivery.
        api_response = await api_instance.create_delivery_order(timeout=timeout, create_order_request=create_order_request)
        print("The response of DeliveriesCreateAndUpdateApi->create_delivery_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->create_delivery_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **create_order_request** | [**CreateOrderRequest**](CreateOrderRequest.md)|  | [optional] 

### Return type

[**OrderResponse**](OrderResponse.md)

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

# **print_delivery_bill**
> CorrelationIdResponse print_delivery_bill(timeout=timeout, print_delivery_bill_request=print_delivery_bill_request)

Print delivery bill.



 > Allowed from version `7.6.1`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
from iikocloud_client.models.print_delivery_bill_request import PrintDeliveryBillRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    print_delivery_bill_request = iikocloud_client.PrintDeliveryBillRequest() # PrintDeliveryBillRequest |  (optional)

    try:
        # Print delivery bill.
        api_response = await api_instance.print_delivery_bill(timeout=timeout, print_delivery_bill_request=print_delivery_bill_request)
        print("The response of DeliveriesCreateAndUpdateApi->print_delivery_bill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->print_delivery_bill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **print_delivery_bill_request** | [**PrintDeliveryBillRequest**](PrintDeliveryBillRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **print_table_order_bill**
> CorrelationIdResponse print_table_order_bill(timeout=timeout, print_bill_request=print_bill_request)

Print bill.



 > This method is a command. Use `api/1/commands/status` method to get the progress status.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
from iikocloud_client.models.print_bill_request import PrintBillRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    print_bill_request = iikocloud_client.PrintBillRequest() # PrintBillRequest |  (optional)

    try:
        # Print bill.
        api_response = await api_instance.print_table_order_bill(timeout=timeout, print_bill_request=print_bill_request)
        print("The response of DeliveriesCreateAndUpdateApi->print_table_order_bill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->print_table_order_bill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **print_bill_request** | [**PrintBillRequest**](PrintBillRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **update_delivery_order_courier**
> CorrelationIdResponse update_delivery_order_courier(timeout=timeout, update_order_courier_request=update_order_courier_request)

Update order courier.



 > Allowed from version `7.1.5`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order driver: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
from iikocloud_client.models.update_order_courier_request import UpdateOrderCourierRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    update_order_courier_request = iikocloud_client.UpdateOrderCourierRequest() # UpdateOrderCourierRequest |  (optional)

    try:
        # Update order courier.
        api_response = await api_instance.update_delivery_order_courier(timeout=timeout, update_order_courier_request=update_order_courier_request)
        print("The response of DeliveriesCreateAndUpdateApi->update_delivery_order_courier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->update_delivery_order_courier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **update_order_courier_request** | [**UpdateOrderCourierRequest**](UpdateOrderCourierRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **update_delivery_order_payments**
> CorrelationIdResponse update_delivery_order_payments(timeout=timeout, update_order_payments_request=update_order_payments_request)

Update order payment details.

> Deprecated, use `api/1/deliveries/change_payments` method instead.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Deprecated`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
from iikocloud_client.models.update_order_payments_request import UpdateOrderPaymentsRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    update_order_payments_request = iikocloud_client.UpdateOrderPaymentsRequest() # UpdateOrderPaymentsRequest |  (optional)

    try:
        # Update order payment details.
        api_response = await api_instance.update_delivery_order_payments(timeout=timeout, update_order_payments_request=update_order_payments_request)
        print("The response of DeliveriesCreateAndUpdateApi->update_delivery_order_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->update_delivery_order_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **update_order_payments_request** | [**UpdateOrderPaymentsRequest**](UpdateOrderPaymentsRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **update_delivery_order_problem**
> CorrelationIdResponse update_delivery_order_problem(timeout=timeout, update_order_problem_request=update_order_problem_request)

Update order problem.



 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
from iikocloud_client.models.update_order_problem_request import UpdateOrderProblemRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    update_order_problem_request = iikocloud_client.UpdateOrderProblemRequest() # UpdateOrderProblemRequest |  (optional)

    try:
        # Update order problem.
        api_response = await api_instance.update_delivery_order_problem(timeout=timeout, update_order_problem_request=update_order_problem_request)
        print("The response of DeliveriesCreateAndUpdateApi->update_delivery_order_problem:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->update_delivery_order_problem: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **update_order_problem_request** | [**UpdateOrderProblemRequest**](UpdateOrderProblemRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **update_delivery_order_status**
> CorrelationIdResponse update_delivery_order_status(timeout=timeout, update_delivery_status_request=update_delivery_status_request)

Update delivery status.



 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
from iikocloud_client.models.update_delivery_status_request import UpdateDeliveryStatusRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    update_delivery_status_request = iikocloud_client.UpdateDeliveryStatusRequest() # UpdateDeliveryStatusRequest |  (optional)

    try:
        # Update delivery status.
        api_response = await api_instance.update_delivery_order_status(timeout=timeout, update_delivery_status_request=update_delivery_status_request)
        print("The response of DeliveriesCreateAndUpdateApi->update_delivery_order_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->update_delivery_order_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **update_delivery_status_request** | [**UpdateDeliveryStatusRequest**](UpdateDeliveryStatusRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **update_delivery_tracking_link**
> update_delivery_tracking_link(timeout=timeout, update_tracking_link_request=update_tracking_link_request)

Update tracking link of an order.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.update_tracking_link_request import UpdateTrackingLinkRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    update_tracking_link_request = iikocloud_client.UpdateTrackingLinkRequest() # UpdateTrackingLinkRequest |  (optional)

    try:
        # Update tracking link of an order.
        await api_instance.update_delivery_tracking_link(timeout=timeout, update_tracking_link_request=update_tracking_link_request)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->update_delivery_tracking_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **update_tracking_link_request** | [**UpdateTrackingLinkRequest**](UpdateTrackingLinkRequest.md)|  | [optional] 

### Return type

void (empty response body)

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

