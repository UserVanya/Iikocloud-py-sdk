# iikocloud_client.CustomersApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loyalty_iiko_customer_card_add_post**](CustomersApi.md#loyalty_iiko_customer_card_add_post) | **POST** /loyalty/iiko/customer/card/add | Add card.
[**loyalty_iiko_customer_card_remove_post**](CustomersApi.md#loyalty_iiko_customer_card_remove_post) | **POST** /loyalty/iiko/customer/card/remove | Delete card.
[**loyalty_iiko_customer_create_or_update_post**](CustomersApi.md#loyalty_iiko_customer_create_or_update_post) | **POST** /loyalty/iiko/customer/create_or_update | Create or update customer.
[**loyalty_iiko_customer_info_post**](CustomersApi.md#loyalty_iiko_customer_info_post) | **POST** /loyalty/iiko/customer/info | Get customer info.
[**loyalty_iiko_customer_program_add_post**](CustomersApi.md#loyalty_iiko_customer_program_add_post) | **POST** /loyalty/iiko/customer/program/add | Add customer to program.
[**loyalty_iiko_customer_wallet_cancel_hold_post**](CustomersApi.md#loyalty_iiko_customer_wallet_cancel_hold_post) | **POST** /loyalty/iiko/customer/wallet/cancel_hold | Cancel hold money.
[**loyalty_iiko_customer_wallet_chargeoff_post**](CustomersApi.md#loyalty_iiko_customer_wallet_chargeoff_post) | **POST** /loyalty/iiko/customer/wallet/chargeoff | Withdraw balance.
[**loyalty_iiko_customer_wallet_hold_post**](CustomersApi.md#loyalty_iiko_customer_wallet_hold_post) | **POST** /loyalty/iiko/customer/wallet/hold | Hold money.
[**loyalty_iiko_customer_wallet_topup_post**](CustomersApi.md#loyalty_iiko_customer_wallet_topup_post) | **POST** /loyalty/iiko/customer/wallet/topup | Refill balance.
[**loyalty_iiko_delete_customers_post**](CustomersApi.md#loyalty_iiko_delete_customers_post) | **POST** /loyalty/iiko/delete_customers | Logical deletion of customers.
[**loyalty_iiko_get_counters_post**](CustomersApi.md#loyalty_iiko_get_counters_post) | **POST** /loyalty/iiko/get_counters | Get counters.
[**loyalty_iiko_restore_customers_post**](CustomersApi.md#loyalty_iiko_restore_customers_post) | **POST** /loyalty/iiko/restore_customers | Logical recovery of customers.


# **loyalty_iiko_customer_card_add_post**
> object loyalty_iiko_customer_card_add_post(timeout=timeout, customer_add_magnet_card_request=customer_add_magnet_card_request)

Add card.

Add new card for customer.

 > Restriction group: `Guests: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.customer_add_magnet_card_request import CustomerAddMagnetCardRequest
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    customer_add_magnet_card_request = iikocloud_client.CustomerAddMagnetCardRequest() # CustomerAddMagnetCardRequest |  (optional)

    try:
        # Add card.
        api_response = await api_instance.loyalty_iiko_customer_card_add_post(timeout=timeout, customer_add_magnet_card_request=customer_add_magnet_card_request)
        print("The response of CustomersApi->loyalty_iiko_customer_card_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_card_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **customer_add_magnet_card_request** | [**CustomerAddMagnetCardRequest**](CustomerAddMagnetCardRequest.md)|  | [optional] 

### Return type

**object**

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

# **loyalty_iiko_customer_card_remove_post**
> object loyalty_iiko_customer_card_remove_post(timeout=timeout, customer_delete_magnet_card_request=customer_delete_magnet_card_request)

Delete card.

Delete existing card for customer.

 > Restriction group: `Guests: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.customer_delete_magnet_card_request import CustomerDeleteMagnetCardRequest
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    customer_delete_magnet_card_request = iikocloud_client.CustomerDeleteMagnetCardRequest() # CustomerDeleteMagnetCardRequest |  (optional)

    try:
        # Delete card.
        api_response = await api_instance.loyalty_iiko_customer_card_remove_post(timeout=timeout, customer_delete_magnet_card_request=customer_delete_magnet_card_request)
        print("The response of CustomersApi->loyalty_iiko_customer_card_remove_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_card_remove_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **customer_delete_magnet_card_request** | [**CustomerDeleteMagnetCardRequest**](CustomerDeleteMagnetCardRequest.md)|  | [optional] 

### Return type

**object**

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

# **loyalty_iiko_customer_create_or_update_post**
> CustomerCreateOrUpdateCustomerResponse loyalty_iiko_customer_create_or_update_post(timeout=timeout, customer_create_or_update_customer_request=customer_create_or_update_customer_request)

Create or update customer.

Create or update customer info by id or phone or card track.

 > Restriction group: `Guests: creating`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.customer_create_or_update_customer_request import CustomerCreateOrUpdateCustomerRequest
from iikocloud_client.models.customer_create_or_update_customer_response import CustomerCreateOrUpdateCustomerResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    customer_create_or_update_customer_request = iikocloud_client.CustomerCreateOrUpdateCustomerRequest() # CustomerCreateOrUpdateCustomerRequest |  (optional)

    try:
        # Create or update customer.
        api_response = await api_instance.loyalty_iiko_customer_create_or_update_post(timeout=timeout, customer_create_or_update_customer_request=customer_create_or_update_customer_request)
        print("The response of CustomersApi->loyalty_iiko_customer_create_or_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_create_or_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **customer_create_or_update_customer_request** | [**CustomerCreateOrUpdateCustomerRequest**](CustomerCreateOrUpdateCustomerRequest.md)|  | [optional] 

### Return type

[**CustomerCreateOrUpdateCustomerResponse**](CustomerCreateOrUpdateCustomerResponse.md)

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

# **loyalty_iiko_customer_info_post**
> CustomerGetCustomerInfoResponse loyalty_iiko_customer_info_post(timeout=timeout, customer_get_customer_info_request=customer_get_customer_info_request)

Get customer info.

Get customer info by specified criterion.

 > Restriction group: `Guests: info`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.customer_get_customer_info_request import CustomerGetCustomerInfoRequest
from iikocloud_client.models.customer_get_customer_info_response import CustomerGetCustomerInfoResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    customer_get_customer_info_request = iikocloud_client.CustomerGetCustomerInfoRequest() # CustomerGetCustomerInfoRequest |  (optional)

    try:
        # Get customer info.
        api_response = await api_instance.loyalty_iiko_customer_info_post(timeout=timeout, customer_get_customer_info_request=customer_get_customer_info_request)
        print("The response of CustomersApi->loyalty_iiko_customer_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **customer_get_customer_info_request** | [**CustomerGetCustomerInfoRequest**](CustomerGetCustomerInfoRequest.md)|  | [optional] 

### Return type

[**CustomerGetCustomerInfoResponse**](CustomerGetCustomerInfoResponse.md)

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

# **loyalty_iiko_customer_program_add_post**
> CustomerAddCustomerToProgramResponse loyalty_iiko_customer_program_add_post(timeout=timeout, customer_add_customer_to_program_request=customer_add_customer_to_program_request)

Add customer to program.

Add new customer for program.

 > Restriction group: `Guests: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.customer_add_customer_to_program_request import CustomerAddCustomerToProgramRequest
from iikocloud_client.models.customer_add_customer_to_program_response import CustomerAddCustomerToProgramResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    customer_add_customer_to_program_request = iikocloud_client.CustomerAddCustomerToProgramRequest() # CustomerAddCustomerToProgramRequest |  (optional)

    try:
        # Add customer to program.
        api_response = await api_instance.loyalty_iiko_customer_program_add_post(timeout=timeout, customer_add_customer_to_program_request=customer_add_customer_to_program_request)
        print("The response of CustomersApi->loyalty_iiko_customer_program_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_program_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **customer_add_customer_to_program_request** | [**CustomerAddCustomerToProgramRequest**](CustomerAddCustomerToProgramRequest.md)|  | [optional] 

### Return type

[**CustomerAddCustomerToProgramResponse**](CustomerAddCustomerToProgramResponse.md)

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

# **loyalty_iiko_customer_wallet_cancel_hold_post**
> object loyalty_iiko_customer_wallet_cancel_hold_post(timeout=timeout, customer_cancel_hold_money_request=customer_cancel_hold_money_request)

Cancel hold money.

Cancel holding transaction that created earlier.

 > Restriction group: `Loyalty: wallets`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.customer_cancel_hold_money_request import CustomerCancelHoldMoneyRequest
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    customer_cancel_hold_money_request = iikocloud_client.CustomerCancelHoldMoneyRequest() # CustomerCancelHoldMoneyRequest |  (optional)

    try:
        # Cancel hold money.
        api_response = await api_instance.loyalty_iiko_customer_wallet_cancel_hold_post(timeout=timeout, customer_cancel_hold_money_request=customer_cancel_hold_money_request)
        print("The response of CustomersApi->loyalty_iiko_customer_wallet_cancel_hold_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_wallet_cancel_hold_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **customer_cancel_hold_money_request** | [**CustomerCancelHoldMoneyRequest**](CustomerCancelHoldMoneyRequest.md)|  | [optional] 

### Return type

**object**

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

# **loyalty_iiko_customer_wallet_chargeoff_post**
> object loyalty_iiko_customer_wallet_chargeoff_post(timeout=timeout, customer_change_user_balance_request=customer_change_user_balance_request)

Withdraw balance.

Withdraw customer balance.

 > Restriction group: `Loyalty: wallets`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.customer_change_user_balance_request import CustomerChangeUserBalanceRequest
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    customer_change_user_balance_request = iikocloud_client.CustomerChangeUserBalanceRequest() # CustomerChangeUserBalanceRequest |  (optional)

    try:
        # Withdraw balance.
        api_response = await api_instance.loyalty_iiko_customer_wallet_chargeoff_post(timeout=timeout, customer_change_user_balance_request=customer_change_user_balance_request)
        print("The response of CustomersApi->loyalty_iiko_customer_wallet_chargeoff_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_wallet_chargeoff_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **customer_change_user_balance_request** | [**CustomerChangeUserBalanceRequest**](CustomerChangeUserBalanceRequest.md)|  | [optional] 

### Return type

**object**

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

# **loyalty_iiko_customer_wallet_hold_post**
> CustomerHoldMoneyResponse loyalty_iiko_customer_wallet_hold_post(timeout=timeout, customer_hold_money_request=customer_hold_money_request)

Hold money.

Hold customer's money in loyalty program. Payment will be process on POS during processing of an order.

 > Restriction group: `Loyalty: wallets`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.customer_hold_money_request import CustomerHoldMoneyRequest
from iikocloud_client.models.customer_hold_money_response import CustomerHoldMoneyResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    customer_hold_money_request = iikocloud_client.CustomerHoldMoneyRequest() # CustomerHoldMoneyRequest |  (optional)

    try:
        # Hold money.
        api_response = await api_instance.loyalty_iiko_customer_wallet_hold_post(timeout=timeout, customer_hold_money_request=customer_hold_money_request)
        print("The response of CustomersApi->loyalty_iiko_customer_wallet_hold_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_wallet_hold_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **customer_hold_money_request** | [**CustomerHoldMoneyRequest**](CustomerHoldMoneyRequest.md)|  | [optional] 

### Return type

[**CustomerHoldMoneyResponse**](CustomerHoldMoneyResponse.md)

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

# **loyalty_iiko_customer_wallet_topup_post**
> object loyalty_iiko_customer_wallet_topup_post(timeout=timeout, customer_change_user_balance_request=customer_change_user_balance_request)

Refill balance.

Refill customer balance.

 > Restriction group: `Loyalty: wallets`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.customer_change_user_balance_request import CustomerChangeUserBalanceRequest
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    customer_change_user_balance_request = iikocloud_client.CustomerChangeUserBalanceRequest() # CustomerChangeUserBalanceRequest |  (optional)

    try:
        # Refill balance.
        api_response = await api_instance.loyalty_iiko_customer_wallet_topup_post(timeout=timeout, customer_change_user_balance_request=customer_change_user_balance_request)
        print("The response of CustomersApi->loyalty_iiko_customer_wallet_topup_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_wallet_topup_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **customer_change_user_balance_request** | [**CustomerChangeUserBalanceRequest**](CustomerChangeUserBalanceRequest.md)|  | [optional] 

### Return type

**object**

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

# **loyalty_iiko_delete_customers_post**
> CustomerDeleteCustomersResponse loyalty_iiko_delete_customers_post(timeout=timeout, customer_delete_customers_request=customer_delete_customers_request)

Logical deletion of customers.

Mark customers as deleted.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.customer_delete_customers_request import CustomerDeleteCustomersRequest
from iikocloud_client.models.customer_delete_customers_response import CustomerDeleteCustomersResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    customer_delete_customers_request = iikocloud_client.CustomerDeleteCustomersRequest() # CustomerDeleteCustomersRequest |  (optional)

    try:
        # Logical deletion of customers.
        api_response = await api_instance.loyalty_iiko_delete_customers_post(timeout=timeout, customer_delete_customers_request=customer_delete_customers_request)
        print("The response of CustomersApi->loyalty_iiko_delete_customers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_delete_customers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **customer_delete_customers_request** | [**CustomerDeleteCustomersRequest**](CustomerDeleteCustomersRequest.md)|  | [optional] 

### Return type

[**CustomerDeleteCustomersResponse**](CustomerDeleteCustomersResponse.md)

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

# **loyalty_iiko_get_counters_post**
> LoyaltyResultGetCountersResponse loyalty_iiko_get_counters_post(timeout=timeout, loyalty_result_get_counters_request=loyalty_result_get_counters_request)

Get counters.

Get customer orders count and sum for different period.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.loyalty_result_get_counters_request import LoyaltyResultGetCountersRequest
from iikocloud_client.models.loyalty_result_get_counters_response import LoyaltyResultGetCountersResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    loyalty_result_get_counters_request = iikocloud_client.LoyaltyResultGetCountersRequest() # LoyaltyResultGetCountersRequest |  (optional)

    try:
        # Get counters.
        api_response = await api_instance.loyalty_iiko_get_counters_post(timeout=timeout, loyalty_result_get_counters_request=loyalty_result_get_counters_request)
        print("The response of CustomersApi->loyalty_iiko_get_counters_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_get_counters_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **loyalty_result_get_counters_request** | [**LoyaltyResultGetCountersRequest**](LoyaltyResultGetCountersRequest.md)|  | [optional] 

### Return type

[**LoyaltyResultGetCountersResponse**](LoyaltyResultGetCountersResponse.md)

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

# **loyalty_iiko_restore_customers_post**
> CustomerRestoreCustomersResponse loyalty_iiko_restore_customers_post(timeout=timeout, customer_restore_customers_request=customer_restore_customers_request)

Logical recovery of customers.

Removing deletion flags for customers.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.customer_restore_customers_request import CustomerRestoreCustomersRequest
from iikocloud_client.models.customer_restore_customers_response import CustomerRestoreCustomersResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    customer_restore_customers_request = iikocloud_client.CustomerRestoreCustomersRequest() # CustomerRestoreCustomersRequest |  (optional)

    try:
        # Logical recovery of customers.
        api_response = await api_instance.loyalty_iiko_restore_customers_post(timeout=timeout, customer_restore_customers_request=customer_restore_customers_request)
        print("The response of CustomersApi->loyalty_iiko_restore_customers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_restore_customers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **customer_restore_customers_request** | [**CustomerRestoreCustomersRequest**](CustomerRestoreCustomersRequest.md)|  | [optional] 

### Return type

[**CustomerRestoreCustomersResponse**](CustomerRestoreCustomersResponse.md)

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

