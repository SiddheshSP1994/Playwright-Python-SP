import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-1991", "title": "Catalog scenario 1991", "data": {"sku": "SKU1991", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1991@example.com", "threshold": 910}},
    {"id": "CATALOG-1992", "title": "Catalog scenario 1992", "data": {"sku": "SKU1992", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1992@example.com", "threshold": 920}},
    {"id": "CATALOG-1993", "title": "Catalog scenario 1993", "data": {"sku": "SKU1993", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1993@example.com", "threshold": 930}},
    {"id": "CATALOG-1994", "title": "Catalog scenario 1994", "data": {"sku": "SKU1994", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1994@example.com", "threshold": 940}},
    {"id": "CATALOG-1995", "title": "Catalog scenario 1995", "data": {"sku": "SKU1995", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1995@example.com", "threshold": 950}},
    {"id": "CATALOG-1996", "title": "Catalog scenario 1996", "data": {"sku": "SKU1996", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1996@example.com", "threshold": 960}},
    {"id": "CATALOG-1997", "title": "Catalog scenario 1997", "data": {"sku": "SKU1997", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1997@example.com", "threshold": 970}},
    {"id": "CATALOG-1998", "title": "Catalog scenario 1998", "data": {"sku": "SKU1998", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1998@example.com", "threshold": 980}},
    {"id": "CATALOG-1999", "title": "Catalog scenario 1999", "data": {"sku": "SKU1999", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1999@example.com", "threshold": 990}},
    {"id": "CATALOG-2000", "title": "Catalog scenario 2000", "data": {"sku": "SKU2000", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2000@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
