#!/usr/bin/env python3
"""
Apex Module F1018: Dual-Tier Pricing & Product Line Engine
Handles $5.0M Sovereign Flight Model and Future Affordable Road Model.
"""

class ApexProductCatalog:
    def __init__(self):
        self.production_cost_flight = 2500000.0  # $2.5M Unit Cost

    def evaluate_sale_offer(self, model_type: str, offer_price_usd: float) -> dict:
        """Evaluates sale request against $5.0M base / $4.5M floor limits."""
        if model_type == "APEX_SOVEREIGN_FLIGHT":
            if offer_price_usd >= 4500000.0:
                profit = offer_price_usd - self.production_cost_flight
                return {
                    "model": "APEX_SOVEREIGN (Flight + AI)",
                    "agreed_price": f"${offer_price_usd:,.2f}",
                    "status": "SALE_APPROVED",
                    "net_profit_per_unit": f"${profit:,.2f}",
                    "target_buyer": "Elite / High-Net-Worth Investor"
                }
            else:
                return {
                    "model": "APEX_SOVEREIGN (Flight + AI)",
                    "offered_price": f"${offer_price_usd:,.2f}",
                    "status": "OFFER_DENIED",
                    "reason": "Price below minimum floor of $4.5M. Preserving brand exclusivity."
                }
        elif model_type == "APEX_ROAD_CIVILIAN":
            return {
                "model": "APEX ROAD (Ground-Only EV)",
                "status": "FUTURE_MASS_PRODUCTION_CONCEPT",
                "flight_capability": "DISABLED",
                "target_buyer": "Everyday Consumers"
            }

if __name__ == "__main__":
    catalog = ApexProductCatalog()
    print("Flight Test ($5.0M Base):", catalog.evaluate_sale_offer("APEX_SOVEREIGN_FLIGHT", 5000000.0))
    print("Flight Test ($4.5M Floor):", catalog.evaluate_sale_offer("APEX_SOVEREIGN_FLIGHT", 4500000.0))
    print("Flight Test (Lowball $3.0M):", catalog.evaluate_sale_offer("APEX_SOVEREIGN_FLIGHT", 3000000.0))
    print("Civilian Road Test:", catalog.evaluate_sale_offer("APEX_ROAD_CIVILIAN", 45000.0))
