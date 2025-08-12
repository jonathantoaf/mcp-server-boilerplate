from datetime import datetime, timezone

from humps.main import camelize
from pydantic import BaseModel


class SharedBaseModel(BaseModel):
    class Config:
        alias_generator = camelize
        # Don't force use of aliases in class instantiation/attribute access
        validate_by_name = True

        # Always serialize datetime in the ISO 8601 format, to preserve timezones
        json_encoders = {
            datetime: lambda date_time: (
                date_time.replace(tzinfo=timezone.utc).isoformat()
                if not date_time.tzinfo
                else date_time.isoformat()
            ),
        }
