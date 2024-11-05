
import httpx
from dacite import from_dict, Config

from .models import *
from .consts import BASE_URL, ENDPOINTS


class ZyxelNebulaError(Exception):
    """Exception raised when there is a issue with Zyxel Nebula Client."""


class ZyxelNebulaApiKeyError(ZyxelNebulaError):
    """Exception raised when the Zyxel Nebula API key is invalid or expired."""


class ZyxelNebulaClient:
    """
    ZyxelNebulaClient is a client for interacting with the Zyxel Nebula API, providing methods for managing organizations, devices, sites, and clients within the Nebula ecosystem.
    """

    def __init__(self, api_key: str, client: httpx.AsyncClient = None):
        self.client = client or httpx.AsyncClient()
        self.client.headers = {
            "X-ZyxelNebula-API-Key": api_key
        }
        self.client.event_hooks['response'] = [self.raise_error]

    async def raise_error(self, response: httpx.Response):
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 401:
                raise ZyxelNebulaApiKeyError(
                    "The API token is invalid or has expired.") from e
            raise ZyxelNebulaError() from e
        except httpx.RequestError as e:
            raise ZyxelNebulaError(
                "Failed to connect to Zyxel Nebula. Please check your network connection.") from e
        except Exception as e:
            raise ConnectionError("An unexpected error occurred") from e

    async def get_groups(self) -> List[Group]:
        """
        Retrieve a list of groups available in the Zyxel Nebula platform.

        This asynchronous method sends a GET request to the API endpoint to retrieve all groups, 
        returning a list of `Group` objects.

        Returns:
            List[Group]: A list of `Group` instances representing the available groups.

        Raises:
            httpx.HTTPStatusError: If the response status code indicates an error.

        Example:
            groups = await get_groups()
        """
        url = BASE_URL + ENDPOINTS["GET_GROUPS"]

        response = await self.client.get(url)
        response.raise_for_status()
        data = response.json()
        return [from_dict(data_class=Group, data=item, config=Config(cast=[Enum])) for item in data]

    async def get_organizations_from_group(self, group_id: str) -> List[OrgBaseInfo]:
        """
        Retrieve a list of organizations associated with a specified group.

        This asynchronous method constructs a URL using the provided group ID, sends a GET request 
        to retrieve the organizations linked to that group, and returns a list of `OrgBaseInfo` objects.

        Args:
            group_id (str): The unique identifier for the group.

        Returns:
            List[OrgBaseInfo]: A list of `OrgBaseInfo` instances representing the organizations 
            associated with the specified group.

        Raises:
            httpx.HTTPStatusError: If the response status code indicates an error.

        Example:
            organizations = await get_organizations_from_group(group_id="group123")
        """
        url = BASE_URL + \
            ENDPOINTS["GET_ORGANIZATIONS_FROM_GROUP"].format(group_id=group_id)

        response = await self.client.get(url)
        response.raise_for_status()
        data = response.json()
        return [from_dict(data_class=OrgBaseInfo, data=item, config=Config(cast=[Enum])) for item in data]

    async def get_organizations(self) -> List[OrgBaseInfo]:
        """
        Retrieve a list of all organizations in the Zyxel Nebula platform.

        This asynchronous method sends a GET request to the API endpoint to retrieve all organizations, 
        returning a list of `OrgBaseInfo` objects.

        Returns:
            List[OrgBaseInfo]: A list of `OrgBaseInfo` instances representing all organizations.

        Raises:
            httpx.HTTPStatusError: If the response status code indicates an error.

        Example:
            organizations = await get_organizations()
        """
        url = BASE_URL + ENDPOINTS["GET_ORGANIZATIONS"]

        response = await self.client.get(url)
        response.raise_for_status()
        data = response.json()
        return [from_dict(data_class=OrgBaseInfo, data=item, config=Config(cast=[Enum])) for item in data]

    async def get_organization_info(self, org_id: str) -> Org:
        """
        Retrieve information about a specified organization.

        This asynchronous method constructs a URL using the provided organization ID, sends a GET request 
        to retrieve the organization details, and returns an `Org` object containing the organization 
        information.

        Args:
            org_id (str): The unique identifier for the organization.

        Returns:
            Org: An instance of `Org` containing the information related to the specified organization.

        Raises:
            httpx.HTTPStatusError: If the response status code indicates an error.

        Example:
            organization_info = await get_organization_info(org_id="org123")
        """
        url = BASE_URL + \
            ENDPOINTS["GET_ORGANIZATION_INFO"].format(org_id=org_id)

        response = await self.client.get(url)
        response.raise_for_status()
        data = response.json()
        return from_dict(data_class=Org, data=data, config=Config(cast=[Enum]))

    async def get_sites(self, org_id: str) -> List[Site]:
        """
        Retrieve a list of sites associated with a specified organization.

        This asynchronous method constructs a URL using the provided organization ID, sends a GET request 
        to retrieve the sites, and returns a list of `Site` objects representing the sites.

        Args:
            org_id (str): The unique identifier for the organization.

        Returns:
            List[Site]: A list of `Site` instances representing the sites associated with the specified 
            organization.

        Raises:
            httpx.HTTPStatusError: If the response status code indicates an error.

        Example:
            sites = await get_sites(org_id="org123")
        """
        url = BASE_URL + ENDPOINTS["GET_SITES"].format(org_id=org_id)

        response = await self.client.get(url)
        response.raise_for_status()
        data = response.json()
        return [from_dict(data_class=Site, data=item, config=Config(cast=[Enum])) for item in data]

    async def get_devices_from_organization(self, org_id: str) -> List[Device]:
        """
        Retrieve a list of devices associated with a specified organization.

        This asynchronous method constructs a URL using the provided organization ID, sends a GET request 
        to retrieve the devices, and returns a list of `Device` objects representing the devices.

        Args:
            org_id (str): The unique identifier for the organization.

        Returns:
            List[Device]: A list of `Device` instances representing the devices associated with the 
            specified organization.

        Raises:
            httpx.HTTPStatusError: If the response status code indicates an error.

        Example:
            devices = await get_devices_from_organization(org_id="org123")
        """
        url = BASE_URL + \
            ENDPOINTS["GET_DEVICES_FROM_ORGANIZATION"].format(org_id=org_id)

        response = await self.client.get(url)
        response.raise_for_status()
        data = response.json()
        return [from_dict(data_class=Device, data=item, config=Config(cast=[Enum])) for item in data[0]["devices"]]

    async def get_device_firmware_status_from_organization(self, org_id: str) -> List[DeviceFirmwareStatus]:
        """
        Retrieve the firmware status of devices associated with a specified organization.

        This asynchronous method constructs a URL using the provided organization ID, sends a GET request 
        to retrieve the firmware status of devices within the organization, and returns a list of 
        `DeviceFirmwareStatus` objects representing the firmware status of each device.

        Args:
            org_id (str): The unique identifier for the organization.

        Returns:
            List[DeviceFirmwareStatus]: A list of `DeviceFirmwareStatus` instances containing the firmware 
            status information for each device associated with the specified organization.

        Raises:
            httpx.HTTPStatusError: If the response status code indicates an error.

        Example:
            firmware_status_list = await get_device_firmware_status_from_organization(org_id="org123")
        """
        url = BASE_URL + \
            ENDPOINTS["GET_DEVICE_FIRMWARE_STATUS_FROM_ORGANIZATION"].format(
                org_id=org_id)

        response = await self.client.get(url)
        response.raise_for_status()
        data = response.json()
        return [from_dict(data_class=DeviceFirmwareStatus, data=item, config=Config(cast=[Enum])) for item in data]

    async def get_device_firmware_status_from_site(self, site_id: str) -> List[DeviceFirmwareStatus]:
        """
        Retrieves the firmware status of all devices associated with a specified site.

        This asynchronous method constructs a URL using the provided site ID, sends a GET request 
        to retrieve the firmware status of devices within the site, and returns a list of 
        `DeviceFirmwareStatus` objects representing the firmware status of each device.
sensor
        Args:
            site_id (str): The unique identifier for the site.

        Returns:
            List[DeviceFirmwareStatus]: A list of `DeviceFirmwareStatus` instances containing the 
            firmware status information for each device associated with the specified site.

        Raises:
            httpx.HTTPStatusError: If the response status code indicates an error.

        Example:
            firmware_status_list = await get_device_firmware_status_from_site(site_id="site123")
        """
        url = BASE_URL + \
            ENDPOINTS["GET_DEVICE_FIRMWARE_STATUS_FROM_SITE"].format(
                site_id=site_id)

        response = await self.client.get(url)
        response.raise_for_status()
        data = response.json()
        return [from_dict(data_class=DeviceFirmwareStatus, data=item, config=Config(cast=[Enum])) for item in data]

    async def get_devices_device_online_by_type(self, site_id: str, device_type: DeviceType) -> List[DeviceOnlineStatus]:
        """
        Retrieve online status information for all devices of a specified type within a site.

        This asynchronous method constructs a URL using the provided site ID, sends a GET request 
        to retrieve the online status of devices filtered by the specified device type, and returns 
        a list of `DeviceOnlineStatus` objects representing the online status of each device.

        Args:
            site_id (str): The ID of the site for which to retrieve device online statuses.
            device_type (DeviceType): The type of device to filter by (e.g., access points, switches).

        Returns:
            List[DeviceOnlineStatus]: A list of `DeviceOnlineStatus` objects representing the online 
            status of each device of the specified type within the site.

        Raises:
            httpx.HTTPStatusError: If the response status code indicates an error.

        Example:
            online_status = await get_devices_device_online_by_type(site_id="site123", device_type=DeviceType.switch)
        """
        url = BASE_URL + \
            ENDPOINTS["GET_DEVICES_ONLINE_BY_TYPE"].format(
                site_id=site_id)

        params = {'type': device_type.value}

        response = await self.client.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return [from_dict(data_class=DeviceOnlineStatus, data=item, config=Config(cast=[Enum])) for item in data]

    async def get_site_vpn_status(self, site_id: str) -> SiteVPNStatus:
        """
        Retrieves the VPN status for a specified site.

        This asynchronous method constructs a URL using the provided site ID, sends a GET request 
        to retrieve the current VPN status of the site, and returns a `SiteVPNStatus` object 
        containing the response data.

        Args:
            site_id (str): The unique identifier for the site.

        Returns:
            SiteVPNStatus: An instance of `SiteVPNStatus` containing the response data related to the 
            VPN status of the specified site.

        Raises:
            httpx.HTTPStatusError: If the response status code indicates an error.

        Example:
            vpn_status = await get_site_vpn_status(site_id="site123")
        """
        url = BASE_URL + \
            ENDPOINTS["GET_SITE_VPN_STATUS"].format(
                site_id=site_id)

        response = await self.client.get(url)
        response.raise_for_status()
        data = response.json()
        return from_dict(data_class=SiteVPNStatus, data=data, config=Config(cast=[Enum]))

    async def get_site_clients(self, site_id: str, attributes: List[ClientAttributesReq] = [ClientAttributesReq.mac_address]) -> List[GenericClient]:
        """
        Retrieves a list of clients for a specified site, including specific attributes.

        This asynchronous method constructs a URL using the provided site ID, sends a POST request 
        with the specified attributes in the payload, and returns a list of `GenericClient` objects 
        containing the response data.

        Args:
            site_id (str): The unique identifier for the site.
            attributes (List[ClientAttributesReq]): A list of attributes to include in the response. 
                Defaults to `[ClientAttributesReq.mac_address]`.

        Returns:
            List[GenericClient]: A list of `GenericClient` instances containing the response data with 
            information about the clients associated with the specified site.

        Raises:
            httpx.HTTPStatusError: If the response status code indicates an error.

        Example:
            site_clients_data = await get_site_clients(site_id="site123", attributes=[ClientAttributesReq.ip_address, ClientAttributesReq.device_name])
        """
        url = BASE_URL + ENDPOINTS["GET_SITE_CLIENTS"].format(site_id=site_id)

        payload = [attr.value for attr in attributes] if attributes else []

        response = await self.client.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return [from_dict(data_class=GenericClient, data=item, config=Config(cast=[Enum])) for item in data]

    async def get_ap_clients(self, site_id: str, attributes: List[APClientAttributesReq] = [APClientAttributesReq.mac_address]) -> List[APClient]:
        """
        Retrieves a list of access point (AP) clients for a specified site, including specific attributes.

        This asynchronous method constructs a URL using the provided site ID, sends a POST request 
        with the specified attributes in the payload, and returns a list of `APClient` objects 
        containing the response data.

        Args:
            site_id (str): The unique identifier for the site.
            attributes (List[APClientAttributesReq]): A list of attributes to include in the response. 
                Defaults to `[APClientAttributesReq.mac_address]`.

        Returns:
            List[APClient]: A list of `APClient` instances containing the response data with information 
            about the access point clients.

        Raises:
            httpx.HTTPStatusError: If the response status code indicates an error.

        Example:
            ap_clients_data = await get_ap_clients(site_id="site123", attributes=[APClientAttributesReq.ip_address, APClientAttributesReq.device_name])
        """
        url = BASE_URL + ENDPOINTS["GET_AP_CLIENTS"].format(site_id=site_id)

        payload = [attr.value for attr in attributes] if attributes else []

        response = await self.client.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return [from_dict(data_class=APClient, data=item, config=Config(cast=[Enum])) for item in data]

    async def ping(self, site_id: str, device_id: str, target: str) -> PingResp:
        """
        Sends a ping request to a specified target from a device within a site.

        This asynchronous method constructs a URL using the provided site ID and device ID, 
        sends a POST request with the target specified in the payload, and returns a 
        `PingResp` object containing the response data.

        Args:
            site_id (str): The unique identifier for the site.
            device_id (str): The unique identifier for the device.
            target (str): The target address (e.g., IP or hostname) to ping.

        Returns:
            PingResp: An instance of `PingResp` containing the response data from the ping request.

        Raises:
            httpx.HTTPStatusError: If the response status code indicates an error.

        Example:
            response = await ping(site_id="site123", device_id="device456", target="192.168.1.1")
        """
        url = BASE_URL + \
            ENDPOINTS["PING"].format(
                site_id=site_id, device_id=device_id)

        payload = {'target': target}

        response = await self.client.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return from_dict(data_class=PingResp, data=data, config=Config(cast=[Enum]))

    async def reboot(self, site_id: str, device_id: str) -> GenericResp:
        """
        Sends a request to reboot a specified device within a site.

        This asynchronous method constructs a URL using the provided site ID and device ID, 
        sends a POST request to initiate a reboot on the specified device, and returns a 
        `GenericResp` object containing the response data.

        Args:
            site_id (str): The unique identifier for the site.
            device_id (str): The unique identifier for the device to be rebooted.

        Returns:
            GenericResp: An instance of `GenericResp` containing the response data from the reboot request.

        Raises:
            httpx.HTTPStatusError: If the response status code indicates an error.

        Example:
            response = await reboot(site_id="site123", device_id="device456")
        """
        url = BASE_URL + \
            ENDPOINTS["REBOOT"].format(
                site_id=site_id, device_id=device_id)

        response = await self.client.post(url)
        response.raise_for_status()
        data = response.json()
        return from_dict(data_class=GenericResp, data=data, config=Config(cast=[Enum]))

    async def cable_test(self, site_id: str, device_id: str, ports: List[int]) -> CableTestResp:
        """
        Performs a cable test on specified ports of a device within a site.

        This asynchronous method constructs a URL using the provided site ID and device ID, 
        sends a POST request with the specified ports in the payload to initiate a cable test, 
        and returns a `CableTestResp` object containing the response data.

        Args:
            site_id (str): The unique identifier for the site.
            device_id (str): The unique identifier for the device on which to perform the cable test.
            ports (List[int]): A list of port numbers to be tested.

        Returns:
            CableTestResp: An instance of `CableTestResp` containing the response data from the cable test request.

        Raises:
            httpx.HTTPStatusError: If the response status code indicates an error.

        Example:
            response = await cable_test(site_id="site123", device_id="device456", ports=[1, 2, 3])
        """
        url = BASE_URL + \
            ENDPOINTS["CABLE_TEST"].format(
                site_id=site_id, device_id=device_id)

        payload = {'ports': ports}

        response = await self.client.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return from_dict(data_class=CableTestResp, data=data, config=Config(cast=[Enum]))

    async def connectivity(self, site_id: str, device_id: str, period: Optional[ClientPeriod] = ClientPeriod.field_2h) -> List[Connectivity]:
        """
        Retrieves connectivity data for a specified device within a site over a given period.

        This asynchronous method constructs a URL using the provided site ID and device ID, 
        sends a POST request with the specified period in the payload, and returns a list of 
        `Connectivity` objects containing the response data.

        Args:
            site_id (str): The unique identifier for the site.
            device_id (str): The unique identifier for the device whose connectivity data is to be retrieved.
            period (Optional[ClientPeriod]): The time period for which to retrieve connectivity data. 
                Defaults to `ClientPeriod.field_2h`.

        Returns:
            List[Connectivity]: A list of `Connectivity` instances containing the response data.

        Raises:
            httpx.HTTPStatusError: If the response status code indicates an error.

        Example:
            connectivity_data = await connectivity(site_id="site123", device_id="device456", period=ClientPeriod.field_1h)
        """
        url = BASE_URL + \
            ENDPOINTS["CONNECTIVITY"].format(
                site_id=site_id, device_id=device_id)

        payload = {'period': period.value}

        response = await self.client.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return [from_dict(data_class=Connectivity, data=item, config=Config(cast=[Enum])) for item in data]

    async def get_site_clients_v2(self, site_id: str, period: Optional[ClientPeriod] = ClientPeriod.field_2h, features: Optional[List[ClientAttributesReq]] = [ClientAttributesReq.mac_address], ) -> GenericClients:
        """
        Retrieves client information for a specified site over a given period, including specific attributes.

        This asynchronous method constructs a URL using the provided site ID, sends a POST request with 
        the specified period and features in the payload, and returns a `GenericClients` object containing 
        the response data.

        Args:
            site_id (str): The unique identifier for the site.
            period (Optional[ClientPeriod]): The time period for which to retrieve client data. 
                Defaults to `ClientPeriod.field_2h`.
            features (Optional[List[ClientAttributesReq]]): A list of client attributes to include in the response. 
                Defaults to `[ClientAttributesReq.mac_address]`.

        Returns:
            GenericClients: An instance of `GenericClients` containing the response data with client information.

        Raises:
            httpx.HTTPStatusError: If the response status code indicates an error.

        Example:
            clients_data = await get_site_clients_v2(site_id="site123", period=ClientPeriod.field_1h, features=[ClientAttributesReq.ip_address, ClientAttributesReq.device_name])
        """
        url = BASE_URL + \
            ENDPOINTS["GET_SITE_CLIENTS_V2"].format(site_id=site_id)

        payload = {
            "period": period.value if period else None,
            "featrues": [attr.value for attr in features] if features else []
        }

        response = await self.client.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return from_dict(data_class=GenericClients, data=data, config=Config(cast=[Enum]))

    async def get_ap_clients_v2(self, site_id: str, period: Optional[ClientPeriod] = ClientPeriod.field_2h, features: Optional[List[APClientAttributesReqV2]] = [APClientAttributesReqV2.mac_address], ) -> APClients:
        """
        Retrieves client information for a specified access point (AP) within a site over a given period, including specific attributes.

        This asynchronous method constructs a URL using the provided site ID, sends a POST request with 
        the specified period and features in the payload, and returns an `APClients` object containing 
        the response data.

        Args:
            site_id (str): The unique identifier for the site.
            period (Optional[ClientPeriod]): The time period for which to retrieve AP client data. 
                Defaults to `ClientPeriod.field_2h`.
            features (Optional[List[APClientAttributesReqV2]]): A list of AP client attributes to include in the response. 
                Defaults to `[APClientAttributesReqV2.mac_address]`.

        Returns:
            APClients: An instance of `APClients` containing the response data with AP client information.

        Raises:
            httpx.HTTPStatusError: If the response status code indicates an error.

        Example:
            ap_clients_data = await get_ap_clients_v2(site_id="site123", period=ClientPeriod.field_1h, features=[APClientAttributesReqV2.ip_address, APClientAttributesReqV2.device_name])
        """
        url = BASE_URL + \
            ENDPOINTS["GET_AP_CLIENTS_V2"].format(site_id=site_id)

        payload = {
            "period": period.value if period else None,
            "featrues": [attr.value for attr in features] if features else []
        }

        response = await self.client.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return from_dict(data_class=APClients, data=data, config=Config(cast=[Enum]))

    async def get_sw_clients_v2(self, site_id: str, period: Optional[ClientPeriod] = ClientPeriod.field_2h, features: Optional[List[SWClientAttributesReq]] = [SWClientAttributesReq.mac_address], ) -> SWClients:
        """
        Retrieves client information for specified switches within a site over a given period, including specific attributes.

        This asynchronous method constructs a URL using the provided site ID, sends a POST request with 
        the specified period and features in the payload, and returns an `SWClients` object containing 
        the response data.

        Args:
            site_id (str): The unique identifier for the site.
            period (Optional[ClientPeriod]): The time period for which to retrieve switch client data. 
                Defaults to `ClientPeriod.field_2h`.
            features (Optional[List[SWClientAttributesReq]]): A list of switch client attributes to include in the response. 
                Defaults to `[SWClientAttributesReq.mac_address]`.

        Returns:
            SWClients: An instance of `SWClients` containing the response data with switch client information.

        Raises:
            httpx.HTTPStatusError: If the response status code indicates an error.

        Example:
            sw_clients_data = await get_sw_clients_v2(site_id="site123", period=ClientPeriod.field_1h, features=[SWClientAttributesReq.ip_address, SWClientAttributesReq.device_name])
        """
        url = BASE_URL + \
            ENDPOINTS["GET_SW_CLIENTS_V2"].format(site_id=site_id)

        payload = {
            "period": period.value if period else None,
            "featrues": [attr.value for attr in features] if features else []
        }

        response = await self.client.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return from_dict(data_class=SWClients, data=data, config=Config(cast=[Enum]))

    async def get_gw_clients_v2(self, site_id: str, period: Optional[ClientPeriod] = ClientPeriod.field_2h, features: Optional[List[GWClientAttributesReq]] = [GWClientAttributesReq.mac_address], ) -> GWClients:
        """
        Retrieves client information for specified gateways within a site over a given period, including specific attributes.

        This asynchronous method constructs a URL using the provided site ID, sends a POST request with 
        the specified period and features in the payload, and returns a `GWClients` object containing 
        the response data.

        Args:
            site_id (str): The unique identifier for the site.
            period (Optional[ClientPeriod]): The time period for which to retrieve gateway client data. 
                Defaults to `ClientPeriod.field_2h`.
            features (Optional[List[GWClientAttributesReq]]): A list of gateway client attributes to include in the response. 
                Defaults to `[GWClientAttributesReq.mac_address]`.

        Returns:
            GWClients: An instance of `GWClients` containing the response data with gateway client information.

        Raises:
            httpx.HTTPStatusError: If the response status code indicates an error.

        Example:
            gw_clients_data = await get_gw_clients_v2(site_id="site123", period=ClientPeriod.field_1h, features=[GWClientAttributesReq.ip_address, GWClientAttributesReq.device_name])
        """
        url = BASE_URL + \
            ENDPOINTS["GET_GW_CLIENTS_V2"].format(site_id=site_id)

        payload = {
            "period": period.value if period else None,
            "featrues": [attr.value for attr in features] if features else []
        }

        response = await self.client.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return from_dict(data_class=GWClients, data=data, config=Config(cast=[Enum]))
