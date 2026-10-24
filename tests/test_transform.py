from project_name.transform import snake_case


def test_snake_case_basic():
    assert snake_case("Trip Distance (mi)") == "trip_distance_mi"


def test_snake_case_strips_edges():
    assert snake_case("  Fare $ ") == "fare"