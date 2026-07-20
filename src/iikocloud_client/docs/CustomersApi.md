# iikocloud_client.CustomersApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_customer_magnet_card**](CustomersApi.md#add_customer_magnet_card) | **POST** /api/1/loyalty/iiko/customer/card/add | Add card.
[**add_customer_to_program**](CustomersApi.md#add_customer_to_program) | **POST** /api/1/loyalty/iiko/customer/program/add | Add customer to program.
[**cancel_customer_balance_hold**](CustomersApi.md#cancel_customer_balance_hold) | **POST** /api/1/loyalty/iiko/customer/wallet/cancel_hold | Cancel hold money.
[**create_or_update_customer**](CustomersApi.md#create_or_update_customer) | **POST** /api/1/loyalty/iiko/customer/create_or_update | Create or update customer.
[**delete_customers**](CustomersApi.md#delete_customers) | **POST** /api/1/loyalty/iiko/delete_customers | Logical deletion of customers.
[**get_customer_info**](CustomersApi.md#get_customer_info) | **POST** /api/1/loyalty/iiko/customer/info | Get customer info.
[**get_loyalty_counters**](CustomersApi.md#get_loyalty_counters) | **POST** /api/1/loyalty/iiko/get_counters | Get counters.
[**hold_customer_balance**](CustomersApi.md#hold_customer_balance) | **POST** /api/1/loyalty/iiko/customer/wallet/hold | Hold money.
[**remove_customer_magnet_card**](CustomersApi.md#remove_customer_magnet_card) | **POST** /api/1/loyalty/iiko/customer/card/remove | Delete card.
[**restore_customers**](CustomersApi.md#restore_customers) | **POST** /api/1/loyalty/iiko/restore_customers | Logical recovery of customers.
[**top_up_customer_balance**](CustomersApi.md#top_up_customer_balance) | **POST** /api/1/loyalty/iiko/customer/wallet/topup | Refill balance.
[**withdraw_customer_balance**](CustomersApi.md#withdraw_customer_balance) | **POST** /api/1/loyalty/iiko/customer/wallet/chargeoff | Withdraw balance.


# **add_customer_magnet_card**
> object add_customer_magnet_card(timeout=timeout, add_magnet_card_request=add_magnet_card_request)

Add card.

Add new card for customer.

 > Restriction group: `Guests: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.add_magnet_card_request import AddMagnetCardRequest
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    add_magnet_card_request = iikocloud_client.AddMagnetCardRequest() # AddMagnetCardRequest |  (optional)

    try:
        # Add card.
        api_response = await api_instance.add_customer_magnet_card(timeout=timeout, add_magnet_card_request=add_magnet_card_request)
        print("The response of CustomersApi->add_customer_magnet_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->add_customer_magnet_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **add_magnet_card_request** | [**AddMagnetCardRequest**](AddMagnetCardRequest.md)|  | [optional] 

### Return type

**object**

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

# **add_customer_to_program**
> AddCustomerToProgramResponse add_customer_to_program(timeout=timeout, add_customer_to_program_request=add_customer_to_program_request)

Add customer to program.

Add new customer for program.

 > Restriction group: `Guests: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.add_customer_to_program_request import AddCustomerToProgramRequest
from iikocloud_client.models.add_customer_to_program_response import AddCustomerToProgramResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    add_customer_to_program_request = iikocloud_client.AddCustomerToProgramRequest() # AddCustomerToProgramRequest |  (optional)

    try:
        # Add customer to program.
        api_response = await api_instance.add_customer_to_program(timeout=timeout, add_customer_to_program_request=add_customer_to_program_request)
        print("The response of CustomersApi->add_customer_to_program:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->add_customer_to_program: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **add_customer_to_program_request** | [**AddCustomerToProgramRequest**](AddCustomerToProgramRequest.md)|  | [optional] 

### Return type

[**AddCustomerToProgramResponse**](AddCustomerToProgramResponse.md)

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

# **cancel_customer_balance_hold**
> object cancel_customer_balance_hold(timeout=timeout, cancel_hold_money_request=cancel_hold_money_request)

Cancel hold money.

Cancel holding transaction that created earlier.

 > Restriction group: `Loyalty: wallets`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.cancel_hold_money_request import CancelHoldMoneyRequest
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    cancel_hold_money_request = iikocloud_client.CancelHoldMoneyRequest() # CancelHoldMoneyRequest |  (optional)

    try:
        # Cancel hold money.
        api_response = await api_instance.cancel_customer_balance_hold(timeout=timeout, cancel_hold_money_request=cancel_hold_money_request)
        print("The response of CustomersApi->cancel_customer_balance_hold:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->cancel_customer_balance_hold: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **cancel_hold_money_request** | [**CancelHoldMoneyRequest**](CancelHoldMoneyRequest.md)|  | [optional] 

### Return type

**object**

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

# **create_or_update_customer**
> CreateOrUpdateCustomerResponse create_or_update_customer(timeout=timeout, create_or_update_customer_request=create_or_update_customer_request)

Create or update customer.

Create or update customer info by id or phone or card track.

 > Restriction group: `Guests: creating`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.create_or_update_customer_request import CreateOrUpdateCustomerRequest
from iikocloud_client.models.create_or_update_customer_response import CreateOrUpdateCustomerResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    create_or_update_customer_request = iikocloud_client.CreateOrUpdateCustomerRequest() # CreateOrUpdateCustomerRequest |  (optional)

    try:
        # Create or update customer.
        api_response = await api_instance.create_or_update_customer(timeout=timeout, create_or_update_customer_request=create_or_update_customer_request)
        print("The response of CustomersApi->create_or_update_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->create_or_update_customer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **create_or_update_customer_request** | [**CreateOrUpdateCustomerRequest**](CreateOrUpdateCustomerRequest.md)|  | [optional] 

### Return type

[**CreateOrUpdateCustomerResponse**](CreateOrUpdateCustomerResponse.md)

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

# **delete_customers**
> DeleteCustomersResponse delete_customers(timeout=timeout, delete_customers_request=delete_customers_request)

Logical deletion of customers.

Mark customers as deleted.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.delete_customers_request import DeleteCustomersRequest
from iikocloud_client.models.delete_customers_response import DeleteCustomersResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    delete_customers_request = iikocloud_client.DeleteCustomersRequest() # DeleteCustomersRequest |  (optional)

    try:
        # Logical deletion of customers.
        api_response = await api_instance.delete_customers(timeout=timeout, delete_customers_request=delete_customers_request)
        print("The response of CustomersApi->delete_customers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->delete_customers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **delete_customers_request** | [**DeleteCustomersRequest**](DeleteCustomersRequest.md)|  | [optional] 

### Return type

[**DeleteCustomersResponse**](DeleteCustomersResponse.md)

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

# **get_customer_info**
> GetCustomerInfoResponse get_customer_info(timeout=timeout, get_customer_info_request=get_customer_info_request)

Get customer info.

Get customer info by specified criterion.

 > Restriction group: `Guests: info`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_customer_info_request import GetCustomerInfoRequest
from iikocloud_client.models.get_customer_info_response import GetCustomerInfoResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_customer_info_request = iikocloud_client.GetCustomerInfoRequest() # GetCustomerInfoRequest |  (optional)

    try:
        # Get customer info.
        api_response = await api_instance.get_customer_info(timeout=timeout, get_customer_info_request=get_customer_info_request)
        print("The response of CustomersApi->get_customer_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->get_customer_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_customer_info_request** | [**GetCustomerInfoRequest**](GetCustomerInfoRequest.md)|  | [optional] 

### Return type

[**GetCustomerInfoResponse**](GetCustomerInfoResponse.md)

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

# **get_loyalty_counters**
> GetCountersResponse get_loyalty_counters(timeout=timeout, get_counters_request=get_counters_request)

Get counters.

Get customer orders count and sum for different period.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_counters_request import GetCountersRequest
from iikocloud_client.models.get_counters_response import GetCountersResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_counters_request = iikocloud_client.GetCountersRequest() # GetCountersRequest |  (optional)

    try:
        # Get counters.
        api_response = await api_instance.get_loyalty_counters(timeout=timeout, get_counters_request=get_counters_request)
        print("The response of CustomersApi->get_loyalty_counters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->get_loyalty_counters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_counters_request** | [**GetCountersRequest**](GetCountersRequest.md)|  | [optional] 

### Return type

[**GetCountersResponse**](GetCountersResponse.md)

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

# **hold_customer_balance**
> HoldMoneyResponse hold_customer_balance(timeout=timeout, hold_money_request=hold_money_request)

Hold money.

Hold customer's money in loyalty program. Payment will be process on POS during processing of an order.

 > Restriction group: `Loyalty: wallets`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.hold_money_request import HoldMoneyRequest
from iikocloud_client.models.hold_money_response import HoldMoneyResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    hold_money_request = iikocloud_client.HoldMoneyRequest() # HoldMoneyRequest |  (optional)

    try:
        # Hold money.
        api_response = await api_instance.hold_customer_balance(timeout=timeout, hold_money_request=hold_money_request)
        print("The response of CustomersApi->hold_customer_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->hold_customer_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **hold_money_request** | [**HoldMoneyRequest**](HoldMoneyRequest.md)|  | [optional] 

### Return type

[**HoldMoneyResponse**](HoldMoneyResponse.md)

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

# **remove_customer_magnet_card**
> object remove_customer_magnet_card(timeout=timeout, delete_magnet_card_request=delete_magnet_card_request)

Delete card.

Delete existing card for customer.

 > Restriction group: `Guests: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.delete_magnet_card_request import DeleteMagnetCardRequest
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    delete_magnet_card_request = iikocloud_client.DeleteMagnetCardRequest() # DeleteMagnetCardRequest |  (optional)

    try:
        # Delete card.
        api_response = await api_instance.remove_customer_magnet_card(timeout=timeout, delete_magnet_card_request=delete_magnet_card_request)
        print("The response of CustomersApi->remove_customer_magnet_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->remove_customer_magnet_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **delete_magnet_card_request** | [**DeleteMagnetCardRequest**](DeleteMagnetCardRequest.md)|  | [optional] 

### Return type

**object**

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

# **restore_customers**
> RestoreCustomersResponse restore_customers(timeout=timeout, restore_customers_request=restore_customers_request)

Logical recovery of customers.

Removing deletion flags for customers.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.restore_customers_request import RestoreCustomersRequest
from iikocloud_client.models.restore_customers_response import RestoreCustomersResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    restore_customers_request = iikocloud_client.RestoreCustomersRequest() # RestoreCustomersRequest |  (optional)

    try:
        # Logical recovery of customers.
        api_response = await api_instance.restore_customers(timeout=timeout, restore_customers_request=restore_customers_request)
        print("The response of CustomersApi->restore_customers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->restore_customers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **restore_customers_request** | [**RestoreCustomersRequest**](RestoreCustomersRequest.md)|  | [optional] 

### Return type

[**RestoreCustomersResponse**](RestoreCustomersResponse.md)

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

# **top_up_customer_balance**
> object top_up_customer_balance(timeout=timeout, change_user_balance_request=change_user_balance_request)

Refill balance.

Refill customer balance.

 > Restriction group: `Loyalty: wallets`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.change_user_balance_request import ChangeUserBalanceRequest
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    change_user_balance_request = iikocloud_client.ChangeUserBalanceRequest() # ChangeUserBalanceRequest |  (optional)

    try:
        # Refill balance.
        api_response = await api_instance.top_up_customer_balance(timeout=timeout, change_user_balance_request=change_user_balance_request)
        print("The response of CustomersApi->top_up_customer_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->top_up_customer_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **change_user_balance_request** | [**ChangeUserBalanceRequest**](ChangeUserBalanceRequest.md)|  | [optional] 

### Return type

**object**

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

# **withdraw_customer_balance**
> object withdraw_customer_balance(timeout=timeout, change_user_balance_request=change_user_balance_request)

Withdraw balance.

Withdraw customer balance.

 > Restriction group: `Loyalty: wallets`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.change_user_balance_request import ChangeUserBalanceRequest
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    change_user_balance_request = iikocloud_client.ChangeUserBalanceRequest() # ChangeUserBalanceRequest |  (optional)

    try:
        # Withdraw balance.
        api_response = await api_instance.withdraw_customer_balance(timeout=timeout, change_user_balance_request=change_user_balance_request)
        print("The response of CustomersApi->withdraw_customer_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->withdraw_customer_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **change_user_balance_request** | [**ChangeUserBalanceRequest**](ChangeUserBalanceRequest.md)|  | [optional] 

### Return type

**object**

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

