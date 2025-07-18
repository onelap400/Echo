
"""Projection models for 400 m performance.

These formulas are *illustrative*. Replace coefficients with updated values
if your calibration changes.

Inputs are expressed in seconds.
"""

def project_5x200(avg_200_time: float) -> float:
    """Vince Anderson model: 400 m = avg_200_time / 0.524"""
    if avg_200_time <= 0:
        return None
    return round(avg_200_time / 0.524, 2)

def project_fly30(fly30_time: float) -> float:
    """Simple linear heuristic: 400 m ≈ fly30_time × 16.

    (Based on empirical link: 2.75 s → 44.0 s; adjust as needed.)
    """
    if fly30_time <= 0:
        return None
    return round(fly30_time * 16, 2)

def project_split400(total_split: float) -> float:
    """Split‑400 workout model: use the workout total as projection."""
    return round(total_split, 2) if total_split > 0 else None

def project_asr(asr_estimate: float) -> float:
    """Anaerobic Speed Reserve projection entered directly."""
    return round(asr_estimate, 2) if asr_estimate > 0 else None

def combined_projection(row: dict) -> float:
    """Mean of available model outputs."""
    preds = [p for p in [
        project_5x200(row.get('avg_200')),
        project_fly30(row.get('fly30')),
        project_split400(row.get('split400_total')),
        project_asr(row.get('asr_proj'))
    ] if p]
    return round(sum(preds) / len(preds), 2) if preds else None
