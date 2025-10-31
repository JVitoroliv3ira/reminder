from dataclasses import dataclass
from datetime import datetime
import re

_TIMEZONE_REGEX = re.compile(r"^[A-Za-z_]+/[A-Za-z_]+$")

@dataclass(frozen=True, slots=True)
class ScheduleIntent:
    raw_text: str
    anchor_dt: datetime 
    timezone: str

    def __post_init__(self) -> None:

        if not self.raw_text or self.raw_text.strip() == "":
            raise ValueError("raw_text não pode ser vazio")

        if not self.timezone or self.timezone.strip() == "":
            raise ValueError("timezone não pode ser vazio")

        if not _TIMEZONE_REGEX.match(self.timezone):
            raise ValueError(
                f'timezone "{self.timezone}" inválido. Esperado formato "Regiao/Cidade", ex.: "America/Fortaleza".'
            )

        if not isinstance(self.anchor_dt, datetime):
            raise ValueError("anchor_dt deve ser datetime válido")


