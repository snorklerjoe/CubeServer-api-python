"""Classes for holding data"""

from abc import ABC, abstractmethod
from enum import Enum, unique
from typing import Union
import json


__all__ = [
    "DataClass",
    "DataPoint",
    "Temperature",
    "Humidity",
    "Pressure",
    "Intensity",
    "Text"
]

@unique
class DataClass(Enum):
    TEMPERATURE = "temperature"
    HUMIDITY = "humidity"
    PRESSURE = "pressure"
    LIGHT_INTENSITY = "lux"
    COMMENT = "txt"

class DataPoint(ABC):
    """A class for storing and handling datapoints"""

    @staticmethod
    @property
    @abstractmethod
    def UNIT() -> str:
        """A standard string representation of the unit for this datapoint"""

    def __init__(self, data_class: DataClass, value: Union[int, float, str]):
        """Initializes a piece of data to send to the server"""
        self.data_class = data_class
        self.value = value

    def dumps(self) -> str:
        """Dumps a JSON string out that the server will (hopefully) accept"""
        return json.dumps(
            {
                "type": self.data_class,
                "value": self.value
            }
        )

    def __str__(self) -> str:
        return f"{self.value} {self.UNIT}"

class Temperature(DataPoint):
    """A class for DataPoints that store temperature values"""
    UNIT = u"\N{DEGREE SIGN}F"
    def __init__(self, value: Union[int, float]):
        super().__init__(DataClass.TEMPERATURE, value)

class Humidity(DataPoint):
    """A class for DataPoints that store humidity values"""
    UNIT = "%"
    def __init__(self, value: Union[int, float]):
        super().__init__(DataClass.HUMIDITY, value)

class Pressure(DataPoint):
    """A class for DataPoints that store barometric pressure values"""
    UNIT="inHg"
    def __init__(self, value: Union[int, float]):
        super().__init__(DataClass.PRESSURE, value)

class Intensity(DataPoint):
    """A class for DataPoints that store light intensity values"""
    UNIT="lux"
    def __init__(self, value: Union[int, float]):
        super().__init__(DataClass.LIGHT_INTENSITY, value)

class Text(DataPoint):
    """A class reserved for DataPoints that are intended as a text comment"""
    UNIT=""  # No unit for regular strings of text
    def __init__(self, value: str):
        super().__init__(DataClass.COMMENT, value)
