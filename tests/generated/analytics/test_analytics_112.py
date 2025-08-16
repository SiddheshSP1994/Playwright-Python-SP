import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-6711", "title": "Analytics scenario 6711", "data": {"sku": "SKU6711", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6711@example.com", "threshold": 110}},
    {"id": "ANALYTICS-6712", "title": "Analytics scenario 6712", "data": {"sku": "SKU6712", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6712@example.com", "threshold": 120}},
    {"id": "ANALYTICS-6713", "title": "Analytics scenario 6713", "data": {"sku": "SKU6713", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6713@example.com", "threshold": 130}},
    {"id": "ANALYTICS-6714", "title": "Analytics scenario 6714", "data": {"sku": "SKU6714", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6714@example.com", "threshold": 140}},
    {"id": "ANALYTICS-6715", "title": "Analytics scenario 6715", "data": {"sku": "SKU6715", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6715@example.com", "threshold": 150}},
    {"id": "ANALYTICS-6716", "title": "Analytics scenario 6716", "data": {"sku": "SKU6716", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6716@example.com", "threshold": 160}},
    {"id": "ANALYTICS-6717", "title": "Analytics scenario 6717", "data": {"sku": "SKU6717", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6717@example.com", "threshold": 170}},
    {"id": "ANALYTICS-6718", "title": "Analytics scenario 6718", "data": {"sku": "SKU6718", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6718@example.com", "threshold": 180}},
    {"id": "ANALYTICS-6719", "title": "Analytics scenario 6719", "data": {"sku": "SKU6719", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6719@example.com", "threshold": 190}},
    {"id": "ANALYTICS-6720", "title": "Analytics scenario 6720", "data": {"sku": "SKU6720", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6720@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
