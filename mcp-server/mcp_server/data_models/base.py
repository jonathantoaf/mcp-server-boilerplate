from datetime import datetime, timezone
from humps.main import camelize
from pydantic import BaseModel, ConfigDict


class SharedBaseModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=camelize,
        # Don't force use of aliases in class instantiation/attribute access
        populate_by_name=True,
        # Always serialize datetime in the ISO 8601 format, to preserve timezones
        json_encoders={
            datetime: lambda date_time: (
                date_time.replace(tzinfo=timezone.utc).isoformat()
                if not date_time.tzinfo
                else date_time.isoformat()
            ),
        },
    )
