"""MeinVodafone Entities."""

import logging

from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.components.sensor.const import UnitOfInformation, UnitOfTime
from homeassistant.helpers.entity import EntityCategory

from .MeinVodafoneContract import MeinVodafoneContract

_LOGGER = logging.getLogger(__name__)


class BaseEntity:
    """Base class for all components."""

    contract: MeinVodafoneContract

    def __init__(
        self,
        component,
        attr: str,
        name: str,
        icon: str | None = None,
        plan_name: str | None = None,
        entity_type: EntityCategory | None = None,
        device_class: str | None = None,
        state_class: str | None = None,
        display_precision: int | None = None,
    ) -> None:
        """Init."""
        self.attr = attr
        self.component = component
        self.name = name
        self.icon = icon
        self.plan_name = plan_name
        self.entity_type = entity_type
        self.device_class = device_class
        self.state_class = state_class
        self.display_precision = display_precision

    def setup(self, contract: MeinVodafoneContract) -> bool:
        """Set up entity if supported."""
        self.contract = contract
        if not self.is_supported:
            _LOGGER.debug("%s %s is not supported", type(self).__name__, self.attr)
            return False

        _LOGGER.debug("%s %s is supported", type(self).__name__, self.attr)
        return True

    @property
    def is_supported(self) -> bool:
        """Check entity is supported."""
        supported = "is_" + self.attr + "_supported"
        if hasattr(self.contract, supported):
            return getattr(self.contract, supported)
        return False


class Sensor(BaseEntity):
    """Base class for sensor type entities."""

    def __init__(
        self,
        attr: str,
        name: str,
        icon: str | None,
        unit: str | None,
        plan_name: str | None = None,
        entity_type: EntityCategory | None = None,
        device_class: SensorDeviceClass | None = None,
        state_class: SensorStateClass | None = None,
        display_precision: int | None = None,
    ) -> None:
        """Init."""
        super().__init__(
            component="sensor",
            attr=attr,
            name=name,
            icon=icon,
            plan_name=plan_name,
            entity_type=entity_type,
            device_class=device_class,
            state_class=state_class,
            display_precision=display_precision,
        )
        self.unit = unit


def create_entities():
    """Return list of all entities."""
    return [
        Sensor(
            attr="primary_minutes_remaining",
            name="Primary minutes remaining",
            icon="mdi:clock-plus",
            unit=UnitOfTime.MINUTES,
            device_class=SensorDeviceClass.DURATION,
            plan_name="primary_minutes_name",
            state_class=SensorStateClass.MEASUREMENT,
            display_precision=0,
        ),
        Sensor(
            attr="primary_minutes_used",
            name="Primary minutes used",
            icon="mdi:clock-minus",
            unit=UnitOfTime.MINUTES,
            device_class=SensorDeviceClass.DURATION,
            plan_name="primary_minutes_name",
            state_class=SensorStateClass.MEASUREMENT,
            display_precision=0,
        ),
        Sensor(
            attr="primary_minutes_total",
            name="Primary minutes total",
            icon="mdi:clock-check",
            unit=UnitOfTime.MINUTES,
            device_class=SensorDeviceClass.DURATION,
            plan_name="primary_minutes_name",
            state_class=SensorStateClass.MEASUREMENT,
            display_precision=0,
        ),
        Sensor(
            attr="secondary_minutes_remaining",
            name="Secondary minutes remaining",
            icon="mdi:clock-plus",
            unit=UnitOfTime.MINUTES,
            device_class=SensorDeviceClass.DURATION,
            plan_name="secondary_minutes_name",
            state_class=SensorStateClass.MEASUREMENT,
            display_precision=0,
        ),
        Sensor(
            attr="secondary_minutes_used",
            name="Secondary minutes used",
            icon="mdi:clock-minus",
            unit=UnitOfTime.MINUTES,
            device_class=SensorDeviceClass.DURATION,
            plan_name="secondary_minutes_name",
            state_class=SensorStateClass.MEASUREMENT,
            display_precision=0,
        ),
        Sensor(
            attr="secondary_minutes_total",
            name="Secondary minutes total",
            icon="mdi:clock-check",
            unit=UnitOfTime.MINUTES,
            device_class=SensorDeviceClass.DURATION,
            plan_name="secondary_minutes_name",
            state_class=SensorStateClass.MEASUREMENT,
            display_precision=0,
        ),
        Sensor(
            attr="primary_sms_remaining",
            name="Primary SMS remaining",
            icon="mdi:message-plus",
            unit="sms",
            plan_name="primary_sms_name",
            state_class=SensorStateClass.MEASUREMENT,
        ),
        Sensor(
            attr="primary_sms_used",
            name="Primary SMS used",
            icon="mdi:message-minus",
            unit="sms",
            plan_name="primary_sms_name",
            state_class=SensorStateClass.MEASUREMENT,
        ),
        Sensor(
            attr="primary_sms_total",
            name="Primary SMS total",
            icon="mdi:message-check",
            unit="sms",
            plan_name="primary_sms_name",
            state_class=SensorStateClass.MEASUREMENT,
        ),
        Sensor(
            attr="secondary_sms_remaining",
            name="Secondary SMS remaining",
            icon="mdi:message-plus",
            unit="sms",
            plan_name="secondary_sms_name",
            state_class=SensorStateClass.MEASUREMENT,
        ),
        Sensor(
            attr="secondary_sms_used",
            name="Secondary SMS used",
            icon="mdi:message-minus",
            unit="sms",
            plan_name="secondary_sms_name",
            state_class=SensorStateClass.MEASUREMENT,
        ),
        Sensor(
            attr="secondary_sms_total",
            name="Secondary SMS total",
            icon="mdi:message-check",
            unit="sms",
            plan_name="secondary_sms_name",
            state_class=SensorStateClass.MEASUREMENT,
        ),
        Sensor(
            attr="primary_data_remaining",
            name="Primary data remaining",
            icon="mdi:web-plus",
            unit=UnitOfInformation.MEBIBYTES,
            device_class=SensorDeviceClass.DATA_SIZE,
            plan_name="primary_data_name",
            state_class=SensorStateClass.MEASUREMENT,
        ),
        Sensor(
            attr="primary_data_used",
            name="Primary data used",
            icon="mdi:web-minus",
            unit=UnitOfInformation.MEBIBYTES,
            device_class=SensorDeviceClass.DATA_SIZE,
            plan_name="primary_data_name",
            state_class=SensorStateClass.MEASUREMENT,
        ),
        Sensor(
            attr="primary_data_total",
            name="Primary data total",
            icon="mdi:web-check",
            unit=UnitOfInformation.MEBIBYTES,
            device_class=SensorDeviceClass.DATA_SIZE,
            plan_name="primary_data_name",
            state_class=SensorStateClass.MEASUREMENT,
        ),
        Sensor(
            attr="secondary_data_remaining",
            name="Secondary data remaining",
            icon="mdi:web-plus",
            unit=UnitOfInformation.MEBIBYTES,
            device_class=SensorDeviceClass.DATA_SIZE,
            plan_name="secondary_data_name",
            state_class=SensorStateClass.MEASUREMENT,
        ),
        Sensor(
            attr="secondary_data_used",
            name="Secondary data used",
            icon="mdi:web-minus",
            unit=UnitOfInformation.MEBIBYTES,
            device_class=SensorDeviceClass.DATA_SIZE,
            plan_name="secondary_data_name",
            state_class=SensorStateClass.MEASUREMENT,
        ),
        Sensor(
            attr="secondary_data_total",
            name="Secondary data total",
            icon="mdi:web-check",
            unit=UnitOfInformation.MEBIBYTES,
            device_class=SensorDeviceClass.DATA_SIZE,
            plan_name="secondary_data_name",
            state_class=SensorStateClass.MEASUREMENT,
        ),
        Sensor(
            attr="billing_current_summary",
            name="Billing currect summary",
            icon="mdi:credit-card-search",
            unit="€",
            state_class=SensorStateClass.MEASUREMENT,
        ),
        Sensor(
            attr="billing_last_summary",
            name="Billing last summary",
            icon="mdi:credit-card-clock",
            unit="€",
            state_class=SensorStateClass.MEASUREMENT,
        ),
        Sensor(
            attr="billing_cycle_days",
            name="Billing cycle days",
            icon="mdi:credit-card-sync",
            unit=UnitOfTime.DAYS,
            device_class=SensorDeviceClass.DURATION,
            state_class=SensorStateClass.MEASUREMENT,
            display_precision=0,
        ),
    ]


class MeinVodafoneEntities:
    """Class for accessing the entities."""

    def __init__(self, contract) -> None:
        """Initialize instruments."""
        self.entities_list = [
            entity for entity in create_entities() if entity.setup(contract)
        ]
