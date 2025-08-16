import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-0711", "title": "Analytics scenario 711", "data": {"sku": "SKU711", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user711@example.com", "threshold": 110}},
    {"id": "ANALYTICS-0712", "title": "Analytics scenario 712", "data": {"sku": "SKU712", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user712@example.com", "threshold": 120}},
    {"id": "ANALYTICS-0713", "title": "Analytics scenario 713", "data": {"sku": "SKU713", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user713@example.com", "threshold": 130}},
    {"id": "ANALYTICS-0714", "title": "Analytics scenario 714", "data": {"sku": "SKU714", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user714@example.com", "threshold": 140}},
    {"id": "ANALYTICS-0715", "title": "Analytics scenario 715", "data": {"sku": "SKU715", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user715@example.com", "threshold": 150}},
    {"id": "ANALYTICS-0716", "title": "Analytics scenario 716", "data": {"sku": "SKU716", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user716@example.com", "threshold": 160}},
    {"id": "ANALYTICS-0717", "title": "Analytics scenario 717", "data": {"sku": "SKU717", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user717@example.com", "threshold": 170}},
    {"id": "ANALYTICS-0718", "title": "Analytics scenario 718", "data": {"sku": "SKU718", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user718@example.com", "threshold": 180}},
    {"id": "ANALYTICS-0719", "title": "Analytics scenario 719", "data": {"sku": "SKU719", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user719@example.com", "threshold": 190}},
    {"id": "ANALYTICS-0720", "title": "Analytics scenario 720", "data": {"sku": "SKU720", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user720@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
