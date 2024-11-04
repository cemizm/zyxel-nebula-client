
# Zyxel Nebula API Client

This is an unofficial Python client for interacting with the [Zyxel Nebula API](https://zyxelnetworks.github.io/NebulaOpenAPI/doc/openapi.html), providing access to manage sites, devices, and clients within the Zyxel Nebula environment.

## Features

- Retrieve clients connected to a specific site.
- View device firmware status and client connectivity.
- Manage sites and device groups within the Zyxel Nebula ecosystem.

## Requirements

- Python 3.12 or higher
- An API key for Zyxel Nebula

## Installation

Install the package using [pip](https://pip.pypa.io/en/stable/):

```bash
pip install zyxel-nebula-client
```

## Usage

### Retrieve API key

Login in to Nebula and generate an API token which located at **Site-wide** > **Configure** > **Site settings** is specifically used to generate an API token for DPPSK third-party integration.

### Setup the Client

To begin, initialize the client with your API key:

```python
from zyxel_nebula_client import ZyxelNebulaClient

# Replace 'your_api_key_here' with your actual API key
client = ZyxelNebulaClient(api_key='your_api_key_here')
```

### Example Usage

#### 1. Retrieve Site Clients

To retrieve a list of clients connected to a specific site:

```python
from zyxel_nebula_client import ClientAttributesReq

site_id = "your_site_id"

# Specify the attributes you want to retrieve for each client
attributes = [ClientAttributesReq.mac_address, ClientAttributesReq.ipv4_address]

# Asynchronous call to get site clients
clients = await client.get_site_clients(site_id=site_id, attributes=attributes)

# Print client information
for client in clients:
    print(client)
```

#### 2. Retrieve Organizations
To retrieve a list of organizations associated with your API key, you can use the following code snippet:

```python
# Asynchronous call to get organizations
organizations = await client.get_organizations()

# Print organization information
for org in organizations:
    print(f"Organization ID: {org.org_id}, Name: {org.name}")
```

#### 3. Retrieve Sites for a Specific Organization
To get a list of sites within a specific organization, use this example:

```python
org_id = "your_org_id"

# Asynchronous call to get sites for the specified organization
sites = await client.get_sites(org_id=org_id)

# Print site information
for site in sites:
    print(f"Site ID: {site.site_id}, Name: {site.name}, Location: {site.location}")
```

#### 4. Get Device Firmware Status
To retrieve the firmware status of devices within a specific organization, use this example:

```python
org_id = "your_org_id"

# Asynchronous call to get firmware status
firmware_status = await client.get_device_firmware_status_from_organization(org_id=org_id)

# Print firmware status for each device
for status in firmware_status:
    print(f"Device ID: {status.device_id}, Firmware Version: {status.firmware_version}, Status: {status.status}")
```
## Documentation

For more details, refer to the [Zyxel Nebula API documentation](https://zyxelnetworks.github.io/NebulaOpenAPI/doc/openapi.html).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## Issues

If you encounter any issues or have feature requests, please open an issue in the [GitHub repository](https://github.com/cemizm/zyxel-nebula-client/issues).

## Acknowledgements

- [Zyxel Nebula API](https://zyxelnetworks.github.io/NebulaOpenAPI/doc/openapi.html) for providing the API documentation.
- All contributors who help improve this project.
