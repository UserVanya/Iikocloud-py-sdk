# ExtendedOrganizationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_format_type** | [**AddressFormatType**](AddressFormatType.md) | Address format type. | 
**address_lookup** | [**List[AddressHintsServiceType]**](AddressHintsServiceType.md) | Available address lookup services. | 
**confirm_allowed_interval_in_minutes** | **int** | Confirm orders time interval. | 
**country** | **str** | Country. | 
**country_phone_code** | **str** | Country dialing code. | 
**currency_iso_name** | **str** | ISO currency code (for example: RUB, USD, EUR). | 
**currency_minimum_denomination** | **float** | Value rounding of position. | 
**default_call_center_payment_type_id** | **UUID** | Default payment type for CallCenter. | 
**default_delivery_city_id** | **UUID** | Default delivery city. | 
**delivery_city_ids** | **List[UUID]** | Delivery cities. | 
**delivery_order_payment_settings** | [**DeliveryOrderPaymentSettings**](DeliveryOrderPaymentSettings.md) | Delivery order payment settings. | [optional] 
**delivery_service_type** | [**DeliverySettingsServiceType**](DeliverySettingsServiceType.md) | Delivery type. | 
**inn** | **str** | Restaurant&#x60;s INN (Taxpayer Identification Number). | 
**is_anonymous_guests_allowed** | **bool** | If the store allows orders for anonymous guests, then it is not necessary to transfer  information about the guest as part of the delivery order. You can only transfer  the phone number and optionally name of the guest, which will not be stored in the guest base  and will only be used for the delivery of a current delivery order. | [optional] 
**is_cloud** | **bool** | Determines whether organization is hosted in iikoCloud. | 
**is_confirmation_enabled** | **bool** | Determines whether to use delivery confirmation. | 
**latitude** | **float** | Latitude. | 
**longitude** | **float** | Longitude. | 
**marketing_source_required_in_delivery** | **bool** | Require mandatory marketing source input when creating a delivery. | 
**order_item_comment_enabled** | **bool** | Allow text comments for order items (in all restaurant sections). | 
**restaurant_address** | **str** | Restaurant address. | 
**use_uae_addressing_system** | **bool** | Regional setting \&quot;Use the UAE Addressing System\&quot;. | 
**version** | **str** | RMS version. | 

## Example

```python
from iikocloud_client.models.extended_organization_info import ExtendedOrganizationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedOrganizationInfo from a JSON string
extended_organization_info_instance = ExtendedOrganizationInfo.from_json(json)
# print the JSON string representation of the object
print(ExtendedOrganizationInfo.to_json())

# convert the object into a dict
extended_organization_info_dict = extended_organization_info_instance.to_dict()
# create an instance of ExtendedOrganizationInfo from a dict
extended_organization_info_from_dict = ExtendedOrganizationInfo.from_dict(extended_organization_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


