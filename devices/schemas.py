from ninja import ModelSchema, Schema
from .models import Device, Location
# from typing import Union


class LocationSchema(ModelSchema):
    class Meta:
        model = Location
        fields = ("id", "name")


class DeviceSchema(ModelSchema):
    location: LocationSchema | None = None

    class Meta:
        model = Device
        fields = ("id", "name", "slug", "location")


class CreateDeviceSchema(Schema):
    name: str
    location_id: int | None = None


class ErrorSchema(Schema):
    message: str


class DeviceLocationPatch(Schema):
    location_id: int | None = None
