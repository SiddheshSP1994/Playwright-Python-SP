import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-8031", "title": "Analytics scenario 8031", "data": {"sku": "SKU8031", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8031@example.com", "threshold": 310}},
    {"id": "ANALYTICS-8032", "title": "Analytics scenario 8032", "data": {"sku": "SKU8032", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8032@example.com", "threshold": 320}},
    {"id": "ANALYTICS-8033", "title": "Analytics scenario 8033", "data": {"sku": "SKU8033", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8033@example.com", "threshold": 330}},
    {"id": "ANALYTICS-8034", "title": "Analytics scenario 8034", "data": {"sku": "SKU8034", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8034@example.com", "threshold": 340}},
    {"id": "ANALYTICS-8035", "title": "Analytics scenario 8035", "data": {"sku": "SKU8035", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8035@example.com", "threshold": 350}},
    {"id": "ANALYTICS-8036", "title": "Analytics scenario 8036", "data": {"sku": "SKU8036", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8036@example.com", "threshold": 360}},
    {"id": "ANALYTICS-8037", "title": "Analytics scenario 8037", "data": {"sku": "SKU8037", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8037@example.com", "threshold": 370}},
    {"id": "ANALYTICS-8038", "title": "Analytics scenario 8038", "data": {"sku": "SKU8038", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8038@example.com", "threshold": 380}},
    {"id": "ANALYTICS-8039", "title": "Analytics scenario 8039", "data": {"sku": "SKU8039", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8039@example.com", "threshold": 390}},
    {"id": "ANALYTICS-8040", "title": "Analytics scenario 8040", "data": {"sku": "SKU8040", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8040@example.com", "threshold": 400}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
