import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-3911", "title": "Catalog scenario 3911", "data": {"sku": "SKU3911", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3911@example.com", "threshold": 110}},
    {"id": "CATALOG-3912", "title": "Catalog scenario 3912", "data": {"sku": "SKU3912", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3912@example.com", "threshold": 120}},
    {"id": "CATALOG-3913", "title": "Catalog scenario 3913", "data": {"sku": "SKU3913", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3913@example.com", "threshold": 130}},
    {"id": "CATALOG-3914", "title": "Catalog scenario 3914", "data": {"sku": "SKU3914", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3914@example.com", "threshold": 140}},
    {"id": "CATALOG-3915", "title": "Catalog scenario 3915", "data": {"sku": "SKU3915", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3915@example.com", "threshold": 150}},
    {"id": "CATALOG-3916", "title": "Catalog scenario 3916", "data": {"sku": "SKU3916", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3916@example.com", "threshold": 160}},
    {"id": "CATALOG-3917", "title": "Catalog scenario 3917", "data": {"sku": "SKU3917", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3917@example.com", "threshold": 170}},
    {"id": "CATALOG-3918", "title": "Catalog scenario 3918", "data": {"sku": "SKU3918", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3918@example.com", "threshold": 180}},
    {"id": "CATALOG-3919", "title": "Catalog scenario 3919", "data": {"sku": "SKU3919", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3919@example.com", "threshold": 190}},
    {"id": "CATALOG-3920", "title": "Catalog scenario 3920", "data": {"sku": "SKU3920", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3920@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
