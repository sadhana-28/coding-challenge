def calculate_overall_and_chemical_free_sales():
    """
    Calculates:
    1. Overall sales from all crops
    2. Sales from chemical-free farming at the end of 11 months

    Returns:
    tuple: (overall_sales, chemical_free_sales)
    """

    TOTAL_LAND = 80
    SEGMENTS = 5
    LAND_PER_SEGMENT = TOTAL_LAND / SEGMENTS  # 16 acres

    # ---------------- Tomato ----------------
    tomato_area = LAND_PER_SEGMENT
    tomato_30_area = 0.30 * tomato_area
    tomato_70_area = 0.70 * tomato_area

    tomato_yield = (tomato_30_area * 10) + (tomato_70_area * 12)  # tonnes
    tomato_sales = tomato_yield * 1000 * 7  # Rs/kg

    # ---------------- Potato ----------------
    potato_yield = LAND_PER_SEGMENT * 10  # tonnes
    potato_sales = potato_yield * 1000 * 20

    # ---------------- Cabbage ----------------
    cabbage_yield = LAND_PER_SEGMENT * 14  # tonnes
    cabbage_sales = cabbage_yield * 1000 * 24

    # ---------------- Sunflower ----------------
    sunflower_yield = LAND_PER_SEGMENT * 0.7  # tonnes
    sunflower_sales = sunflower_yield * 1000 * 200

    # ---------------- Sugarcane ----------------
    sugarcane_yield = LAND_PER_SEGMENT * 45  # tonnes
    sugarcane_sales = sugarcane_yield * 4000  # Rs/tonne

    # ---------------- Totals ----------------
    overall_sales = (
        tomato_sales
        + potato_sales
        + cabbage_sales
        + sunflower_sales
        + sugarcane_sales
    )

    chemical_free_sales = (
        tomato_sales
        + potato_sales
        + cabbage_sales
        + sunflower_sales
    )

    return overall_sales, chemical_free_sales


if __name__ == "__main__":
    overall, chemical_free = calculate_overall_and_chemical_free_sales()

    print(f"Overall Sales from 80 acres: ₹{overall:,.2f}")
    print(f"Chemical-free Sales at end of 11 months: ₹{chemical_free:,.2f}")
