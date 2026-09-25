# iikocloud_client.InventoryIncomingInventoryApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_inventory_incoming_inventory**](InventoryIncomingInventoryApi.md#cancel_inventory_incoming_inventory) | **POST** /api/inventory/v1/incoming_inventory/cancel | Cancel inventory draft
[**create_inventory_incoming_inventory**](InventoryIncomingInventoryApi.md#create_inventory_incoming_inventory) | **POST** /api/inventory/v1/incoming_inventory/create | Create inventory
[**get_inventory_incoming_inventory**](InventoryIncomingInventoryApi.md#get_inventory_incoming_inventory) | **POST** /api/inventory/v1/incoming_inventory/get | Get inventory
[**list_inventory_incoming_inventories**](InventoryIncomingInventoryApi.md#list_inventory_incoming_inventories) | **POST** /api/inventory/v1/incoming_inventory/list | Export inventories
[**post_inventory_incoming_inventory**](InventoryIncomingInventoryApi.md#post_inventory_incoming_inventory) | **POST** /api/inventory/v1/incoming_inventory/post | Post inventory
[**unpost_inventory_incoming_inventory**](InventoryIncomingInventoryApi.md#unpost_inventory_incoming_inventory) | **POST** /api/inventory/v1/incoming_inventory/unpost | Unpost inventory
[**update_inventory_incoming_inventory**](InventoryIncomingInventoryApi.md#update_inventory_incoming_inventory) | **POST** /api/inventory/v1/incoming_inventory/update | Edit inventory


# **cancel_inventory_incoming_inventory**
> IncomingInventorySaveResponse cancel_inventory_incoming_inventory(get_by_id_request, timeout=timeout)

Cancel inventory draft

Changes the inventory status from NEW to CANCELED

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.incoming_inventory_save_response import IncomingInventorySaveResponse
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
    api_instance = iikocloud_client.InventoryIncomingInventoryApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Cancel inventory draft
        api_response = await api_instance.cancel_inventory_incoming_inventory(get_by_id_request, timeout=timeout)
        print("The response of InventoryIncomingInventoryApi->cancel_inventory_incoming_inventory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingInventoryApi->cancel_inventory_incoming_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**IncomingInventorySaveResponse**](IncomingInventorySaveResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request (validation/invalid JSON) |  -  |
**401** | Unauthorized |  -  |
**405** | Method not allowed (POST expected) |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_inventory_incoming_inventory**
> IncomingInventorySaveResponse create_inventory_incoming_inventory(incoming_inventory_create_request, timeout=timeout)

Create inventory

Loads an inventory document: records the actual quantity of goods in the store and generates a variance report comparing the recorded and actual balances. It lets the restaurant automate stock reconciliation without manual entry: the integrator submits the actual quantity for each item, and the system compares it with the recorded balances and determines surpluses and shortages.

The document is created with the "Draft" status and does not affect balances until it is posted. To record the variances in accounting, post the document with a separate method (`post`); the draft can be edited (`update`) or canceled (`cancel`).

<b>Attention!</b> This method loads an already prepared (final) inventory document. The method does not break dishes and preparations down into ingredients: the integrator calculates the composition of the items independently using separate methods and submits the ready-made rows. If a dish is written off using the "Ingredients" method, all ingredients must be loaded manually according to the technical and technological card.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.incoming_inventory_create_request import IncomingInventoryCreateRequest
from iikocloud_client.models.incoming_inventory_save_response import IncomingInventorySaveResponse
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
    api_instance = iikocloud_client.InventoryIncomingInventoryApi(api_client)
    incoming_inventory_create_request = iikocloud_client.IncomingInventoryCreateRequest() # IncomingInventoryCreateRequest | Inventory creation parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Create inventory
        api_response = await api_instance.create_inventory_incoming_inventory(incoming_inventory_create_request, timeout=timeout)
        print("The response of InventoryIncomingInventoryApi->create_inventory_incoming_inventory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingInventoryApi->create_inventory_incoming_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incoming_inventory_create_request** | [**IncomingInventoryCreateRequest**](IncomingInventoryCreateRequest.md)| Inventory creation parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**IncomingInventorySaveResponse**](IncomingInventorySaveResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created |  -  |
**400** | Invalid request (validation/empty body/invalid JSON) |  -  |
**401** | Unauthorized |  -  |
**405** | Method not allowed (POST expected) |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_incoming_inventory**
> IncomingInventoryGetResponse get_inventory_incoming_inventory(get_by_id_request, timeout=timeout)

Get inventory

Gets an inventory document by identifier

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.incoming_inventory_get_response import IncomingInventoryGetResponse
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
    api_instance = iikocloud_client.InventoryIncomingInventoryApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Inventory request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get inventory
        api_response = await api_instance.get_inventory_incoming_inventory(get_by_id_request, timeout=timeout)
        print("The response of InventoryIncomingInventoryApi->get_inventory_incoming_inventory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingInventoryApi->get_inventory_incoming_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Inventory request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**IncomingInventoryGetResponse**](IncomingInventoryGetResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request (validation/invalid JSON) |  -  |
**401** | Unauthorized |  -  |
**405** | Method not allowed (POST expected) |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inventory_incoming_inventories**
> List[IncomingInventoryListItem] list_inventory_incoming_inventories(list_request, timeout=timeout)

Export inventories

Exports inventory documents for the specified period

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.incoming_inventory_list_item import IncomingInventoryListItem
from iikocloud_client.models.list_request import ListRequest
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
    api_instance = iikocloud_client.InventoryIncomingInventoryApi(api_client)
    list_request = iikocloud_client.ListRequest() # ListRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Export inventories
        api_response = await api_instance.list_inventory_incoming_inventories(list_request, timeout=timeout)
        print("The response of InventoryIncomingInventoryApi->list_inventory_incoming_inventories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingInventoryApi->list_inventory_incoming_inventories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_request** | [**ListRequest**](ListRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**List[IncomingInventoryListItem]**](IncomingInventoryListItem.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request (validation/invalid JSON) |  -  |
**401** | Unauthorized |  -  |
**405** | Method not allowed (POST expected) |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_inventory_incoming_inventory**
> IncomingInventorySaveResponse post_inventory_incoming_inventory(get_by_id_request, timeout=timeout)

Post inventory

Changes the inventory status from NEW to PROCESSED

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.incoming_inventory_save_response import IncomingInventorySaveResponse
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
    api_instance = iikocloud_client.InventoryIncomingInventoryApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Post inventory
        api_response = await api_instance.post_inventory_incoming_inventory(get_by_id_request, timeout=timeout)
        print("The response of InventoryIncomingInventoryApi->post_inventory_incoming_inventory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingInventoryApi->post_inventory_incoming_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**IncomingInventorySaveResponse**](IncomingInventorySaveResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request (validation/invalid JSON) |  -  |
**401** | Unauthorized |  -  |
**405** | Method not allowed (POST expected) |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpost_inventory_incoming_inventory**
> IncomingInventorySaveResponse unpost_inventory_incoming_inventory(get_by_id_request, timeout=timeout)

Unpost inventory

Changes the inventory status from PROCESSED to NEW

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_id_request import GetByIDRequest
from iikocloud_client.models.incoming_inventory_save_response import IncomingInventorySaveResponse
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
    api_instance = iikocloud_client.InventoryIncomingInventoryApi(api_client)
    get_by_id_request = iikocloud_client.GetByIDRequest() # GetByIDRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Unpost inventory
        api_response = await api_instance.unpost_inventory_incoming_inventory(get_by_id_request, timeout=timeout)
        print("The response of InventoryIncomingInventoryApi->unpost_inventory_incoming_inventory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingInventoryApi->unpost_inventory_incoming_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_by_id_request** | [**GetByIDRequest**](GetByIDRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**IncomingInventorySaveResponse**](IncomingInventorySaveResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid request (validation/invalid JSON) |  -  |
**401** | Unauthorized |  -  |
**405** | Method not allowed (POST expected) |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inventory_incoming_inventory**
> IncomingInventorySaveResponse update_inventory_incoming_inventory(incoming_inventory_update_request, timeout=timeout)

Edit inventory

Edits an existing inventory document

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.incoming_inventory_save_response import IncomingInventorySaveResponse
from iikocloud_client.models.incoming_inventory_update_request import IncomingInventoryUpdateRequest
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
    api_instance = iikocloud_client.InventoryIncomingInventoryApi(api_client)
    incoming_inventory_update_request = iikocloud_client.IncomingInventoryUpdateRequest() # IncomingInventoryUpdateRequest | Inventory editing parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Edit inventory
        api_response = await api_instance.update_inventory_incoming_inventory(incoming_inventory_update_request, timeout=timeout)
        print("The response of InventoryIncomingInventoryApi->update_inventory_incoming_inventory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryIncomingInventoryApi->update_inventory_incoming_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incoming_inventory_update_request** | [**IncomingInventoryUpdateRequest**](IncomingInventoryUpdateRequest.md)| Inventory editing parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**IncomingInventorySaveResponse**](IncomingInventorySaveResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated |  -  |
**400** | Invalid request (validation/empty body/invalid JSON/document not found) |  -  |
**401** | Unauthorized |  -  |
**405** | Method not allowed (POST expected) |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

