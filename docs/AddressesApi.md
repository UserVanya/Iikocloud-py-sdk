# iikocloud_client.AddressesApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cities_post**](AddressesApi.md#cities_post) | **POST** /cities | Cities.
[**regions_post**](AddressesApi.md#regions_post) | **POST** /regions | Regions.
[**streets_by_city_post**](AddressesApi.md#streets_by_city_post) | **POST** /streets/by_city | Streets by city.
[**streets_by_id_post**](AddressesApi.md#streets_by_id_post) | **POST** /streets/by_id | Streets by id or by classifierId.


# **cities_post**
> IikoTransportPublicApiContractsAddressCitiesResponse cities_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_address_cities_request=iiko_transport_public_api_contracts_address_cities_request)

Cities.



 > Restriction group: `Data: geo`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_address_cities_request import IikoTransportPublicApiContractsAddressCitiesRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_address_cities_response import IikoTransportPublicApiContractsAddressCitiesResponse
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
    api_instance = iikocloud_client.AddressesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_address_cities_request = iikocloud_client.IikoTransportPublicApiContractsAddressCitiesRequest() # IikoTransportPublicApiContractsAddressCitiesRequest |  (optional)

    try:
        # Cities.
        api_response = await api_instance.cities_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_address_cities_request=iiko_transport_public_api_contracts_address_cities_request)
        print("The response of AddressesApi->cities_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressesApi->cities_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_address_cities_request** | [**IikoTransportPublicApiContractsAddressCitiesRequest**](IikoTransportPublicApiContractsAddressCitiesRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsAddressCitiesResponse**](IikoTransportPublicApiContractsAddressCitiesResponse.md)

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

# **regions_post**
> IikoTransportPublicApiContractsAddressRegionsResponse regions_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_address_regions_request=iiko_transport_public_api_contracts_address_regions_request)

Regions.



 > Restriction group: `Data: geo`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_address_regions_request import IikoTransportPublicApiContractsAddressRegionsRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_address_regions_response import IikoTransportPublicApiContractsAddressRegionsResponse
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
    api_instance = iikocloud_client.AddressesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_address_regions_request = iikocloud_client.IikoTransportPublicApiContractsAddressRegionsRequest() # IikoTransportPublicApiContractsAddressRegionsRequest |  (optional)

    try:
        # Regions.
        api_response = await api_instance.regions_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_address_regions_request=iiko_transport_public_api_contracts_address_regions_request)
        print("The response of AddressesApi->regions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressesApi->regions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_address_regions_request** | [**IikoTransportPublicApiContractsAddressRegionsRequest**](IikoTransportPublicApiContractsAddressRegionsRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsAddressRegionsResponse**](IikoTransportPublicApiContractsAddressRegionsResponse.md)

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

# **streets_by_city_post**
> IikoTransportPublicApiContractsAddressStreetsResponse streets_by_city_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_address_streets_by_city_request=iiko_transport_public_api_contracts_address_streets_by_city_request)

Streets by city.



 > Restriction group: `Data: geo`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_address_streets_by_city_request import IikoTransportPublicApiContractsAddressStreetsByCityRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_address_streets_response import IikoTransportPublicApiContractsAddressStreetsResponse
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
    api_instance = iikocloud_client.AddressesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_address_streets_by_city_request = iikocloud_client.IikoTransportPublicApiContractsAddressStreetsByCityRequest() # IikoTransportPublicApiContractsAddressStreetsByCityRequest |  (optional)

    try:
        # Streets by city.
        api_response = await api_instance.streets_by_city_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_address_streets_by_city_request=iiko_transport_public_api_contracts_address_streets_by_city_request)
        print("The response of AddressesApi->streets_by_city_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressesApi->streets_by_city_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_address_streets_by_city_request** | [**IikoTransportPublicApiContractsAddressStreetsByCityRequest**](IikoTransportPublicApiContractsAddressStreetsByCityRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsAddressStreetsResponse**](IikoTransportPublicApiContractsAddressStreetsResponse.md)

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

# **streets_by_id_post**
> IikoTransportPublicApiContractsAddressStreetsByIdResponse streets_by_id_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_address_streets_by_id_request=iiko_transport_public_api_contracts_address_streets_by_id_request)

Streets by id or by classifierId.



 > Restriction group: `Data: geo`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_address_streets_by_id_request import IikoTransportPublicApiContractsAddressStreetsByIdRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_address_streets_by_id_response import IikoTransportPublicApiContractsAddressStreetsByIdResponse
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
    api_instance = iikocloud_client.AddressesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_address_streets_by_id_request = iikocloud_client.IikoTransportPublicApiContractsAddressStreetsByIdRequest() # IikoTransportPublicApiContractsAddressStreetsByIdRequest |  (optional)

    try:
        # Streets by id or by classifierId.
        api_response = await api_instance.streets_by_id_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_address_streets_by_id_request=iiko_transport_public_api_contracts_address_streets_by_id_request)
        print("The response of AddressesApi->streets_by_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressesApi->streets_by_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_address_streets_by_id_request** | [**IikoTransportPublicApiContractsAddressStreetsByIdRequest**](IikoTransportPublicApiContractsAddressStreetsByIdRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsAddressStreetsByIdResponse**](IikoTransportPublicApiContractsAddressStreetsByIdResponse.md)

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

