import pytest


@pytest.fixture
def clean_merged_data():
    return {"strikers": [{"name": "Mary", "club": "Manchester United"}, {"name": "Robin van Persie", "club": "Feyenoord"}, {"name": "Nicolas Pepe", "club": "Arsenal"}, {"name": "Gonzalo Higuain", "club": "Napoli"}, {"name": "Sunil Chettri", "club": "Bengaluru FC"}], "boweler": [{"name": "KK", "club": "RR"}]}


@pytest.fixture
def clean_data():
    return [{"strikers": [{"name": "Mary", "club": "Manchester United"}, {"name": "Robin van Persie", "club": "Feyenoord"}]}, {"strikers": [{"name": "Nicolas Pepe", "club": "Arsenal"}], "boweler": [{"name": "KK", "club": "RR"}]}, {"strikers": [{"name": "Gonzalo Higuain", "club": "Napoli"}, {"name": "Sunil Chettri", "club": "Bengaluru FC"}]}]


@pytest.fixture
def merged_data_with_hindi():
	return {"strikers": [{"name": "Mary", "club": "Manchester United"}, {"name": "Robin van Persie", "club": "Feyenoord"}, {"name": "Nicolas Pepe", "club": "Arsenal"}, {"name": "Gonzalo Higuain", "club": "Napoli"}, {"name": "Sunil Chettri", "club": "Bengaluru FC"}], "boweler": [{"name": "नवीन", "club": "RR"}]}


@pytest.fixture
def data_with_hindi():
	return [{"strikers": [{"name": "Mary", "club": "Manchester United"}, {"name": "Robin van Persie", "club": "Feyenoord"}]}, {"strikers": [{"name": "Nicolas Pepe", "club": "Arsenal"}], "boweler": [{"name": "नवीन", "club": "RR"}]}, {"strikers": [{"name": "Gonzalo Higuain", "club": "Napoli"}, {"name": "Sunil Chettri", "club": "Bengaluru FC"}]}]