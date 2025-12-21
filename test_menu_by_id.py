#menu_test_organization_id = UUID('815bb8fd-b393-477a-8abc-fb962ab408d6'), menu_id = '23311'
import iikocloud_client as icc
import asyncio
from uuid import UUID
async def main():
    client = icc.ApiClient()
    menu_api = icc.MenuApi(client)
    auth_api = icc.AuthorizationApi(client)
    
    async with client:
        response = await auth_api.access_token_post(
            auth_get_access_token_request=icc.AuthGetAccessTokenRequest(
                apiLogin='df9096bf2bde4e38858c3b60dbc14a36',
            )
        )
        print(response)
        client.configuration.access_token = response.token
        request = icc.NomenclatureMenuRequest(
            organizationIds=[UUID('815bb8fd-b393-477a-8abc-fb962ab408d6')],
            externalMenuId='23311',
            version=4
        )
        response_2 = await menu_api.menu_by_id_post(nomenclature_menu_request=request)
        print(response_2)
asyncio.run(main())