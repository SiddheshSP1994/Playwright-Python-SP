import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-3161", "title": "Email scenario 3161", "data": {"sku": "SKU3161", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3161@example.com", "threshold": 610}},
    {"id": "EMAIL-3162", "title": "Email scenario 3162", "data": {"sku": "SKU3162", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3162@example.com", "threshold": 620}},
    {"id": "EMAIL-3163", "title": "Email scenario 3163", "data": {"sku": "SKU3163", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3163@example.com", "threshold": 630}},
    {"id": "EMAIL-3164", "title": "Email scenario 3164", "data": {"sku": "SKU3164", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3164@example.com", "threshold": 640}},
    {"id": "EMAIL-3165", "title": "Email scenario 3165", "data": {"sku": "SKU3165", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3165@example.com", "threshold": 650}},
    {"id": "EMAIL-3166", "title": "Email scenario 3166", "data": {"sku": "SKU3166", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3166@example.com", "threshold": 660}},
    {"id": "EMAIL-3167", "title": "Email scenario 3167", "data": {"sku": "SKU3167", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3167@example.com", "threshold": 670}},
    {"id": "EMAIL-3168", "title": "Email scenario 3168", "data": {"sku": "SKU3168", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3168@example.com", "threshold": 680}},
    {"id": "EMAIL-3169", "title": "Email scenario 3169", "data": {"sku": "SKU3169", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3169@example.com", "threshold": 690}},
    {"id": "EMAIL-3170", "title": "Email scenario 3170", "data": {"sku": "SKU3170", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3170@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
