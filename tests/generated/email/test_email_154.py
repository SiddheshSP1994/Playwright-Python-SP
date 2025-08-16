import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-9221", "title": "Email scenario 9221", "data": {"sku": "SKU9221", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9221@example.com", "threshold": 210}},
    {"id": "EMAIL-9222", "title": "Email scenario 9222", "data": {"sku": "SKU9222", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9222@example.com", "threshold": 220}},
    {"id": "EMAIL-9223", "title": "Email scenario 9223", "data": {"sku": "SKU9223", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9223@example.com", "threshold": 230}},
    {"id": "EMAIL-9224", "title": "Email scenario 9224", "data": {"sku": "SKU9224", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9224@example.com", "threshold": 240}},
    {"id": "EMAIL-9225", "title": "Email scenario 9225", "data": {"sku": "SKU9225", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9225@example.com", "threshold": 250}},
    {"id": "EMAIL-9226", "title": "Email scenario 9226", "data": {"sku": "SKU9226", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9226@example.com", "threshold": 260}},
    {"id": "EMAIL-9227", "title": "Email scenario 9227", "data": {"sku": "SKU9227", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9227@example.com", "threshold": 270}},
    {"id": "EMAIL-9228", "title": "Email scenario 9228", "data": {"sku": "SKU9228", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9228@example.com", "threshold": 280}},
    {"id": "EMAIL-9229", "title": "Email scenario 9229", "data": {"sku": "SKU9229", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9229@example.com", "threshold": 290}},
    {"id": "EMAIL-9230", "title": "Email scenario 9230", "data": {"sku": "SKU9230", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9230@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
