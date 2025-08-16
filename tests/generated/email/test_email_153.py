import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-9161", "title": "Email scenario 9161", "data": {"sku": "SKU9161", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9161@example.com", "threshold": 610}},
    {"id": "EMAIL-9162", "title": "Email scenario 9162", "data": {"sku": "SKU9162", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9162@example.com", "threshold": 620}},
    {"id": "EMAIL-9163", "title": "Email scenario 9163", "data": {"sku": "SKU9163", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9163@example.com", "threshold": 630}},
    {"id": "EMAIL-9164", "title": "Email scenario 9164", "data": {"sku": "SKU9164", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9164@example.com", "threshold": 640}},
    {"id": "EMAIL-9165", "title": "Email scenario 9165", "data": {"sku": "SKU9165", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9165@example.com", "threshold": 650}},
    {"id": "EMAIL-9166", "title": "Email scenario 9166", "data": {"sku": "SKU9166", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9166@example.com", "threshold": 660}},
    {"id": "EMAIL-9167", "title": "Email scenario 9167", "data": {"sku": "SKU9167", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9167@example.com", "threshold": 670}},
    {"id": "EMAIL-9168", "title": "Email scenario 9168", "data": {"sku": "SKU9168", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9168@example.com", "threshold": 680}},
    {"id": "EMAIL-9169", "title": "Email scenario 9169", "data": {"sku": "SKU9169", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9169@example.com", "threshold": 690}},
    {"id": "EMAIL-9170", "title": "Email scenario 9170", "data": {"sku": "SKU9170", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9170@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
