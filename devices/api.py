from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from .models import Device, Location
from .schemas import LocationSchema, DeviceSchema, CreateDeviceSchema, ErrorSchema, DeviceLocationPatch
app = NinjaAPI()


@app.get('devices/', response=list[DeviceSchema])
def get_devices(request):
    return Device.objects.all()


@app.get('devices/{slug}/', response=DeviceSchema)
def get_device(request, slug: str):
    device = get_object_or_404(Device, slug=slug)
    return device


@app.post('devices/', response={200: DeviceSchema, 404: ErrorSchema})
def create_device(request, device: CreateDeviceSchema):

    if device.location_id:
        location_exist = Location.objects.filter(
            id=device.location_id).exists()
        if not location_exist:
            return 404, {"message": "This Location does not exist"}
    device_data = device.model_dump()
    model_data = Device.objects.create(**device_data)
    return model_data


@app.post('devices/{device_slug}/set-location', response=DeviceSchema)
def update_device_location(request, device_slug: str, location: DeviceLocationPatch):
    device = get_object_or_404(Device, slug=device_slug)
    if location.location_id:
        location = get_object_or_404(Location, pk=location.location_id)
        device.location = location
    else:
        device.location = None
    return device


@app.get('locations/', response=list[LocationSchema])
def get_locations(request):
    return Location.objects.all()
