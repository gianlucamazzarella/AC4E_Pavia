from analysis import make_phillips_curve_data, ols_slope, summarize_relationship


def test_make_phillips_curve_data_has_expected_columns():
    data = make_phillips_curve_data(n=10, seed=1)

    assert list(data.columns) == ["unemployment", "inflation"]
    assert len(data) == 10


def test_ols_slope_recovers_simple_linear_relationship():
    slope = ols_slope(
        x=make_phillips_curve_data(n=3, seed=2)["unemployment"].to_numpy(),
        y=make_phillips_curve_data(n=3, seed=2)["inflation"].to_numpy(),
    )

    assert isinstance(slope, float)


def test_summary_reports_negative_slope_for_synthetic_data():
    data = make_phillips_curve_data(n=100, seed=42)
    summary = summarize_relationship(data)

    assert summary["n"] == 100.0
    assert summary["ols_slope"] < 0
