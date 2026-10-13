# iikocloud_client.NomenclatureAssemblyChartApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_nomenclature_assembly_chart**](NomenclatureAssemblyChartApi.md#create_nomenclature_assembly_chart) | **POST** /api/nomenclature/v1/assembly-chart/create | Create an assembly chart
[**create_nomenclature_assembly_chart_v2**](NomenclatureAssemblyChartApi.md#create_nomenclature_assembly_chart_v2) | **POST** /api/nomenclature/v2/assembly-chart/create | Create an assembly chart (v2)
[**create_nomenclature_assembly_chart_v3**](NomenclatureAssemblyChartApi.md#create_nomenclature_assembly_chart_v3) | **POST** /api/nomenclature/v3/assembly-chart/create | Create an assembly chart (v3)
[**delete_nomenclature_assembly_chart**](NomenclatureAssemblyChartApi.md#delete_nomenclature_assembly_chart) | **POST** /api/nomenclature/v1/assembly-chart/delete | Delete an assembly chart
[**delete_nomenclature_assembly_chart_v2**](NomenclatureAssemblyChartApi.md#delete_nomenclature_assembly_chart_v2) | **POST** /api/nomenclature/v2/assembly-chart/delete | Delete an assembly chart (v2)
[**delete_nomenclature_assembly_chart_v3**](NomenclatureAssemblyChartApi.md#delete_nomenclature_assembly_chart_v3) | **POST** /api/nomenclature/v3/assembly-chart/delete | Delete an assembly chart (v3)
[**get_nomenclature_assembled_chart_v2**](NomenclatureAssemblyChartApi.md#get_nomenclature_assembled_chart_v2) | **POST** /api/nomenclature/v2/assembly-chart/assembled | Get an assembled chart
[**get_nomenclature_assembly_chart**](NomenclatureAssemblyChartApi.md#get_nomenclature_assembly_chart) | **POST** /api/nomenclature/v1/assembly-chart/get | Get an assembly chart by ID
[**get_nomenclature_assembly_chart_tree_v2**](NomenclatureAssemblyChartApi.md#get_nomenclature_assembly_chart_tree_v2) | **POST** /api/nomenclature/v2/assembly-chart/tree | Get an assembly chart tree
[**get_nomenclature_assembly_chart_v2**](NomenclatureAssemblyChartApi.md#get_nomenclature_assembly_chart_v2) | **POST** /api/nomenclature/v2/assembly-chart/get | Get an assembly chart by ID (v2)
[**get_nomenclature_assembly_chart_v3**](NomenclatureAssemblyChartApi.md#get_nomenclature_assembly_chart_v3) | **POST** /api/nomenclature/v3/assembly-chart/get | Get an assembly chart by ID (v3)
[**get_nomenclature_prepared_chart_v2**](NomenclatureAssemblyChartApi.md#get_nomenclature_prepared_chart_v2) | **POST** /api/nomenclature/v2/assembly-chart/prepared | Get a prepared chart (breakdown to store items)
[**list_nomenclature_assembly_charts**](NomenclatureAssemblyChartApi.md#list_nomenclature_assembly_charts) | **POST** /api/nomenclature/v1/assembly-chart/list | Get a list of assembly charts by product
[**list_nomenclature_assembly_charts_v2**](NomenclatureAssemblyChartApi.md#list_nomenclature_assembly_charts_v2) | **POST** /api/nomenclature/v2/assembly-chart/list | Get a list of assembly charts by product (v2)
[**list_nomenclature_assembly_charts_v3**](NomenclatureAssemblyChartApi.md#list_nomenclature_assembly_charts_v3) | **POST** /api/nomenclature/v3/assembly-chart/list | Get a list of assembly charts (v3)
[**resolve_nomenclature_assembly_chart_v3**](NomenclatureAssemblyChartApi.md#resolve_nomenclature_assembly_chart_v3) | **POST** /api/nomenclature/v3/assembly-chart/resolve | Resolve an assembly chart representation
[**update_nomenclature_assembly_chart**](NomenclatureAssemblyChartApi.md#update_nomenclature_assembly_chart) | **POST** /api/nomenclature/v1/assembly-chart/update | Update an assembly chart
[**update_nomenclature_assembly_chart_v2**](NomenclatureAssemblyChartApi.md#update_nomenclature_assembly_chart_v2) | **POST** /api/nomenclature/v2/assembly-chart/update | Update an assembly chart (v2)
[**update_nomenclature_assembly_chart_v3**](NomenclatureAssemblyChartApi.md#update_nomenclature_assembly_chart_v3) | **POST** /api/nomenclature/v3/assembly-chart/update | Update an assembly chart (v3)


# **create_nomenclature_assembly_chart**
> AssemblyChartCommonResponse create_nomenclature_assembly_chart(create_request, timeout=timeout)

Create an assembly chart

Saves a new assembly chart for a product.
If the product was created recently and has not yet appeared in the nomenclature list (eventual consistency), the method may fail with a 502 error. Wait until the product appears in the nomenclature list before creating an assembly chart for it.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_common_response import AssemblyChartCommonResponse
from iikocloud_client.models.create_request import CreateRequest
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    create_request = iikocloud_client.CreateRequest() # CreateRequest | Request body for creating an assembly chart
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Create an assembly chart
        api_response = await api_instance.create_nomenclature_assembly_chart(create_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->create_nomenclature_assembly_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->create_nomenclature_assembly_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_request** | [**CreateRequest**](CreateRequest.md)| Request body for creating an assembly chart | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartCommonResponse**](AssemblyChartCommonResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Assembly chart created successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nomenclature_assembly_chart_v2**
> AssemblyChartCommonResponse create_nomenclature_assembly_chart_v2(create_request, timeout=timeout)

Create an assembly chart (v2)

Saves a new assembly chart for a product.
If the product was created recently and has not yet appeared in the nomenclature list (eventual consistency), the method may fail with a 502 error. Wait until the product appears in the nomenclature list before creating an assembly chart for it.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_common_response import AssemblyChartCommonResponse
from iikocloud_client.models.create_request import CreateRequest
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    create_request = iikocloud_client.CreateRequest() # CreateRequest | Request body for creating an assembly chart
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Create an assembly chart (v2)
        api_response = await api_instance.create_nomenclature_assembly_chart_v2(create_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->create_nomenclature_assembly_chart_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->create_nomenclature_assembly_chart_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_request** | [**CreateRequest**](CreateRequest.md)| Request body for creating an assembly chart | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartCommonResponse**](AssemblyChartCommonResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Assembly chart created successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nomenclature_assembly_chart_v3**
> AssemblyChartCommonResponseV3 create_nomenclature_assembly_chart_v3(create_request_v3, timeout=timeout)

Create an assembly chart (v3)

Saves a new assembly chart for a product.
If the product was created recently and has not yet appeared in the nomenclature list (eventual consistency), the method may fail with a 502 error. Wait until the product appears in the nomenclature list before creating an assembly chart for it.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_common_response_v3 import AssemblyChartCommonResponseV3
from iikocloud_client.models.create_request_v3 import CreateRequestV3
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    create_request_v3 = iikocloud_client.CreateRequestV3() # CreateRequestV3 | Request body for creating an assembly chart
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Create an assembly chart (v3)
        api_response = await api_instance.create_nomenclature_assembly_chart_v3(create_request_v3, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->create_nomenclature_assembly_chart_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->create_nomenclature_assembly_chart_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_request_v3** | [**CreateRequestV3**](CreateRequestV3.md)| Request body for creating an assembly chart | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartCommonResponseV3**](AssemblyChartCommonResponseV3.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Assembly chart created successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nomenclature_assembly_chart**
> AssemblyChartCommonResponse delete_nomenclature_assembly_chart(delete_request, timeout=timeout)

Delete an assembly chart

Deletes an assembly chart by UUID.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_common_response import AssemblyChartCommonResponse
from iikocloud_client.models.delete_request import DeleteRequest
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    delete_request = iikocloud_client.DeleteRequest() # DeleteRequest | Request body for deleting an assembly chart
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Delete an assembly chart
        api_response = await api_instance.delete_nomenclature_assembly_chart(delete_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->delete_nomenclature_assembly_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->delete_nomenclature_assembly_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_request** | [**DeleteRequest**](DeleteRequest.md)| Request body for deleting an assembly chart | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartCommonResponse**](AssemblyChartCommonResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assembly chart deleted successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nomenclature_assembly_chart_v2**
> AssemblyChartCommonResponse delete_nomenclature_assembly_chart_v2(delete_request, timeout=timeout)

Delete an assembly chart (v2)

Deletes an assembly chart by UUID.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_common_response import AssemblyChartCommonResponse
from iikocloud_client.models.delete_request import DeleteRequest
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    delete_request = iikocloud_client.DeleteRequest() # DeleteRequest | Request body for deleting an assembly chart
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Delete an assembly chart (v2)
        api_response = await api_instance.delete_nomenclature_assembly_chart_v2(delete_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->delete_nomenclature_assembly_chart_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->delete_nomenclature_assembly_chart_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_request** | [**DeleteRequest**](DeleteRequest.md)| Request body for deleting an assembly chart | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartCommonResponse**](AssemblyChartCommonResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assembly chart deleted successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nomenclature_assembly_chart_v3**
> AssemblyChartCommonResponseV3 delete_nomenclature_assembly_chart_v3(delete_request_v3, timeout=timeout)

Delete an assembly chart (v3)

Deletes an assembly chart by UUID.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_common_response_v3 import AssemblyChartCommonResponseV3
from iikocloud_client.models.delete_request_v3 import DeleteRequestV3
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    delete_request_v3 = iikocloud_client.DeleteRequestV3() # DeleteRequestV3 | Request body for deleting an assembly chart
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Delete an assembly chart (v3)
        api_response = await api_instance.delete_nomenclature_assembly_chart_v3(delete_request_v3, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->delete_nomenclature_assembly_chart_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->delete_nomenclature_assembly_chart_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_request_v3** | [**DeleteRequestV3**](DeleteRequestV3.md)| Request body for deleting an assembly chart | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartCommonResponseV3**](AssemblyChartCommonResponseV3.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assembly chart deleted successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nomenclature_assembled_chart_v2**
> AssemblyChartResponse get_nomenclature_assembled_chart_v2(assembled_request, timeout=timeout)

Get an assembled chart

Returns the top-level assembly chart (without resolving nested ingredient charts) effective for
the product on the given date. If no chart is found, returns 200 with an empty body.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembled_request import AssembledRequest
from iikocloud_client.models.assembly_chart_response import AssemblyChartResponse
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    assembled_request = iikocloud_client.AssembledRequest() # AssembledRequest | Request body for getting an assembled chart
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get an assembled chart
        api_response = await api_instance.get_nomenclature_assembled_chart_v2(assembled_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->get_nomenclature_assembled_chart_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->get_nomenclature_assembled_chart_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assembled_request** | [**AssembledRequest**](AssembledRequest.md)| Request body for getting an assembled chart | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartResponse**](AssemblyChartResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assembled assembly chart |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nomenclature_assembly_chart**
> AssemblyChartResponse get_nomenclature_assembly_chart(get_request, timeout=timeout)

Get an assembly chart by ID

Returns a single assembly chart by its UUID.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_response import AssemblyChartResponse
from iikocloud_client.models.get_request import GetRequest
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    get_request = iikocloud_client.GetRequest() # GetRequest | Request body for getting an assembly chart by ID
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get an assembly chart by ID
        api_response = await api_instance.get_nomenclature_assembly_chart(get_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->get_nomenclature_assembly_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->get_nomenclature_assembly_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_request** | [**GetRequest**](GetRequest.md)| Request body for getting an assembly chart by ID | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartResponse**](AssemblyChartResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assembly chart |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nomenclature_assembly_chart_tree_v2**
> ChartTreeNodeDto get_nomenclature_assembly_chart_tree_v2(tree_request, timeout=timeout)

Get an assembly chart tree

Returns the assembly chart tree of the product for the given date: for every ingredient that has
its own assembly chart, its composition is recursively resolved. If no chart is found, returns 200
with an empty body.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.chart_tree_node_dto import ChartTreeNodeDto
from iikocloud_client.models.tree_request import TreeRequest
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    tree_request = iikocloud_client.TreeRequest() # TreeRequest | Request body for getting an assembly chart tree
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get an assembly chart tree
        api_response = await api_instance.get_nomenclature_assembly_chart_tree_v2(tree_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->get_nomenclature_assembly_chart_tree_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->get_nomenclature_assembly_chart_tree_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tree_request** | [**TreeRequest**](TreeRequest.md)| Request body for getting an assembly chart tree | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**ChartTreeNodeDto**](ChartTreeNodeDto.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assembly chart tree |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nomenclature_assembly_chart_v2**
> AssemblyChartResponse get_nomenclature_assembly_chart_v2(get_request, timeout=timeout)

Get an assembly chart by ID (v2)

Returns a single assembly chart by its UUID.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_response import AssemblyChartResponse
from iikocloud_client.models.get_request import GetRequest
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    get_request = iikocloud_client.GetRequest() # GetRequest | Request body for getting an assembly chart by ID
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get an assembly chart by ID (v2)
        api_response = await api_instance.get_nomenclature_assembly_chart_v2(get_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->get_nomenclature_assembly_chart_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->get_nomenclature_assembly_chart_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_request** | [**GetRequest**](GetRequest.md)| Request body for getting an assembly chart by ID | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartResponse**](AssemblyChartResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assembly chart |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nomenclature_assembly_chart_v3**
> AssemblyChartResponseV3 get_nomenclature_assembly_chart_v3(get_request_v3, timeout=timeout)

Get an assembly chart by ID (v3)

Returns a single assembly chart by its UUID.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_response_v3 import AssemblyChartResponseV3
from iikocloud_client.models.get_request_v3 import GetRequestV3
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    get_request_v3 = iikocloud_client.GetRequestV3() # GetRequestV3 | Request body for getting an assembly chart by ID
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get an assembly chart by ID (v3)
        api_response = await api_instance.get_nomenclature_assembly_chart_v3(get_request_v3, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->get_nomenclature_assembly_chart_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->get_nomenclature_assembly_chart_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_request_v3** | [**GetRequestV3**](GetRequestV3.md)| Request body for getting an assembly chart by ID | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartResponseV3**](AssemblyChartResponseV3.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assembly chart |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nomenclature_prepared_chart_v2**
> PreparedChartDto get_nomenclature_prepared_chart_v2(prepared_request, timeout=timeout)

Get a prepared chart (breakdown to store items)

Returns the recipe breakdown of the product down to elementary store items (ingredients written
off from stock) for the given date. If no chart is found, returns 200 with an empty body.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.prepared_chart_dto import PreparedChartDto
from iikocloud_client.models.prepared_request import PreparedRequest
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    prepared_request = iikocloud_client.PreparedRequest() # PreparedRequest | Request body for getting a prepared chart
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a prepared chart (breakdown to store items)
        api_response = await api_instance.get_nomenclature_prepared_chart_v2(prepared_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->get_nomenclature_prepared_chart_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->get_nomenclature_prepared_chart_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prepared_request** | [**PreparedRequest**](PreparedRequest.md)| Request body for getting a prepared chart | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**PreparedChartDto**](PreparedChartDto.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Prepared chart (breakdown to store items) |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nomenclature_assembly_charts**
> ListResponse list_nomenclature_assembly_charts(list_request, timeout=timeout)

Get a list of assembly charts by product

Returns the history of assembly charts for a product.
The filter `product eq` is required. The optional `department eq` filter restricts results to a specific department.
Pagination (limit / offset) is applied client-side.
Data is returned from an asynchronously updated snapshot (eventual consistency): recently created or modified assembly charts may be missing from the response for a short time.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.list_request import ListRequest
from iikocloud_client.models.list_response import ListResponse
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    list_request = iikocloud_client.ListRequest() # ListRequest | Parameters for the assembly chart list request
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of assembly charts by product
        api_response = await api_instance.list_nomenclature_assembly_charts(list_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->list_nomenclature_assembly_charts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->list_nomenclature_assembly_charts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_request** | [**ListRequest**](ListRequest.md)| Parameters for the assembly chart list request | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**ListResponse**](ListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of assembly charts |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nomenclature_assembly_charts_v2**
> AssemblyChartListResponse list_nomenclature_assembly_charts_v2(assembly_chart_list_request, timeout=timeout)

Get a list of assembly charts by product (v2)

Returns the history of assembly charts for a product.
The filter `product eq` is required. The optional `department eq` filter restricts results to a specific department.
Pagination (limit / offset) is applied client-side.
Data is returned from an asynchronously updated snapshot (eventual consistency): recently created or modified assembly charts may be missing from the response for a short time.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_list_request import AssemblyChartListRequest
from iikocloud_client.models.assembly_chart_list_response import AssemblyChartListResponse
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    assembly_chart_list_request = iikocloud_client.AssemblyChartListRequest() # AssemblyChartListRequest | Parameters for the assembly chart list request
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of assembly charts by product (v2)
        api_response = await api_instance.list_nomenclature_assembly_charts_v2(assembly_chart_list_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->list_nomenclature_assembly_charts_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->list_nomenclature_assembly_charts_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assembly_chart_list_request** | [**AssemblyChartListRequest**](AssemblyChartListRequest.md)| Parameters for the assembly chart list request | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartListResponse**](AssemblyChartListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of assembly charts |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nomenclature_assembly_charts_v3**
> AssemblyChartListResponseV3 list_nomenclature_assembly_charts_v3(assembly_chart_list_request_v3, timeout=timeout)

Get a list of assembly charts (v3)

Returns assembly charts in one of three modes derived from the request parameters:
a `product` filter is set — the product's chart history; `knownRevision` is set — only the changes since that revision; otherwise — all charts for the period.
Data is returned from an asynchronously updated snapshot (eventual consistency): recently created or modified assembly charts may be missing from the response for a short time.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_list_request_v3 import AssemblyChartListRequestV3
from iikocloud_client.models.assembly_chart_list_response_v3 import AssemblyChartListResponseV3
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    assembly_chart_list_request_v3 = iikocloud_client.AssemblyChartListRequestV3() # AssemblyChartListRequestV3 | Parameters for the assembly chart list request
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of assembly charts (v3)
        api_response = await api_instance.list_nomenclature_assembly_charts_v3(assembly_chart_list_request_v3, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->list_nomenclature_assembly_charts_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->list_nomenclature_assembly_charts_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assembly_chart_list_request_v3** | [**AssemblyChartListRequestV3**](AssemblyChartListRequestV3.md)| Parameters for the assembly chart list request | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartListResponseV3**](AssemblyChartListResponseV3.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of assembly charts |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_nomenclature_assembly_chart_v3**
> ResolveResponseV3 resolve_nomenclature_assembly_chart_v3(resolve_request_v3, timeout=timeout)

Resolve an assembly chart representation

Returns a computed representation of the product's assembly chart for the given date.
The representation is selected by `view`: assembled — the top-level chart (without resolving nested
ingredient charts); prepared — the breakdown down to elementary store items (ingredients written off
from stock); tree — the recipe tree, where every ingredient with its own assembly chart is recursively
expanded. If there is no chart for the date, returns 200 with an empty representation; if the product
is not found, returns 404.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.resolve_request_v3 import ResolveRequestV3
from iikocloud_client.models.resolve_response_v3 import ResolveResponseV3
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    resolve_request_v3 = iikocloud_client.ResolveRequestV3() # ResolveRequestV3 | Request body for resolving an assembly chart representation
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Resolve an assembly chart representation
        api_response = await api_instance.resolve_nomenclature_assembly_chart_v3(resolve_request_v3, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->resolve_nomenclature_assembly_chart_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->resolve_nomenclature_assembly_chart_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resolve_request_v3** | [**ResolveRequestV3**](ResolveRequestV3.md)| Request body for resolving an assembly chart representation | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**ResolveResponseV3**](ResolveResponseV3.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Computed assembly chart representation |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**404** | Not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nomenclature_assembly_chart**
> AssemblyChartCommonResponse update_nomenclature_assembly_chart(assembly_chart_v1_save_request, timeout=timeout)

Update an assembly chart

Updates an existing assembly chart.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_common_response import AssemblyChartCommonResponse
from iikocloud_client.models.assembly_chart_v1_save_request import AssemblyChartV1SaveRequest
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    assembly_chart_v1_save_request = iikocloud_client.AssemblyChartV1SaveRequest() # AssemblyChartV1SaveRequest | Request body for updating an assembly chart
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Update an assembly chart
        api_response = await api_instance.update_nomenclature_assembly_chart(assembly_chart_v1_save_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->update_nomenclature_assembly_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->update_nomenclature_assembly_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assembly_chart_v1_save_request** | [**AssemblyChartV1SaveRequest**](AssemblyChartV1SaveRequest.md)| Request body for updating an assembly chart | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartCommonResponse**](AssemblyChartCommonResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assembly chart updated successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nomenclature_assembly_chart_v2**
> AssemblyChartCommonResponse update_nomenclature_assembly_chart_v2(assembly_chart_v2_save_request, timeout=timeout)

Update an assembly chart (v2)

Updates an existing assembly chart.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_common_response import AssemblyChartCommonResponse
from iikocloud_client.models.assembly_chart_v2_save_request import AssemblyChartV2SaveRequest
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    assembly_chart_v2_save_request = iikocloud_client.AssemblyChartV2SaveRequest() # AssemblyChartV2SaveRequest | Request body for updating an assembly chart
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Update an assembly chart (v2)
        api_response = await api_instance.update_nomenclature_assembly_chart_v2(assembly_chart_v2_save_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->update_nomenclature_assembly_chart_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->update_nomenclature_assembly_chart_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assembly_chart_v2_save_request** | [**AssemblyChartV2SaveRequest**](AssemblyChartV2SaveRequest.md)| Request body for updating an assembly chart | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartCommonResponse**](AssemblyChartCommonResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assembly chart updated successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nomenclature_assembly_chart_v3**
> AssemblyChartCommonResponseV3 update_nomenclature_assembly_chart_v3(assembly_chart_v3_save_request, timeout=timeout)

Update an assembly chart (v3)

Updates an existing assembly chart.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.assembly_chart_common_response_v3 import AssemblyChartCommonResponseV3
from iikocloud_client.models.assembly_chart_v3_save_request import AssemblyChartV3SaveRequest
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
    api_instance = iikocloud_client.NomenclatureAssemblyChartApi(api_client)
    assembly_chart_v3_save_request = iikocloud_client.AssemblyChartV3SaveRequest() # AssemblyChartV3SaveRequest | Request body for updating an assembly chart
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Update an assembly chart (v3)
        api_response = await api_instance.update_nomenclature_assembly_chart_v3(assembly_chart_v3_save_request, timeout=timeout)
        print("The response of NomenclatureAssemblyChartApi->update_nomenclature_assembly_chart_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureAssemblyChartApi->update_nomenclature_assembly_chart_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assembly_chart_v3_save_request** | [**AssemblyChartV3SaveRequest**](AssemblyChartV3SaveRequest.md)| Request body for updating an assembly chart | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AssemblyChartCommonResponseV3**](AssemblyChartCommonResponseV3.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assembly chart updated successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

