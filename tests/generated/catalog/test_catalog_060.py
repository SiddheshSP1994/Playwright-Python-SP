import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-3551", "title": "Catalog scenario 3551", "data": {"sku": "SKU3551", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3551@example.com", "threshold": 510}},
    {"id": "CATALOG-3552", "title": "Catalog scenario 3552", "data": {"sku": "SKU3552", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3552@example.com", "threshold": 520}},
    {"id": "CATALOG-3553", "title": "Catalog scenario 3553", "data": {"sku": "SKU3553", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3553@example.com", "threshold": 530}},
    {"id": "CATALOG-3554", "title": "Catalog scenario 3554", "data": {"sku": "SKU3554", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3554@example.com", "threshold": 540}},
    {"id": "CATALOG-3555", "title": "Catalog scenario 3555", "data": {"sku": "SKU3555", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3555@example.com", "threshold": 550}},
    {"id": "CATALOG-3556", "title": "Catalog scenario 3556", "data": {"sku": "SKU3556", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3556@example.com", "threshold": 560}},
    {"id": "CATALOG-3557", "title": "Catalog scenario 3557", "data": {"sku": "SKU3557", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3557@example.com", "threshold": 570}},
    {"id": "CATALOG-3558", "title": "Catalog scenario 3558", "data": {"sku": "SKU3558", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3558@example.com", "threshold": 580}},
    {"id": "CATALOG-3559", "title": "Catalog scenario 3559", "data": {"sku": "SKU3559", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3559@example.com", "threshold": 590}},
    {"id": "CATALOG-3560", "title": "Catalog scenario 3560", "data": {"sku": "SKU3560", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3560@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
