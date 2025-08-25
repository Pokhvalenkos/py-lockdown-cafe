class VaccineError(Exception):
    def __str__(self) -> str:
        return "Visitors hav problems with their vaccine"


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "NotVaccinatedError, some visitor/s do not have vaccination"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "OutdatedVaccineError, some visitor/s have expired vaccination"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "NotWearingMaskError, some visitor/s do not wear a mask"
