def CostForMilesGas(milesDriven):
    MILES_PER_GAL = 30
    CENTS_PER_GAL = 400

    centsGas = (milesDriven * CENTS_PER_GAL) // MILES_PER_GAL
    return centsGas

def CostForMilesMaintenance(milesDriven):
    TIRES_CENTS = 50000
    TIRES_MILES = 20000
    SERVICE_CENTS = 30000
    SERVICE_MILES = 10000

    centsMaintenance = ((milesDriven * TIRES_CENTS) // TIRES_MILES) + ((milesDriven * SERVICE_CENTS) // SERVICE_MILES)
    return centsMaintenance
def CostForMiles(milesDriven):
    return CostForMilesGas(milesDriven) + CostForMilesMaintenance(milesDriven)

milesDriven = int(input())
print(CostForMiles(milesDriven), "cents")