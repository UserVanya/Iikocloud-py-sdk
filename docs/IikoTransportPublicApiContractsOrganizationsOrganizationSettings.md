# IikoTransportPublicApiContractsOrganizationsOrganizationSettings

Organization settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Organization ID. | 
**prices_vat_inclusive** | **bool** | Determines whether organization prices include VAT.                Available if &#x60;VAT&#x60; requested. | [optional] 
**loyalty_discount_affects_vat** | **bool** | Determines whether organization loyalty discounts affects VAT.                &gt; Working only if \&quot;pricesVatInclusive\&quot; &#x3D; false                Available if &#x60;VAT&#x60; requested. | [optional] 
**version** | **str** | RMS version.                Available if &#x60;Version&#x60; requested. | [optional] 
**address_format_type** | [**IikoTransportPublicApiContractsOrganizationsAddressFormatType**](IikoTransportPublicApiContractsOrganizationsAddressFormatType.md) | Address format type.                Available if &#x60;AddressFormatType&#x60; requested. | [optional] 
**is_anonymous_guests_allowed** | **bool** | If the store allows orders for anonymous guests, then it is not necessary to transfer  information about the guest as part of the delivery order. You can only transfer  the phone number and optionally name of the guest, which will not be stored in the guest base  and will only be used for the delivery of a current delivery order.                Available if &#x60;IsAnonymousGuestsAllowed&#x60; requested. | [optional] 
**name** | **str** | Organization name.                Available if &#x60;Name&#x60; requested. | [optional] 
**country** | **str** | Country.                Available if &#x60;Country&#x60; requested. | [optional] 
**restaurant_address** | **str** | Restaurant address.                Available if &#x60;RestaurantAddress&#x60; requested. | [optional] 
**latitude** | **float** | Latitude.                Available if &#x60;Latitude&#x60; requested. | [optional] 
**longitude** | **float** | Longitude.                Available if &#x60;Longitude&#x60; requested. | [optional] 
**use_uae_addressing_system** | **bool** | Regional setting \&quot;Use the UAE Addressing System\&quot;.                Available if &#x60;UseUaeAddressingSystem&#x60; requested. | [optional] 
**country_phone_code** | **str** | Country dialing code.                Available if &#x60;CountryPhoneCode&#x60; requested. | [optional] 
**marketing_source_required_in_delivery** | **bool** | Require mandatory marketing source input when creating a delivery.                Available if &#x60;MarketingSourceRequiredInDelivery&#x60; requested. | [optional] 
**default_delivery_city_id** | **UUID** | Default delivery city.                Available if &#x60;DefaultDeliveryCityId&#x60; requested. | [optional] 
**delivery_city_ids** | **List[UUID]** | Delivery cities.                Available if &#x60;DeliveryCityIds&#x60; requested. | [optional] 
**delivery_service_type** | [**IikoTransportPublicApiContractsOrganizationsDeliverySettingsServiceType**](IikoTransportPublicApiContractsOrganizationsDeliverySettingsServiceType.md) | Delivery type.                Available if &#x60;DeliveryServiceType&#x60; requested. | [optional] 
**delivery_order_payment_settings** | [**IikoTransportPublicApiContractsOrganizationsDeliveryOrderPaymentSettings**](IikoTransportPublicApiContractsOrganizationsDeliveryOrderPaymentSettings.md) | Delivery order payment settings.                Available if &#x60;DeliveryOrderPaymentSettings&#x60; requested. | [optional] 
**default_call_center_payment_type_id** | **UUID** | Default payment type for CallCenter.                Available if &#x60;DefaultCallCenterPaymentTypeId&#x60; requested. | [optional] 
**order_item_comment_enabled** | **bool** | Allow text comments for order items (in all restaurant sections).                Available if &#x60;OrderItemCommentEnabled&#x60; requested. | [optional] 
**is_confirmation_enabled** | **bool** | Determines whether to use delivery confirmation.                Available if &#x60;IsConfirmationEnabled&#x60; requested. | [optional] 
**confirm_allowed_interval_in_minutes** | **int** | Confirm orders time interval.                Available if &#x60;ConfirmAllowedIntervalInMinutes&#x60; requested. | [optional] 
**address_lookup** | [**List[IikoTransportPublicApiContractsAddressHintsAddressHintsServiceType]**](IikoTransportPublicApiContractsAddressHintsAddressHintsServiceType.md) | Available address lookup services.                Available if &#x60;AddressLookup&#x60; requested. | [optional] 
**use_business_hours_and_mapping** | **bool** | Determines whether the organization use a business hours and mapping settings. | [optional] 
**currency_iso_name** | **str** | ISO currency code (for example: RUB, USD, EUR). | [optional] 
**external_data** | [**List[IikoTransportPublicApiContractsCommonExternalData]**](IikoTransportPublicApiContractsCommonExternalData.md) | Organization&#x60;s external data. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_organizations_organization_settings import IikoTransportPublicApiContractsOrganizationsOrganizationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsOrganizationsOrganizationSettings from a JSON string
iiko_transport_public_api_contracts_organizations_organization_settings_instance = IikoTransportPublicApiContractsOrganizationsOrganizationSettings.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsOrganizationsOrganizationSettings.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_organizations_organization_settings_dict = iiko_transport_public_api_contracts_organizations_organization_settings_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsOrganizationsOrganizationSettings from a dict
iiko_transport_public_api_contracts_organizations_organization_settings_from_dict = IikoTransportPublicApiContractsOrganizationsOrganizationSettings.from_dict(iiko_transport_public_api_contracts_organizations_organization_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


