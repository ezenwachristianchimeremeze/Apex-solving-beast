#!/usr/bin/env python3
"""
Apex Module F1022: Onboard AI Voice Payment & Tier Explanation Engine
Updated with 5k (Paid repairs), 15k (Free repairs), and 25k (Free repairs + Crash swap).
"""

class ApexVoicePaymentEngine:
    def __init__(self):
        self.tiers_info = {
            "2.5": {
                "monthly": 5000,
                "annual": 60000,
                "repairs": "Repairs are NOT free (Owner pays maintenance costs).",
                "purpose": "Kevlar armor, basic radar, and automatic VTOL flight."
            },
            "PRO": {
                "monthly": 15000,
                "annual": 180000,
                "repairs": "100% FREE lifetime repairs and routine maintenance.",
                "purpose": "Ballistic armor, anti-drone jammer, and EMP shielding."
            },
            "MASTER_X": {
                "monthly": 25000,
                "annual": 300000,
                "repairs": "100% FREE repairs PLUS instant full car replacement if crashed.",
                "purpose": "Self-healing armor, quantum vision, and sub-orbital ceiling."
            }
        }

    def trigger_voice_payment_warning(self, payment_status: str, selected_tier: str) -> dict:
        """Triggers voice prompts and explains updated repair coverage and subscription rates."""
        if payment_status == "OVERDUE":
            tier_data = self.tiers_info.get(selected_tier.upper(), self.tiers_info["2.5"])
            
            speech_script = (
                f"Attention, Boss. Your subscription payment is currently past due. "
                f"Flight systems are restricted until payment is confirmed. "
                f"Your plan details: ${tier_data['monthly']:,}/month or ${tier_data['annual']:,}/year. "
                f"Hardware Included: {tier_data['purpose']} "
                f"Repair Policy: {tier_data['repairs']} "
                f"Please press 'Pay Now' on your display screen to authorize and resume flight."
            )
            
            return {
                "flight_lock_status": "RESTRICTED_GROUND_ONLY",
                "voice_prompt_text": speech_script,
                "screen_action": "DISPLAY_PAYMENT_GATEWAY",
                "status": "VOICE_TRIGGER_ACTIVE"
            }
        
        return {"flight_lock_status": "UNLOCKED", "status": "PAYMENT_UP_TO_DATE"}

if __name__ == "__main__":
    engine = ApexVoicePaymentEngine()
    
    print("\n=======================================================")
    print("      APEX VOICE PAYMENT LOCK & REPAIR POLICY TEST     ")
    print("=======================================================\n")
    
    for tier_code in ["2.5", "PRO", "MASTER_X"]:
        result = engine.trigger_voice_payment_warning("OVERDUE", tier_code)
        print(f"--- TIER {tier_code} OVERDUE NOTICE ---")
        print(f"Script Voice Text:\n\"{result['voice_prompt_text']}\"\n")

    print("=======================================================\n")
