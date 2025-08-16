import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-4851", "title": "Analytics scenario 4851", "data": {"sku": "SKU4851", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4851@example.com", "threshold": 510}},
    {"id": "ANALYTICS-4852", "title": "Analytics scenario 4852", "data": {"sku": "SKU4852", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4852@example.com", "threshold": 520}},
    {"id": "ANALYTICS-4853", "title": "Analytics scenario 4853", "data": {"sku": "SKU4853", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4853@example.com", "threshold": 530}},
    {"id": "ANALYTICS-4854", "title": "Analytics scenario 4854", "data": {"sku": "SKU4854", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4854@example.com", "threshold": 540}},
    {"id": "ANALYTICS-4855", "title": "Analytics scenario 4855", "data": {"sku": "SKU4855", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4855@example.com", "threshold": 550}},
    {"id": "ANALYTICS-4856", "title": "Analytics scenario 4856", "data": {"sku": "SKU4856", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4856@example.com", "threshold": 560}},
    {"id": "ANALYTICS-4857", "title": "Analytics scenario 4857", "data": {"sku": "SKU4857", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4857@example.com", "threshold": 570}},
    {"id": "ANALYTICS-4858", "title": "Analytics scenario 4858", "data": {"sku": "SKU4858", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4858@example.com", "threshold": 580}},
    {"id": "ANALYTICS-4859", "title": "Analytics scenario 4859", "data": {"sku": "SKU4859", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4859@example.com", "threshold": 590}},
    {"id": "ANALYTICS-4860", "title": "Analytics scenario 4860", "data": {"sku": "SKU4860", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4860@example.com", "threshold": 600}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
