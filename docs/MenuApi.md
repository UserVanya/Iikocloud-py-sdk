# iikocloud_client.MenuApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**combo_calculate_post**](MenuApi.md#combo_calculate_post) | **POST** /combo/calculate | Calculate combo price
[**combo_post**](MenuApi.md#combo_post) | **POST** /combo | Get combos info
[**menu_by_id_post**](MenuApi.md#menu_by_id_post) | **POST** /menu/by_id | Retrieve external menu by ID.
[**menu_post**](MenuApi.md#menu_post) | **POST** /menu | External menus with price categories.
[**nomenclature_post**](MenuApi.md#nomenclature_post) | **POST** /nomenclature | Menu.
[**stop_lists_add_post**](MenuApi.md#stop_lists_add_post) | **POST** /stop_lists/add | Add items to out-of-stock list.  (You should have extra rights to use this method).
[**stop_lists_check_post**](MenuApi.md#stop_lists_check_post) | **POST** /stop_lists/check | Check items in out-of-stock list.
[**stop_lists_clear_post**](MenuApi.md#stop_lists_clear_post) | **POST** /stop_lists/clear | Clear out-of-stock list.  (You should have extra rights to use this method).
[**stop_lists_post**](MenuApi.md#stop_lists_post) | **POST** /stop_lists | Out-of-stock items.
[**stop_lists_remove_post**](MenuApi.md#stop_lists_remove_post) | **POST** /stop_lists/remove | Remove items from out-of-stock list.  (You should have extra rights to use this method).


# **combo_calculate_post**
> NetLoyaltyResultCalculateComboPriceResponse combo_calculate_post(timeout=timeout, net_loyalty_result_calculate_combo_price_request=net_loyalty_result_calculate_combo_price_request)

Calculate combo price

Make combo price calculation.

 > Restriction group: `Loyalty: order calculate`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.net_loyalty_result_calculate_combo_price_request import NetLoyaltyResultCalculateComboPriceRequest
from iikocloud_client.models.net_loyalty_result_calculate_combo_price_response import NetLoyaltyResultCalculateComboPriceResponse
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
    api_instance = iikocloud_client.MenuApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_loyalty_result_calculate_combo_price_request = iikocloud_client.NetLoyaltyResultCalculateComboPriceRequest() # NetLoyaltyResultCalculateComboPriceRequest |  (optional)

    try:
        # Calculate combo price
        api_response = await api_instance.combo_calculate_post(timeout=timeout, net_loyalty_result_calculate_combo_price_request=net_loyalty_result_calculate_combo_price_request)
        print("The response of MenuApi->combo_calculate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->combo_calculate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_loyalty_result_calculate_combo_price_request** | [**NetLoyaltyResultCalculateComboPriceRequest**](NetLoyaltyResultCalculateComboPriceRequest.md)|  | [optional] 

### Return type

[**NetLoyaltyResultCalculateComboPriceResponse**](NetLoyaltyResultCalculateComboPriceResponse.md)

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

# **combo_post**
> NetLoyaltyResultGetCombosInfoResponse combo_post(timeout=timeout, net_loyalty_result_get_combos_info_request=net_loyalty_result_get_combos_info_request)

Get combos info

Get all organization's combos.

 > Restriction group: `Data: menu`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.net_loyalty_result_get_combos_info_request import NetLoyaltyResultGetCombosInfoRequest
from iikocloud_client.models.net_loyalty_result_get_combos_info_response import NetLoyaltyResultGetCombosInfoResponse
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
    api_instance = iikocloud_client.MenuApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_loyalty_result_get_combos_info_request = iikocloud_client.NetLoyaltyResultGetCombosInfoRequest() # NetLoyaltyResultGetCombosInfoRequest |  (optional)

    try:
        # Get combos info
        api_response = await api_instance.combo_post(timeout=timeout, net_loyalty_result_get_combos_info_request=net_loyalty_result_get_combos_info_request)
        print("The response of MenuApi->combo_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->combo_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_loyalty_result_get_combos_info_request** | [**NetLoyaltyResultGetCombosInfoRequest**](NetLoyaltyResultGetCombosInfoRequest.md)|  | [optional] 

### Return type

[**NetLoyaltyResultGetCombosInfoResponse**](NetLoyaltyResultGetCombosInfoResponse.md)

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

# **menu_by_id_post**
> ExternalMenuPreset menu_by_id_post(timeout=timeout, transport_nomenclature_menu_request=transport_nomenclature_menu_request)

Retrieve external menu by ID.

> Sourced from Web External menu.

 > Restriction group: `Data: menu`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.external_menu_preset import ExternalMenuPreset
from iikocloud_client.models.transport_nomenclature_menu_request import TransportNomenclatureMenuRequest
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
    api_instance = iikocloud_client.MenuApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_nomenclature_menu_request = iikocloud_client.TransportNomenclatureMenuRequest() # TransportNomenclatureMenuRequest |  (optional)

    try:
        # Retrieve external menu by ID.
        api_response = await api_instance.menu_by_id_post(timeout=timeout, transport_nomenclature_menu_request=transport_nomenclature_menu_request)
        print("The response of MenuApi->menu_by_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->menu_by_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_nomenclature_menu_request** | [**TransportNomenclatureMenuRequest**](TransportNomenclatureMenuRequest.md)|  | [optional] 

### Return type

[**ExternalMenuPreset**](ExternalMenuPreset.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Server Error |  -  |
**408** | Request Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **menu_post**
> TransportNomenclatureMenusDataResponse menu_post(timeout=timeout)

External menus with price categories.



 > Restriction group: `Data: menu`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_nomenclature_menus_data_response import TransportNomenclatureMenusDataResponse
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
    api_instance = iikocloud_client.MenuApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)

    try:
        # External menus with price categories.
        api_response = await api_instance.menu_post(timeout=timeout)
        print("The response of MenuApi->menu_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->menu_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]

### Return type

[**TransportNomenclatureMenusDataResponse**](TransportNomenclatureMenusDataResponse.md)

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

# **nomenclature_post**
> TransportNomenclatureNomenclatureResponse nomenclature_post(timeout=timeout, transport_nomenclature_nomenclature_request=transport_nomenclature_nomenclature_request)

Menu.

> Sourced from RMS Data Exchange Export menu.

 > Restriction group: `Data: menu`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_nomenclature_nomenclature_request import TransportNomenclatureNomenclatureRequest
from iikocloud_client.models.transport_nomenclature_nomenclature_response import TransportNomenclatureNomenclatureResponse
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
    api_instance = iikocloud_client.MenuApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_nomenclature_nomenclature_request = iikocloud_client.TransportNomenclatureNomenclatureRequest() # TransportNomenclatureNomenclatureRequest |  (optional)

    try:
        # Menu.
        api_response = await api_instance.nomenclature_post(timeout=timeout, transport_nomenclature_nomenclature_request=transport_nomenclature_nomenclature_request)
        print("The response of MenuApi->nomenclature_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->nomenclature_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_nomenclature_nomenclature_request** | [**TransportNomenclatureNomenclatureRequest**](TransportNomenclatureNomenclatureRequest.md)|  | [optional] 

### Return type

[**TransportNomenclatureNomenclatureResponse**](TransportNomenclatureNomenclatureResponse.md)

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

# **stop_lists_add_post**
> TransportCommonCorrelationIdResponse stop_lists_add_post(timeout=timeout, transport_stop_lists_add_products_to_stop_list_request=transport_stop_lists_add_products_to_stop_list_request)

Add items to out-of-stock list.  (You should have extra rights to use this method).



 > Allowed from version `8.6.1`.

 > Restriction group: `Data: changing stoplists`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_stop_lists_add_products_to_stop_list_request import TransportStopListsAddProductsToStopListRequest
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
    api_instance = iikocloud_client.MenuApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_stop_lists_add_products_to_stop_list_request = iikocloud_client.TransportStopListsAddProductsToStopListRequest() # TransportStopListsAddProductsToStopListRequest |  (optional)

    try:
        # Add items to out-of-stock list.  (You should have extra rights to use this method).
        api_response = await api_instance.stop_lists_add_post(timeout=timeout, transport_stop_lists_add_products_to_stop_list_request=transport_stop_lists_add_products_to_stop_list_request)
        print("The response of MenuApi->stop_lists_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->stop_lists_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_stop_lists_add_products_to_stop_list_request** | [**TransportStopListsAddProductsToStopListRequest**](TransportStopListsAddProductsToStopListRequest.md)|  | [optional] 

### Return type

[**TransportCommonCorrelationIdResponse**](TransportCommonCorrelationIdResponse.md)

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

# **stop_lists_check_post**
> TransportStopListsCheckStopListResponse stop_lists_check_post(timeout=timeout, transport_stop_lists_check_stop_list_request=transport_stop_lists_check_stop_list_request)

Check items in out-of-stock list.



 > Restriction group: `Orders: creating`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_stop_lists_check_stop_list_request import TransportStopListsCheckStopListRequest
from iikocloud_client.models.transport_stop_lists_check_stop_list_response import TransportStopListsCheckStopListResponse
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
    api_instance = iikocloud_client.MenuApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_stop_lists_check_stop_list_request = iikocloud_client.TransportStopListsCheckStopListRequest() # TransportStopListsCheckStopListRequest |  (optional)

    try:
        # Check items in out-of-stock list.
        api_response = await api_instance.stop_lists_check_post(timeout=timeout, transport_stop_lists_check_stop_list_request=transport_stop_lists_check_stop_list_request)
        print("The response of MenuApi->stop_lists_check_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->stop_lists_check_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_stop_lists_check_stop_list_request** | [**TransportStopListsCheckStopListRequest**](TransportStopListsCheckStopListRequest.md)|  | [optional] 

### Return type

[**TransportStopListsCheckStopListResponse**](TransportStopListsCheckStopListResponse.md)

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

# **stop_lists_clear_post**
> TransportCommonCorrelationIdResponse stop_lists_clear_post(timeout=timeout, transport_stop_lists_clear_stop_list_request=transport_stop_lists_clear_stop_list_request)

Clear out-of-stock list.  (You should have extra rights to use this method).



 > Allowed from version `8.6.1`.

 > Restriction group: `Data: changing stoplists`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_stop_lists_clear_stop_list_request import TransportStopListsClearStopListRequest
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
    api_instance = iikocloud_client.MenuApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_stop_lists_clear_stop_list_request = iikocloud_client.TransportStopListsClearStopListRequest() # TransportStopListsClearStopListRequest |  (optional)

    try:
        # Clear out-of-stock list.  (You should have extra rights to use this method).
        api_response = await api_instance.stop_lists_clear_post(timeout=timeout, transport_stop_lists_clear_stop_list_request=transport_stop_lists_clear_stop_list_request)
        print("The response of MenuApi->stop_lists_clear_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->stop_lists_clear_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_stop_lists_clear_stop_list_request** | [**TransportStopListsClearStopListRequest**](TransportStopListsClearStopListRequest.md)|  | [optional] 

### Return type

[**TransportCommonCorrelationIdResponse**](TransportCommonCorrelationIdResponse.md)

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

# **stop_lists_post**
> TransportStopListsStopListsResponse stop_lists_post(timeout=timeout, transport_stop_lists_stop_lists_request=transport_stop_lists_stop_lists_request)

Out-of-stock items.



 > Restriction group: `Data: stoplists`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_stop_lists_stop_lists_request import TransportStopListsStopListsRequest
from iikocloud_client.models.transport_stop_lists_stop_lists_response import TransportStopListsStopListsResponse
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
    api_instance = iikocloud_client.MenuApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_stop_lists_stop_lists_request = iikocloud_client.TransportStopListsStopListsRequest() # TransportStopListsStopListsRequest |  (optional)

    try:
        # Out-of-stock items.
        api_response = await api_instance.stop_lists_post(timeout=timeout, transport_stop_lists_stop_lists_request=transport_stop_lists_stop_lists_request)
        print("The response of MenuApi->stop_lists_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->stop_lists_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_stop_lists_stop_lists_request** | [**TransportStopListsStopListsRequest**](TransportStopListsStopListsRequest.md)|  | [optional] 

### Return type

[**TransportStopListsStopListsResponse**](TransportStopListsStopListsResponse.md)

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

# **stop_lists_remove_post**
> TransportCommonCorrelationIdResponse stop_lists_remove_post(timeout=timeout, transport_stop_lists_remove_products_from_stop_list_request=transport_stop_lists_remove_products_from_stop_list_request)

Remove items from out-of-stock list.  (You should have extra rights to use this method).



 > Allowed from version `8.6.1`.

 > Restriction group: `Data: changing stoplists`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_stop_lists_remove_products_from_stop_list_request import TransportStopListsRemoveProductsFromStopListRequest
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
    api_instance = iikocloud_client.MenuApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_stop_lists_remove_products_from_stop_list_request = iikocloud_client.TransportStopListsRemoveProductsFromStopListRequest() # TransportStopListsRemoveProductsFromStopListRequest |  (optional)

    try:
        # Remove items from out-of-stock list.  (You should have extra rights to use this method).
        api_response = await api_instance.stop_lists_remove_post(timeout=timeout, transport_stop_lists_remove_products_from_stop_list_request=transport_stop_lists_remove_products_from_stop_list_request)
        print("The response of MenuApi->stop_lists_remove_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->stop_lists_remove_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_stop_lists_remove_products_from_stop_list_request** | [**TransportStopListsRemoveProductsFromStopListRequest**](TransportStopListsRemoveProductsFromStopListRequest.md)|  | [optional] 

### Return type

[**TransportCommonCorrelationIdResponse**](TransportCommonCorrelationIdResponse.md)

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

