import pytest
from datetime import datetime, timezone
from reminder.domain.schedule_intent import ScheduleIntent

def make_datetime(y, m, d, h, mm, tzinfo=timezone.utc) -> datetime:
    return datetime(y, m, d, h, mm, tzinfo=tzinfo)

def test_schedule_intent_valid_creation():
    intent = ScheduleIntent(
        raw_text="amanhã às 9h",
        anchor_dt=make_datetime(2025, 10, 30, 21, 30),
        timezone="America/Fortaleza"
    )

    assert intent.raw_text == "amanhã às 9h"
    assert intent.anchor_dt == make_datetime(2025, 10, 30, 21, 30)
    assert intent.timezone == "America/Fortaleza"



def test_schedule_intent_rejects_empty_raw_text():
    with pytest.raises(ValueError):
        ScheduleIntent(
            raw_text="",
            anchor_dt=make_datetime(2025, 10, 30, 21, 30),
            timezone="America/Fortaleza"
        )

def test_schedule_intent_rejects_invalid_timezone_no_slash():
    with pytest.raises(ValueError):
        ScheduleIntent(
            raw_text="amanhã 9h",
            anchor_dt=make_datetime(2025, 10, 31, 12, 0),
            timezone="America",  
        )

def test_schedule_intent_rejects_invalid_timezone_empty():
    with pytest.raises(ValueError):
        ScheduleIntent(
            raw_text="amanhã 9h",
            anchor_dt=make_datetime(2025, 10, 31, 12, 0),
            timezone="",
        )

def test_schedule_intent_is_immutable():
    intent = ScheduleIntent(
        raw_text="amanhã 9h",
        anchor_dt=make_datetime(2025, 10, 31, 12, 0),
        timezone="America/Fortaleza",
    )

    with pytest.raises(AttributeError):
        intent.raw_text = "outra coisa"
