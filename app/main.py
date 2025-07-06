from .cafe import Cafe
from .errors import (NotWearingMaskError, VaccineError)


def go_to_cafe(friends: list, cafe: Cafe) -> str:

    not_vaccinated = 0
    masks_to_buy = 0
    friends_count = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            not_vaccinated += 1
        except NotWearingMaskError:
            masks_to_buy += 1
        else:
            friends_count += 1

    if not_vaccinated > 0:
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    elif friends_count == len(friends):
        return f"Friends can go to {cafe.name}"
