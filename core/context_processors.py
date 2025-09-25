DIENSTEN = [
    "Schilderwerk", "Elektra", "Tegelwerk", "Stucwerk",
    "Badkamer renovatie", "Keuken montage", "Vloeren", "Dakwerk",
]

def site_constants(request):
    return {"DIENSTEN": DIENSTEN}

from .constants import SERVICES_TICKER
def diensten_ticker(request):
    return {"diensten": SERVICES_TICKER}