from pydantic import BaseModel

class SunTrack(BaseModel):
    latitude: float
    longitude: float
    timezone: str
    sunrise_time_utc: float
    sunset_time_utc: float
    sun_apparent_angle_at_noon: float
    sun_surface_angle_at_noon: float
    sun_intensity: float