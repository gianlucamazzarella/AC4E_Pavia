"""Small synthetic economics example for the Pavia workshop."""

from __future__ import annotations

import numpy as np
import pandas as pd


def make_phillips_curve_data(n: int = 40, seed: int = 42) -> pd.DataFrame:
    """Create synthetic unemployment and inflation data.

    Args:
        n: Number of observations.
        seed: Random seed for reproducibility.

    Returns:
        DataFrame with `unemployment` and `inflation` columns.
    """
    rng = np.random.default_rng(seed)
    unemployment = rng.normal(loc=6.0, scale=1.1, size=n)
    shock = rng.normal(loc=0.0, scale=0.3, size=n)
    inflation = 4.0 - 0.35 * unemployment + shock
    return pd.DataFrame({"unemployment": unemployment, "inflation": inflation})


def ols_slope(x: np.ndarray, y: np.ndarray) -> float:
    """Estimate the slope coefficient from a one-regressor OLS model.

    Args:
        x: Regressor values.
        y: Outcome values.

    Returns:
        OLS slope coefficient.
    """
    x_centered = x - x.mean()
    y_centered = y - y.mean()
    return float((x_centered @ y_centered) / (x_centered @ x_centered))


def summarize_relationship(data: pd.DataFrame) -> dict[str, float]:
    """Summarize the unemployment-inflation relationship."""
    slope = ols_slope(data["unemployment"].to_numpy(), data["inflation"].to_numpy())
    return {
        "n": float(len(data)),
        "mean_unemployment": float(data["unemployment"].mean()),
        "mean_inflation": float(data["inflation"].mean()),
        "ols_slope": slope,
    }


def main() -> None:
    """Run the example analysis and print a compact summary."""
    data = make_phillips_curve_data()
    summary = summarize_relationship(data)
    for key, value in summary.items():
        print(f"{key}: {value:.3f}")


if __name__ == "__main__":
    main()
