def check_edema_risk(current_ohm, baseline_ohm):
    """
    Ohm değerindeki düşüşe göre ödem riskini hesaplar.
    Düşüş ne kadar fazlaysa sıvı birikimi o kadar yüksektir.
    """
    drop_percentage = ((baseline_ohm - current_ohm) / baseline_ohm) * 100
    
    if drop_percentage >= 20:
        return "CRITICAL: Emergency Alert! Potential Pulmonary Edema."
    elif drop_percentage >= 10:
        return "WARNING: Edema detected. Notify medical staff."
    else:
        return "STABLE: Patient is within normal range."

# Örnek kullanım:
# print(check_edema_risk(400, 500)) # %20 düşüş senaryosu
