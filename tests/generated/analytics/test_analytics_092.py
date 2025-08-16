import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-5511", "title": "Analytics scenario 5511", "data": {"sku": "SKU5511", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5511@example.com", "threshold": 110}},
    {"id": "ANALYTICS-5512", "title": "Analytics scenario 5512", "data": {"sku": "SKU5512", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5512@example.com", "threshold": 120}},
    {"id": "ANALYTICS-5513", "title": "Analytics scenario 5513", "data": {"sku": "SKU5513", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5513@example.com", "threshold": 130}},
    {"id": "ANALYTICS-5514", "title": "Analytics scenario 5514", "data": {"sku": "SKU5514", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5514@example.com", "threshold": 140}},
    {"id": "ANALYTICS-5515", "title": "Analytics scenario 5515", "data": {"sku": "SKU5515", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5515@example.com", "threshold": 150}},
    {"id": "ANALYTICS-5516", "title": "Analytics scenario 5516", "data": {"sku": "SKU5516", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5516@example.com", "threshold": 160}},
    {"id": "ANALYTICS-5517", "title": "Analytics scenario 5517", "data": {"sku": "SKU5517", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5517@example.com", "threshold": 170}},
    {"id": "ANALYTICS-5518", "title": "Analytics scenario 5518", "data": {"sku": "SKU5518", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5518@example.com", "threshold": 180}},
    {"id": "ANALYTICS-5519", "title": "Analytics scenario 5519", "data": {"sku": "SKU5519", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5519@example.com", "threshold": 190}},
    {"id": "ANALYTICS-5520", "title": "Analytics scenario 5520", "data": {"sku": "SKU5520", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5520@example.com", "threshold": 200}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
