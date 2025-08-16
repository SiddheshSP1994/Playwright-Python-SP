import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-7011", "title": "Analytics scenario 7011", "data": {"sku": "SKU7011", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7011@example.com", "threshold": 110}},
    {"id": "ANALYTICS-7012", "title": "Analytics scenario 7012", "data": {"sku": "SKU7012", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7012@example.com", "threshold": 120}},
    {"id": "ANALYTICS-7013", "title": "Analytics scenario 7013", "data": {"sku": "SKU7013", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7013@example.com", "threshold": 130}},
    {"id": "ANALYTICS-7014", "title": "Analytics scenario 7014", "data": {"sku": "SKU7014", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7014@example.com", "threshold": 140}},
    {"id": "ANALYTICS-7015", "title": "Analytics scenario 7015", "data": {"sku": "SKU7015", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7015@example.com", "threshold": 150}},
    {"id": "ANALYTICS-7016", "title": "Analytics scenario 7016", "data": {"sku": "SKU7016", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7016@example.com", "threshold": 160}},
    {"id": "ANALYTICS-7017", "title": "Analytics scenario 7017", "data": {"sku": "SKU7017", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7017@example.com", "threshold": 170}},
    {"id": "ANALYTICS-7018", "title": "Analytics scenario 7018", "data": {"sku": "SKU7018", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7018@example.com", "threshold": 180}},
    {"id": "ANALYTICS-7019", "title": "Analytics scenario 7019", "data": {"sku": "SKU7019", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7019@example.com", "threshold": 190}},
    {"id": "ANALYTICS-7020", "title": "Analytics scenario 7020", "data": {"sku": "SKU7020", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7020@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
