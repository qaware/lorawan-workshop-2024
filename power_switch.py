import asyncio
import os
import logging
from enum import Enum
from contextlib import asynccontextmanager
from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager

class PowerState(Enum):
    ON = 'on'
    OFF = 'off'

class PowerPlug:
    def __init__(self, email, password, device_name):
        if not email or not password:
            raise ValueError("Email and password must be provided")
        self.email = email
        self.password = password
        self.device_name = device_name

    @asynccontextmanager
    async def _manager_context(self):
        http_api_client = None
        manager = None
        try:
            http_api_client = await MerossHttpClient.async_from_user_password(
                api_base_url='https://iotx-eu.meross.com',
                email=self.email,
                password=self.password
            )
            manager = MerossManager(http_client=http_api_client)
            await manager.async_device_discovery()
            yield manager
        finally:
            if manager:
                await asyncio.sleep(2)
                manager.close()
                await http_api_client.async_logout()

    async def _set_powered(self, powered: bool):
        async with self._manager_context() as manager:
            plugs = manager.find_devices(device_name=self.device_name)
            if len(plugs) < 1:
                raise ValueError(f"No power plugs found with name {self.device_name}")

            device = plugs[0]
            await device.async_update()

            if powered:
                print(f"Turning on {device.name}...")
                await device.async_turn_on()
            else:
                print(f"Turning off {device.name}...")
                await device.async_turn_off()    

    def set_power_state(self, power_state: PowerState):
        asyncio.run(self._set_powered(PowerState.ON == power_state))

# Example usage
if __name__ == "__main__":
    plug = PowerPlug(email=EMAIL, password=PASSWORD, device_name=DEVICE_NAME)
    plug.set_power_state(PowerState.ON)
