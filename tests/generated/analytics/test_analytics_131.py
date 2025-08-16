import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-7851", "title": "Analytics scenario 7851", "data": {"sku": "SKU7851", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7851@example.com", "threshold": 510}},
    {"id": "ANALYTICS-7852", "title": "Analytics scenario 7852", "data": {"sku": "SKU7852", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7852@example.com", "threshold": 520}},
    {"id": "ANALYTICS-7853", "title": "Analytics scenario 7853", "data": {"sku": "SKU7853", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7853@example.com", "threshold": 530}},
    {"id": "ANALYTICS-7854", "title": "Analytics scenario 7854", "data": {"sku": "SKU7854", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7854@example.com", "threshold": 540}},
    {"id": "ANALYTICS-7855", "title": "Analytics scenario 7855", "data": {"sku": "SKU7855", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7855@example.com", "threshold": 550}},
    {"id": "ANALYTICS-7856", "title": "Analytics scenario 7856", "data": {"sku": "SKU7856", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7856@example.com", "threshold": 560}},
    {"id": "ANALYTICS-7857", "title": "Analytics scenario 7857", "data": {"sku": "SKU7857", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7857@example.com", "threshold": 570}},
    {"id": "ANALYTICS-7858", "title": "Analytics scenario 7858", "data": {"sku": "SKU7858", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7858@example.com", "threshold": 580}},
    {"id": "ANALYTICS-7859", "title": "Analytics scenario 7859", "data": {"sku": "SKU7859", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7859@example.com", "threshold": 590}},
    {"id": "ANALYTICS-7860", "title": "Analytics scenario 7860", "data": {"sku": "SKU7860", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7860@example.com", "threshold": 600}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
