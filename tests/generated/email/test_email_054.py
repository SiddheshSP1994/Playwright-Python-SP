import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-3221", "title": "Email scenario 3221", "data": {"sku": "SKU3221", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3221@example.com", "threshold": 210}},
    {"id": "EMAIL-3222", "title": "Email scenario 3222", "data": {"sku": "SKU3222", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3222@example.com", "threshold": 220}},
    {"id": "EMAIL-3223", "title": "Email scenario 3223", "data": {"sku": "SKU3223", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3223@example.com", "threshold": 230}},
    {"id": "EMAIL-3224", "title": "Email scenario 3224", "data": {"sku": "SKU3224", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3224@example.com", "threshold": 240}},
    {"id": "EMAIL-3225", "title": "Email scenario 3225", "data": {"sku": "SKU3225", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3225@example.com", "threshold": 250}},
    {"id": "EMAIL-3226", "title": "Email scenario 3226", "data": {"sku": "SKU3226", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3226@example.com", "threshold": 260}},
    {"id": "EMAIL-3227", "title": "Email scenario 3227", "data": {"sku": "SKU3227", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3227@example.com", "threshold": 270}},
    {"id": "EMAIL-3228", "title": "Email scenario 3228", "data": {"sku": "SKU3228", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3228@example.com", "threshold": 280}},
    {"id": "EMAIL-3229", "title": "Email scenario 3229", "data": {"sku": "SKU3229", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3229@example.com", "threshold": 290}},
    {"id": "EMAIL-3230", "title": "Email scenario 3230", "data": {"sku": "SKU3230", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3230@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
