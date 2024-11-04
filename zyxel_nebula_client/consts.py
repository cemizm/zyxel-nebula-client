BASE_URL = "https://api.nebula.zyxel.com"

# Endpoints
ENDPOINTS = {
    # groups
    "GET_GROUPS": "/v1/nebula/groups",
    "GET_ORGANIZATIONS_FROM_GROUP": "/v1/nebula/groups/{group_id}/organizations",

    # organization
    "GET_ORGANIZATIONS": "/v1/nebula/organizations",
    "GET_ORGANIZATION_INFO": "/v1/nebula/organizations/{org_id}",
    "GET_SITES": "/v1/nebula/organizations/{org_id}/sites",
    "GET_DEVICES_FROM_ORGANIZATION": "/v1/nebula/organizations/{org_id}/sites/devices",
    "GET_DEVICE_FIRMWARE_STATUS_FROM_ORGANIZATION": "/v1/nebula/organizations/{org_id}/firmware-status",

    # sites
    "GET_DEVICE_FIRMWARE_STATUS_FROM_SITE": "/v1/nebula/{site_id}/firmware-status",
    "GET_DEVICES_ONLINE_BY_TYPE": "/v1/nebula/{site_id}/online-status",
    "GET_SITE_VPN_STATUS": "/v1/nebula/{site_id}/vpn-status",
    "GET_SITE_CLIENTS": "/v1/nebula/{site_id}/clients",
    "GET_AP_CLIENTS": "/v1/nebula/{site_id}/ap-clients",
    "PING": "/v1/nebula/{site_id}/livetool/{device_id}/ping",
    "REBOOT": "/v1/nebula/{site_id}/livetool/{device_id}/reboot",
    "CABLE_TEST": "/v1/nebula/{site_id}/livetool/{device_id}/cable-test",
    "CONNECTIVITY": "/v1/nebula/{site_id}/{device_id}/connectivity",
    "GET_SITE_CLIENTS_V2": "/v2/nebula/{site_id}/clients",
    "GET_AP_CLIENTS_V2": "/v2/nebula/{site_id}/ap-clients",
    "GET_SW_CLIENTS_V2": "/v2/nebula/{site_id}/sw-clients",
    "GET_GW_CLIENTS_V2": "/v2/nebula/{site_id}/gw-clients",
}
