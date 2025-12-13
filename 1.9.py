###
# Prints vehicle registration numbers from Krakow
#

polish_license_plates = [
    'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
    'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8059Q',
    'KK54985', 'LU4864U'
]

numer = 1
for car_number in polish_license_plates:
    if car_number.startswith("KR") or car_number.startswith("KK"):
        print(numer, car_number)
        numer += 1