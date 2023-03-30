def calculate_month_electric_cost(month_kwh, tier1_cutoff, tier1_cost, tier2_cutoff, tier2_cost, tier3_cost):
    remaining_kwh = month_kwh
    month_cost = 0.0

    if remaining_kwh > (tier2_cutoff + tier1_cutoff):
        tier_kwh = remaining_kwh - (tier2_cutoff + tier1_cutoff)
        month_cost += tier_kwh * tier3_cost
        remaining_kwh -= tier_kwh

    if remaining_kwh > tier1_cutoff:
        tier_kwh = remaining_kwh - tier1_cutoff
        month_cost += tier_kwh * tier2_cost
        remaining_kwh -= tier_kwh

    month_cost += remaining_kwh * tier1_cost
    return month_cost
month_kwh = float(input())
tier1_cutoff, tier2_cutoff = map(float, input().split())
tier1_cost, tier2_cost, tier3_cost = map(float, input().split())

month_cost = calculate_month_electric_cost(month_kwh, tier1_cutoff, tier1_cost, tier2_cutoff, tier2_cost, tier3_cost)
print(f"${month_cost:.2f}")