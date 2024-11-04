from enum import Enum
import pytest
from dacite import from_dict, Config
from httpx import AsyncClient
from pytest_httpx import HTTPXMock
from zyxel_nebula_client.consts import ENDPOINTS, BASE_URL
from zyxel_nebula_client import ClientAttributesReq, ZyxelNebulaClient
from zyxel_nebula_client.models import APClient, APClientAttributesReq, APClients, CableTestResp, ClientPeriod, Connectivity, Device, DeviceFirmwareStatus, DeviceOnlineStatus, DeviceType, FirmwareStatus, GWClients, GenericClient, GenericClients, GenericResp, Group, OnlineOffline, Org, OrgBaseInfo, OrgMode, PingResp, SWClients, SiteVPNStatus


@pytest.mark.asyncio
async def test_get_groups(httpx_mock: HTTPXMock):
    """Test the `get_groups` method."""
    client = ZyxelNebulaClient(api_key="dummy_api_key")

    # Define the mock data returned by the API
    mock_data = [
        {
            "name": "string",
            "groupId": "string"
        }
    ]

    # Set up the expected URL and mock response
    endpoint = BASE_URL + ENDPOINTS["GET_GROUPS"]
    httpx_mock.add_response(url=endpoint, json=mock_data, method="GET")

    # Call the client method
    result = await client.get_groups()

    # Validate the result
    assert len(result) == 1

    expected = from_dict(data_class=Group,
                         data=mock_data[0], config=Config(cast=[Enum]))

    assert result[0] == expected


@pytest.mark.asyncio
async def test_get_organizations_from_group(httpx_mock: HTTPXMock):
    """Test the `get_organizations_from_group` method."""
    client = ZyxelNebulaClient(api_key="dummy_api_key")
    group_id = "test_group_id"

    # Define the mock data returned by the API
    mock_data = [
        {
            "name": "string",
            "orgId": "string",
            "mode": "PRO"
        }
    ]

    # Set up the expected URL and mock response
    endpoint = BASE_URL + \
        ENDPOINTS["GET_ORGANIZATIONS_FROM_GROUP"].format(group_id=group_id)
    httpx_mock.add_response(url=endpoint, json=mock_data, method="GET")

    # Call the client method
    result = await client.get_organizations_from_group(group_id)

    # Validate the result
    assert len(result) == 1

    expected = from_dict(data_class=OrgBaseInfo,
                         data=mock_data[0], config=Config(cast=[Enum]))

    assert result[0] == expected


@pytest.mark.asyncio
async def test_get_organizations(httpx_mock: HTTPXMock):
    """Test the `get_organizations_from_group` method."""
    client = ZyxelNebulaClient(api_key="dummy_api_key")

    # Define the mock data returned by the API
    mock_data = [
        {
            "name": "string",
            "orgId": "string",
            "mode": "PRO"
        }
    ]

    # Set up the expected URL and mock response
    endpoint = BASE_URL + ENDPOINTS["GET_ORGANIZATIONS"]
    httpx_mock.add_response(url=endpoint, json=mock_data, method="GET")

    # Call the client method
    result = await client.get_organizations()

    # Validate the result
    assert len(result) == 1

    expected = from_dict(data_class=OrgBaseInfo,
                         data=mock_data[0], config=Config(cast=[Enum]))

    assert result[0] == expected


@pytest.mark.asyncio
async def test_get_organization_info(httpx_mock: HTTPXMock):
    """Test the `get_organizations_from_group` method."""
    client = ZyxelNebulaClient(api_key="dummy_api_key")
    org_id = "test_organization_id"

    # Define the mock data returned by the API
    mock_data = {
        "name": "string",
        "orgId": "string",
        "mode": "PRO",
        "prevMode": "PRO",
        "mspId": "string",
        "notes": "string",
        "licenseOverview": {
            "NCCTrialEndAt": "string",
            "NCCExpiredAt": "string"
        }
    }

    # Set up the expected URL and mock response
    endpoint = BASE_URL + \
        ENDPOINTS["GET_ORGANIZATION_INFO"].format(
            org_id=org_id)
    httpx_mock.add_response(url=endpoint, json=mock_data, method="GET")

    # Call the client method
    result = await client.get_organization_info(org_id)

    # Validate the result
    expected = from_dict(data_class=Org,
                         data=mock_data, config=Config(cast=[Enum]))

    assert result == expected


@pytest.mark.asyncio
async def test_get_devices_from_organization(httpx_mock: HTTPXMock):
    """Test the `test_get_devices_from_organization` method with specific attributes."""
    client = ZyxelNebulaClient(api_key="dummy_api_key")
    org_id = "org_id"

    # Define the mock data returned by the API
    mock_data = [
        {
            "siteId": "string",
            "devices": [
                {
                    "devId": "string",
                    "name": "string",
                    "mac": "string",
                    "sn": "string",
                    "model": "string",
                    "type": "AP"
                }
            ]
        }
    ]

    # Set up the expected URL and mock response
    endpoint = BASE_URL + \
        ENDPOINTS["GET_DEVICES_FROM_ORGANIZATION"].format(org_id=org_id)
    httpx_mock.add_response(url=endpoint, json=mock_data, method="GET")

    # Call the client method
    result = await client.get_devices_from_organization(org_id)

    # Validate the result
    assert len(result) == 1

    expected = from_dict(data_class=Device,
                         data=mock_data[0]["devices"][0], config=Config(cast=[Enum]))

    assert result[0] == expected


@pytest.mark.asyncio
async def test_get_device_firmware_status_from_organization(httpx_mock: HTTPXMock):
    """Test the `test_get_device_firmware_status_from_organization` method with specific attributes."""
    client = ZyxelNebulaClient(api_key="dummy_api_key")
    org_id = "org_id"

    # Define the mock data returned by the API
    mock_data = [
        {
            "devId": "string",
            "currentVersion": "string",
            "latestVersion": "string",
            "status": "N/A",
            "lastUpgradeTime": "string"
        }
    ]

    # Set up the expected URL and mock response
    endpoint = BASE_URL + \
        ENDPOINTS["GET_DEVICE_FIRMWARE_STATUS_FROM_ORGANIZATION"].format(
            org_id=org_id)
    httpx_mock.add_response(url=endpoint, json=mock_data, method="GET")

    # Call the client method
    result = await client.get_device_firmware_status_from_organization(org_id)

    # Validate the result
    assert len(result) == 1

    expected = from_dict(data_class=DeviceFirmwareStatus,
                         data=mock_data[0], config=Config(cast=[Enum]))

    assert result[0] == expected


@pytest.mark.asyncio
async def test_get_device_firmware_status_from_site(httpx_mock: HTTPXMock):
    """Test the `get_device_firmware_status_from_organization` method with specific attributes."""
    client = ZyxelNebulaClient(api_key="dummy_api_key")
    site_id = "site_id"

    # Define the mock data returned by the API
    mock_data = [
        {
            "devId": "string",
            "currentVersion": "string",
            "latestVersion": "string",
            "status": "N/A",
            "lastUpgradeTime": "string"
        }
    ]

    # Set up the expected URL and mock response
    endpoint = BASE_URL + \
        ENDPOINTS["GET_DEVICE_FIRMWARE_STATUS_FROM_SITE"].format(
            site_id=site_id)
    httpx_mock.add_response(url=endpoint, json=mock_data, method="GET")

    # Call the client method
    result = await client.get_device_firmware_status_from_site(site_id)

    # Validate the result
    assert len(result) == 1

    expected = from_dict(data_class=DeviceFirmwareStatus,
                         data=mock_data[0], config=Config(cast=[Enum]))

    assert result[0] == expected


@pytest.mark.asyncio
async def test_get_devices_device_online_by_type(httpx_mock: HTTPXMock):
    """Test the `get_devices_device_online_by_type` method with specific attributes."""
    client = ZyxelNebulaClient(api_key="dummy_api_key")
    site_id = "site_id"
    device_type = DeviceType.AP

    # Define the mock data returned by the API
    mock_data = [
        {
            "devId": "string",
            "currentStatus": "ONLINE"
        }
    ]

    # Set up the expected URL and mock response
    endpoint = BASE_URL + \
        ENDPOINTS["GET_DEVICES_ONLINE_BY_TYPE"].format(
            site_id=site_id) + "?type=AP"
    httpx_mock.add_response(url=endpoint, json=mock_data, method="GET")

    # Call the client method
    result = await client.get_devices_device_online_by_type(site_id, device_type)

    # Validate the result
    assert len(result) == 1

    expected = from_dict(data_class=DeviceOnlineStatus,
                         data=mock_data[0], config=Config(cast=[Enum]))

    assert result[0] == expected


@pytest.mark.asyncio
async def test_get_site_vpn_status(httpx_mock: HTTPXMock):
    """Test the `get_site_vpn_status` method with specific attributes."""
    client = ZyxelNebulaClient(api_key="dummy_api_key")
    site_id = "site_id"

    # Define the mock data returned by the API
    mock_data = {
        "sites": [
            {
                "siteId": "string",
                "subnets": [
                    "string"
                ],
                "tunnel": [
                    {
                        "uptime": 0,
                        "status": "string",
                        "lastHeartbeat": 0
                    }
                ]
            }
        ],
        "gateways": [
            {
                "peer": "string",
                "subnets": [
                    "string"
                ],
                "tunnel": [
                    {
                        "uptime": 0,
                        "status": "string",
                        "lastHeartbeat": 0
                    }
                ]
            }
        ],
        "remoteAps": [
            {
                "devId": "string",
                "uptime": 0,
                "status": "string",
                "lastHeartbeat": 0
            }
        ],
        "cleints": [
            {
                "username": "string",
                "hostname": "string",
                "publicIPv4": "192.168.0.1",
                "asssignedIPv4": "192.168.0.1"
            }
        ]
    }

    # Set up the expected URL and mock response
    endpoint = BASE_URL + \
        ENDPOINTS["GET_SITE_VPN_STATUS"].format(
            site_id=site_id)
    httpx_mock.add_response(url=endpoint, json=mock_data, method="GET")

    # Call the client method
    result = await client.get_site_vpn_status(site_id)

    expected = from_dict(data_class=SiteVPNStatus,
                         data=mock_data, config=Config(cast=[Enum]))

    # Validate the result
    assert result == expected


@ pytest.mark.asyncio
async def test_get_site_clients(httpx_mock: HTTPXMock):
    """Test the `get_site_clients` method with specific attributes."""
    client = ZyxelNebulaClient(api_key="dummy_api_key")
    site_id = "test_site_id"
    attributes = [ClientAttributesReq.mac_address, ClientAttributesReq.ipv4]

    # Define the mock data returned by the API
    mock_data = [
        {
            "macAddress": "string",
            "ipv4Address": "192.168.0.1",
            "vlan": 0,
            "lastSeen": 0,
            "connectedTo": "string",
            "status": "ONLINE",
            "firstSeen": 0,
            "description": "string",
            "osHostname": {
                "os": "string",
                "hostname": "string"
            },
            "manufacturer": "string"
        }
    ]

    # Set up the expected URL and mock response
    endpoint = BASE_URL + ENDPOINTS["GET_SITE_CLIENTS"].format(site_id=site_id)
    httpx_mock.add_response(url=endpoint, json=mock_data, method="POST")

    # Call the client method
    result = await client.get_site_clients(site_id=site_id, attributes=attributes)

    # Validate the result
    assert len(result) == 1

    expected = from_dict(data_class=GenericClient,
                         data=mock_data[0], config=Config(cast=[Enum]))

    assert result[0] == expected


@ pytest.mark.asyncio
async def test_get_ap_clients(httpx_mock: HTTPXMock):
    """Test the `get_site_clients` method with specific attributes."""
    client = ZyxelNebulaClient(api_key="dummy_api_key")
    site_id = "test_site_id"
    attributes = [APClientAttributesReq.mac_address,
                  APClientAttributesReq.ipv4]

    # Define the mock data returned by the API
    mock_data = [
        {
            "macAddress": "string",
            "ipv4Address": "192.168.0.1",
            "lastSeen": 0,
            "connectedTo": "string",
            "firstSeen": 0,
            "description": "string",
            "osHostname": {
                "os": "string",
                "hostname": "string"
            },
            "manufacturer": "string",
            "ssid": {
                "name": "string",
                "security": "OPEN"
            },
            "wifiStation": {
                "status": "ONLINE",
                "vlan": 0,
                "signal": 0,
                "band": "band24",
                "channel": 0
            }
        }
    ]

    # Set up the expected URL and mock response
    endpoint = BASE_URL + ENDPOINTS["GET_AP_CLIENTS"].format(site_id=site_id)
    httpx_mock.add_response(url=endpoint, json=mock_data, method="POST")

    # Call the client method
    result = await client.get_ap_clients(site_id=site_id, attributes=attributes)

    # Validate the result
    assert len(result) == 1

    expected = from_dict(data_class=APClient,
                         data=mock_data[0], config=Config(cast=[Enum]))

    assert result[0] == expected


@pytest.mark.asyncio
async def test_ping(httpx_mock: HTTPXMock):
    """Test the `get_site_vpn_status` method with specific attributes."""
    client = ZyxelNebulaClient(api_key="dummy_api_key")
    site_id = "site_id"
    device_id = "device_id"

    # Define the mock data returned by the API
    mock_data = {
        "token": "string",
        "isDone": True,
        "results": [
            {
                "seq": 0,
                "loss": True,
                "timestamp": 0,
                "elapsedTime": 0
            }
        ]
    }

    # Set up the expected URL and mock response
    endpoint = BASE_URL + \
        ENDPOINTS["PING"].format(
            site_id=site_id, device_id=device_id)
    httpx_mock.add_response(url=endpoint, json=mock_data, method="POST")

    # Call the client method
    result = await client.ping(site_id, device_id, target="test")

    expected = from_dict(data_class=PingResp,
                         data=mock_data, config=Config(cast=[Enum]))

    # Validate the result
    assert result == expected


@pytest.mark.asyncio
async def test_reboot(httpx_mock: HTTPXMock):
    """Test the `get_site_vpn_status` method with specific attributes."""
    client = ZyxelNebulaClient(api_key="dummy_api_key")
    site_id = "site_id"
    device_id = "device_id"

    # Define the mock data returned by the API
    mock_data = {
        "status": 0,
        "message": "string"
    }

    # Set up the expected URL and mock response
    endpoint = BASE_URL + \
        ENDPOINTS["REBOOT"].format(
            site_id=site_id, device_id=device_id)
    httpx_mock.add_response(url=endpoint, json=mock_data, method="POST")

    # Call the client method
    result = await client.reboot(site_id, device_id)

    expected = from_dict(data_class=GenericResp,
                         data=mock_data, config=Config(cast=[Enum]))

    # Validate the result
    assert result == expected


@pytest.mark.asyncio
async def test_cable_test(httpx_mock: HTTPXMock):
    """Test the `get_site_vpn_status` method with specific attributes."""
    client = ZyxelNebulaClient(api_key="dummy_api_key")
    site_id = "site_id"
    device_id = "device_id"

    # Define the mock data returned by the API
    mock_data = {
        "ports": [
            {
                "port": 0,
                "results": [
                    {
                        "channel": "string",
                        "pairStatus": "string",
                        "pairLength": "string",
                        "pairDistanceToFault": "string"
                    }
                ]
            }
        ]
    }

    # Set up the expected URL and mock response
    endpoint = BASE_URL + \
        ENDPOINTS["CABLE_TEST"].format(
            site_id=site_id, device_id=device_id)
    httpx_mock.add_response(url=endpoint, json=mock_data, method="POST")

    # Call the client method
    result = await client.cable_test(site_id, device_id, [0, 1, 2])

    expected = from_dict(data_class=CableTestResp,
                         data=mock_data, config=Config(cast=[Enum]))

    # Validate the result
    assert result == expected


@pytest.mark.asyncio
async def test_connectivity(httpx_mock: HTTPXMock):
    """Test the `get_site_vpn_status` method with specific attributes."""
    client = ZyxelNebulaClient(api_key="dummy_api_key")
    site_id = "site_id"
    device_id = "device_id"

    # Define the mock data returned by the API
    mock_data = [
        {
            "begin_time": 0,
            "end_time": 0,
            "status": "string"
        }
    ]

    # Set up the expected URL and mock response
    endpoint = BASE_URL + \
        ENDPOINTS["CONNECTIVITY"].format(
            site_id=site_id, device_id=device_id)
    httpx_mock.add_response(url=endpoint, json=mock_data, method="POST")

    # Call the client method
    result = await client.connectivity(site_id, device_id, ClientPeriod.field_2h)

    # Validate the result
    assert len(result) == 1

    expected = from_dict(data_class=Connectivity,
                         data=mock_data[0], config=Config(cast=[Enum]))

    assert result[0] == expected


@pytest.mark.asyncio
async def test_get_site_clients_v2(httpx_mock: HTTPXMock):
    """Test the `get_site_vpn_status` method with specific attributes."""
    client = ZyxelNebulaClient(api_key="dummy_api_key")
    site_id = "site_id"

    # Define the mock data returned by the API
    mock_data = {
        "KeyFields": [
            "macAddress"
        ],
        "data": [
            {
                "macAddress": "string",
                "ipv4Address": "192.168.0.1",
                "vlan": 0,
                "lastSeen": 0,
                "connectedTo": "string",
                "status": "ONLINE",
                "firstSeen": 0,
                "description": "string",
                "osHostname": {
                    "os": "string",
                    "hostname": "string"
                },
                "manufacturer": "string"
            }
        ]
    }

    # Set up the expected URL and mock response
    endpoint = BASE_URL + \
        ENDPOINTS["GET_SITE_CLIENTS_V2"].format(
            site_id=site_id)
    httpx_mock.add_response(url=endpoint, json=mock_data, method="POST")

    # Call the client method
    result = await client.get_site_clients_v2(site_id, ClientPeriod.field_2h)

    # Validate the result
    expected = from_dict(data_class=GenericClients,
                         data=mock_data, config=Config(cast=[Enum]))

    assert result == expected


@pytest.mark.asyncio
async def test_get_ap_clients_v2(httpx_mock: HTTPXMock):
    """Test the `get_site_vpn_status` method with specific attributes."""
    client = ZyxelNebulaClient(api_key="dummy_api_key")
    site_id = "site_id"

    # Define the mock data returned by the API
    mock_data = {
        "KeyFields": [
            "macAddress"
        ],
        "data": [
            {
                "macAddress": "string",
                "ipv4Address": "192.168.0.1",
                "lastSeen": 0,
                "connectedTo": "string",
                "firstSeen": 0,
                "description": "string",
                "osHostname": {
                    "os": "string",
                    "hostname": "string"
                },
                "manufacturer": "string",
                "ssid": {
                    "name": "string",
                    "security": "OPEN"
                },
                "wifiStation": {
                    "status": "ONLINE",
                    "vlan": 0,
                    "signal": 0,
                    "band": "band24",
                    "channel": 0
                },
                "user": "string",
                "upload": 0,
                "download": 0
            }
        ]
    }

    # Set up the expected URL and mock response
    endpoint = BASE_URL + \
        ENDPOINTS["GET_AP_CLIENTS_V2"].format(
            site_id=site_id)
    httpx_mock.add_response(url=endpoint, json=mock_data, method="POST")

    # Call the client method
    result = await client.get_ap_clients_v2(site_id, ClientPeriod.field_2h)

    # Validate the result
    expected = from_dict(data_class=APClients,
                         data=mock_data, config=Config(cast=[Enum]))

    assert result == expected


@pytest.mark.asyncio
async def test_get_sw_clients_v2(httpx_mock: HTTPXMock):
    """Test the `get_site_vpn_status` method with specific attributes."""
    client = ZyxelNebulaClient(api_key="dummy_api_key")
    site_id = "site_id"

    # Define the mock data returned by the API
    mock_data = {
        "KeyFields": [
            "macAddress"
        ],
        "data": [
            {
                "macAddress": "string",
                "ipv4Address": "192.168.0.1",
                "lastSeen": 0,
                "connectedTo": "string",
                "connectedPort": "string",
                "firstSeen": 0,
                "description": "string",
                "manufacturer": "string",
                "vlan": 0,
                "lldp": "string"
            }
        ]
    }

    # Set up the expected URL and mock response
    endpoint = BASE_URL + \
        ENDPOINTS["GET_SW_CLIENTS_V2"].format(
            site_id=site_id)
    httpx_mock.add_response(url=endpoint, json=mock_data, method="POST")

    # Call the client method
    result = await client.get_sw_clients_v2(site_id, ClientPeriod.field_2h)

    # Validate the result
    expected = from_dict(data_class=SWClients,
                         data=mock_data, config=Config(cast=[Enum]))

    assert result == expected


@pytest.mark.asyncio
async def test_get_gw_clients_v2(httpx_mock: HTTPXMock):
    """Test the `get_site_vpn_status` method with specific attributes."""
    client = ZyxelNebulaClient(api_key="dummy_api_key")
    site_id = "site_id"

    # Define the mock data returned by the API
    mock_data = {
        "KeyFields": [
            "macAddress"
        ],
        "data": [
            {
                "macAddress": "string",
                "ipv4Address": "192.168.0.1",
                "lastSeen": 0,
                "connectedTo": "string",
                "firstSeen": 0,
                "description": "string",
                "osHostname": {
                    "os": "string",
                    "hostname": "string"
                },
                "manufacturer": "string",
                "interface": "string"
            }
        ]
    }

    # Set up the expected URL and mock response
    endpoint = BASE_URL + \
        ENDPOINTS["GET_GW_CLIENTS_V2"].format(
            site_id=site_id)
    httpx_mock.add_response(url=endpoint, json=mock_data, method="POST")

    # Call the client method
    result = await client.get_gw_clients_v2(site_id, ClientPeriod.field_2h)

    # Validate the result
    expected = from_dict(data_class=GWClients,
                         data=mock_data, config=Config(cast=[Enum]))

    assert result == expected
