# iikocloud_client.MenuApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_products_to_stop_list**](MenuApi.md#add_products_to_stop_list) | **POST** /api/1/stop_lists/add | Add items to out-of-stock list.  (You should have extra rights to use this method).
[**calculate_combo_price**](MenuApi.md#calculate_combo_price) | **POST** /api/1/combo/calculate | Calculate combo price
[**check_products_in_stop_list**](MenuApi.md#check_products_in_stop_list) | **POST** /api/1/stop_lists/check | Check items in out-of-stock list.
[**clear_stop_list**](MenuApi.md#clear_stop_list) | **POST** /api/1/stop_lists/clear | Clear out-of-stock list.  (You should have extra rights to use this method).
[**get_combos_info**](MenuApi.md#get_combos_info) | **POST** /api/1/combo | Get combos info
[**get_external_menu_by_id**](MenuApi.md#get_external_menu_by_id) | **POST** /api/2/menu/by_id | Retrieve external menu by ID.
[**get_external_menus**](MenuApi.md#get_external_menus) | **POST** /api/2/menu | External menus with price categories.
[**get_nomenclature**](MenuApi.md#get_nomenclature) | **POST** /api/1/nomenclature | Menu.
[**get_stop_lists**](MenuApi.md#get_stop_lists) | **POST** /api/1/stop_lists | Out-of-stock items.
[**remove_products_from_stop_list**](MenuApi.md#remove_products_from_stop_list) | **POST** /api/1/stop_lists/remove | Remove items from out-of-stock list.  (You should have extra rights to use this method).


# **add_products_to_stop_list**
> CorrelationIdResponse add_products_to_stop_list(timeout=timeout, add_products_to_stop_list_request=add_products_to_stop_list_request)

Add items to out-of-stock list.  (You should have extra rights to use this method).



 > Allowed from version `8.6.1`.

 > Restriction group: `Data: changing stoplists`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.add_products_to_stop_list_request import AddProductsToStopListRequest
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
    api_instance = iikocloud_client.MenuApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    add_products_to_stop_list_request = iikocloud_client.AddProductsToStopListRequest() # AddProductsToStopListRequest |  (optional)

    try:
        # Add items to out-of-stock list.  (You should have extra rights to use this method).
        api_response = await api_instance.add_products_to_stop_list(timeout=timeout, add_products_to_stop_list_request=add_products_to_stop_list_request)
        print("The response of MenuApi->add_products_to_stop_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->add_products_to_stop_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **add_products_to_stop_list_request** | [**AddProductsToStopListRequest**](AddProductsToStopListRequest.md)|  | [optional] 

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

# **calculate_combo_price**
> CalculateComboPriceResponse calculate_combo_price(timeout=timeout, calculate_combo_price_request=calculate_combo_price_request)

Calculate combo price

Make combo price calculation.

 > Restriction group: `Loyalty: order calculate`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.calculate_combo_price_request import CalculateComboPriceRequest
from iikocloud_client.models.calculate_combo_price_response import CalculateComboPriceResponse
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
    api_instance = iikocloud_client.MenuApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    calculate_combo_price_request = iikocloud_client.CalculateComboPriceRequest() # CalculateComboPriceRequest |  (optional)

    try:
        # Calculate combo price
        api_response = await api_instance.calculate_combo_price(timeout=timeout, calculate_combo_price_request=calculate_combo_price_request)
        print("The response of MenuApi->calculate_combo_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->calculate_combo_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **calculate_combo_price_request** | [**CalculateComboPriceRequest**](CalculateComboPriceRequest.md)|  | [optional] 

### Return type

[**CalculateComboPriceResponse**](CalculateComboPriceResponse.md)

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

# **check_products_in_stop_list**
> CheckStopListResponse check_products_in_stop_list(timeout=timeout, check_stop_list_request=check_stop_list_request)

Check items in out-of-stock list.



 > Restriction group: `Orders: creating`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.check_stop_list_request import CheckStopListRequest
from iikocloud_client.models.check_stop_list_response import CheckStopListResponse
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
    api_instance = iikocloud_client.MenuApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    check_stop_list_request = iikocloud_client.CheckStopListRequest() # CheckStopListRequest |  (optional)

    try:
        # Check items in out-of-stock list.
        api_response = await api_instance.check_products_in_stop_list(timeout=timeout, check_stop_list_request=check_stop_list_request)
        print("The response of MenuApi->check_products_in_stop_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->check_products_in_stop_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **check_stop_list_request** | [**CheckStopListRequest**](CheckStopListRequest.md)|  | [optional] 

### Return type

[**CheckStopListResponse**](CheckStopListResponse.md)

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

# **clear_stop_list**
> CorrelationIdResponse clear_stop_list(timeout=timeout, clear_stop_list_request=clear_stop_list_request)

Clear out-of-stock list.  (You should have extra rights to use this method).



 > Allowed from version `8.6.1`.

 > Restriction group: `Data: changing stoplists`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.clear_stop_list_request import ClearStopListRequest
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
    api_instance = iikocloud_client.MenuApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    clear_stop_list_request = iikocloud_client.ClearStopListRequest() # ClearStopListRequest |  (optional)

    try:
        # Clear out-of-stock list.  (You should have extra rights to use this method).
        api_response = await api_instance.clear_stop_list(timeout=timeout, clear_stop_list_request=clear_stop_list_request)
        print("The response of MenuApi->clear_stop_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->clear_stop_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **clear_stop_list_request** | [**ClearStopListRequest**](ClearStopListRequest.md)|  | [optional] 

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

# **get_combos_info**
> GetCombosInfoResponse get_combos_info(timeout=timeout, get_combos_info_request=get_combos_info_request)

Get combos info

Get all organization's combos.

 > Restriction group: `Data: menu`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_combos_info_request import GetCombosInfoRequest
from iikocloud_client.models.get_combos_info_response import GetCombosInfoResponse
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
    api_instance = iikocloud_client.MenuApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_combos_info_request = iikocloud_client.GetCombosInfoRequest() # GetCombosInfoRequest |  (optional)

    try:
        # Get combos info
        api_response = await api_instance.get_combos_info(timeout=timeout, get_combos_info_request=get_combos_info_request)
        print("The response of MenuApi->get_combos_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->get_combos_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_combos_info_request** | [**GetCombosInfoRequest**](GetCombosInfoRequest.md)|  | [optional] 

### Return type

[**GetCombosInfoResponse**](GetCombosInfoResponse.md)

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

# **get_external_menu_by_id**
> ExternalMenuResponse get_external_menu_by_id(timeout=timeout, menu_request=menu_request)

Retrieve external menu by ID.

> Sourced from Web External menu.

 > Restriction group: `Data: menu`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.external_menu_response import ExternalMenuResponse
from iikocloud_client.models.menu_request import MenuRequest
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
    api_instance = iikocloud_client.MenuApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    menu_request = {"externalMenuId":"15#3","organizationIds":["706e5f4a-3efa-49f0-8f1c-15a6c1603e1f"],"priceCategoryId":"00000000-0000-0000-0000-000000000000","version":2} # MenuRequest |  (optional)

    try:
        # Retrieve external menu by ID.
        api_response = await api_instance.get_external_menu_by_id(timeout=timeout, menu_request=menu_request)
        print("The response of MenuApi->get_external_menu_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->get_external_menu_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **menu_request** | [**MenuRequest**](MenuRequest.md)|  | [optional] 

### Return type

[**ExternalMenuResponse**](ExternalMenuResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_menus**
> MenusDataResponse get_external_menus(timeout=timeout)

External menus with price categories.



 > Restriction group: `Data: menu`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.menus_data_response import MenusDataResponse
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
    api_instance = iikocloud_client.MenuApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)

    try:
        # External menus with price categories.
        api_response = await api_instance.get_external_menus(timeout=timeout)
        print("The response of MenuApi->get_external_menus:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->get_external_menus: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]

### Return type

[**MenusDataResponse**](MenusDataResponse.md)

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

# **get_nomenclature**
> NomenclatureResponse get_nomenclature(timeout=timeout, nomenclature_request=nomenclature_request)

Menu.

> Sourced from RMS Data Exchange Export menu.

 > Restriction group: `Data: menu`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_request import NomenclatureRequest
from iikocloud_client.models.nomenclature_response import NomenclatureResponse
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
    api_instance = iikocloud_client.MenuApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    nomenclature_request = iikocloud_client.NomenclatureRequest() # NomenclatureRequest |  (optional)

    try:
        # Menu.
        api_response = await api_instance.get_nomenclature(timeout=timeout, nomenclature_request=nomenclature_request)
        print("The response of MenuApi->get_nomenclature:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->get_nomenclature: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **nomenclature_request** | [**NomenclatureRequest**](NomenclatureRequest.md)|  | [optional] 

### Return type

[**NomenclatureResponse**](NomenclatureResponse.md)

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

# **get_stop_lists**
> StopListsResponse get_stop_lists(timeout=timeout, stop_lists_request=stop_lists_request)

Out-of-stock items.



 > Restriction group: `Data: stoplists`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.stop_lists_request import StopListsRequest
from iikocloud_client.models.stop_lists_response import StopListsResponse
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
    api_instance = iikocloud_client.MenuApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    stop_lists_request = iikocloud_client.StopListsRequest() # StopListsRequest |  (optional)

    try:
        # Out-of-stock items.
        api_response = await api_instance.get_stop_lists(timeout=timeout, stop_lists_request=stop_lists_request)
        print("The response of MenuApi->get_stop_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->get_stop_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **stop_lists_request** | [**StopListsRequest**](StopListsRequest.md)|  | [optional] 

### Return type

[**StopListsResponse**](StopListsResponse.md)

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

# **remove_products_from_stop_list**
> CorrelationIdResponse remove_products_from_stop_list(timeout=timeout, remove_products_from_stop_list_request=remove_products_from_stop_list_request)

Remove items from out-of-stock list.  (You should have extra rights to use this method).



 > Allowed from version `8.6.1`.

 > Restriction group: `Data: changing stoplists`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
from iikocloud_client.models.remove_products_from_stop_list_request import RemoveProductsFromStopListRequest
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
    api_instance = iikocloud_client.MenuApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    remove_products_from_stop_list_request = iikocloud_client.RemoveProductsFromStopListRequest() # RemoveProductsFromStopListRequest |  (optional)

    try:
        # Remove items from out-of-stock list.  (You should have extra rights to use this method).
        api_response = await api_instance.remove_products_from_stop_list(timeout=timeout, remove_products_from_stop_list_request=remove_products_from_stop_list_request)
        print("The response of MenuApi->remove_products_from_stop_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->remove_products_from_stop_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **remove_products_from_stop_list_request** | [**RemoveProductsFromStopListRequest**](RemoveProductsFromStopListRequest.md)|  | [optional] 

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

