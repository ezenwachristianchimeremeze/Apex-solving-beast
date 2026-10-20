#!/usr/bin/env python3
"""
Apex Module F1021: Defense Tier & Subscription Management Engine
Handles Beast 2.5 ($5k), Beast Pro ($15k), and Master X ($25k) tiers.
"""

class ApexDefenseTierEngine:
    def __init__(self):
        self.tiers = {
            "2.5": {
                "name": "Apex Beast 2.5",
                "monthly_fee": 5000.0,
                "defense_level": "Level 1: Kevlar Panels & Radar Warning",
                "repair_coverage": "100% Free Standard Repairs"
            },
            "PRO": {
                "name": "Apex Beast Pro",
                "monthly_fee": 15000.0,
                "defense_level": "Level 2: Ballistic Armor & Anti-Drone Jammer",
                "repair_coverage": "100% Free Repairs + Priority Service"
            },
            "MASTER_X": {
                "name": "Apex Beast Master X",
                "monthly_fee": 25000.0,
                "defense_level": "Level 3: Self-Healing Armor, EMP Shielding & Sub-Orbital Ceiling",
                "repair_coverage": "100% Free Repairs + Instant Vehicle Swap"
            }
        }

    def select_subscription_plan(self, tier_key: str) -> dict:
        """Validates tier selection and displays defense specs."""
        tier = self.tiers.get(tier_key.upper())
        if tier:
            return {
                "plan_selected": tier["name"],
                "monthly_cost": f"${tier['monthly_fee']:,.2f} / month",
                "defense_capabilities": tier["defense_level"],
                "out_of_pocket_repair": "$0.00 (FREE)",
                "status": "SUBSCRIPTION_ACTIVE"
            }
        else:
            return {"status": "INVALID_TIER", "available_tiers": ["2.5", "PRO", "MASTER_X"]}

if __name__ == "__main__":
    engine = ApexDefenseTierEngine()
    print("\n=== APEX SUBSCRIPTION TIER TEST ===")
    print("Tier 2.5 Test :", engine.select_subscription_plan("2.5"))
    print("Tier Pro Test :", engine.select_subscription_plan("pro"))
    print("Tier Master X :", engine.select_subscription_plan("master_x"))
    print("===================================\n")
