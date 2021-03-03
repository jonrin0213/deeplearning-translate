import typing

from ._pairs import _PAIRS_MBART50

# types
WEIGHTS_TYPES = typing.Literal["mbart50", "mbart-large-50-many-to-many-mmt"]

# Weights dictionaries
__MBART50 = {
    "langs": tuple(pair[0] for pair in _PAIRS_MBART50),
    "codes": tuple(pair[1] for pair in _PAIRS_MBART50),
    "pairs": _PAIRS_MBART50,
}


def _dict_from_weights(weights: WEIGHTS_TYPES) -> dict:
    """Returns a dictionary of lang, codes, pairs if the provided weights is supported."""
    if weights.lower() in ["mbart50", "mbart-large-50-many-to-many-mmt"]:
        return dict(_PAIRS_MBART50)
    else:
        error_message = f"Incorrect argument '{weights}' for parameter weights. Currently, only 'mbart50' is available."
        raise ValueError(error_message)


def get_lang_code_map(weights: WEIGHTS_TYPES = "mbart50"):
    return _dict_from_weights(weights)["pairs"]


def available_languages(weights: WEIGHTS_TYPES = "mbart50"):
    return _dict_from_weights(weights)["langs"]


def available_codes(weights: WEIGHTS_TYPES = "mbart50"):
    return _dict_from_weights(weights)["codes"]
