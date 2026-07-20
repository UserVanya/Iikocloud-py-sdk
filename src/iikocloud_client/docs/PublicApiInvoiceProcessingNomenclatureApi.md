# iikocloud_client.PublicApiInvoiceProcessingNomenclatureApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_inventory_product_barcodes**](PublicApiInvoiceProcessingNomenclatureApi.md#update_inventory_product_barcodes) | **POST** /api/inventory/v1/nomenclature/update_barcodes | Update product barcodes


# **update_inventory_product_barcodes**
> UpdateProductBarcodesResponse update_inventory_product_barcodes(update_product_barcodes_request)

Update product barcodes

Replaces all existing barcodes for a specified nomenclature item with a new set.
<b>Note</b>: This is a full replacement operation. Any previously assigned barcode values are permanently removed and overwritten by the values provided in the request


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.update_product_barcodes_request import UpdateProductBarcodesRequest
from iikocloud_client.models.update_product_barcodes_response import UpdateProductBarcodesResponse
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
    api_instance = iikocloud_client.PublicApiInvoiceProcessingNomenclatureApi(api_client)
    update_product_barcodes_request = iikocloud_client.UpdateProductBarcodesRequest() # UpdateProductBarcodesRequest | Product barcode update request

    try:
        # Update product barcodes
        api_response = await api_instance.update_inventory_product_barcodes(update_product_barcodes_request)
        print("The response of PublicApiInvoiceProcessingNomenclatureApi->update_inventory_product_barcodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiInvoiceProcessingNomenclatureApi->update_inventory_product_barcodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_product_barcodes_request** | [**UpdateProductBarcodesRequest**](UpdateProductBarcodesRequest.md)| Product barcode update request | 

### Return type

[**UpdateProductBarcodesResponse**](UpdateProductBarcodesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product barcodes successfully updated |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Access forbidden |  -  |
**404** | Product or related resource not found |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict when updating product barcodes |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | RMS error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

