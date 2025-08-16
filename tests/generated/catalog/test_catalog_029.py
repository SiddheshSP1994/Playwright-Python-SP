import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-1691", "title": "Catalog scenario 1691", "data": {"sku": "SKU1691", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1691@example.com", "threshold": 910}},
    {"id": "CATALOG-1692", "title": "Catalog scenario 1692", "data": {"sku": "SKU1692", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1692@example.com", "threshold": 920}},
    {"id": "CATALOG-1693", "title": "Catalog scenario 1693", "data": {"sku": "SKU1693", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1693@example.com", "threshold": 930}},
    {"id": "CATALOG-1694", "title": "Catalog scenario 1694", "data": {"sku": "SKU1694", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1694@example.com", "threshold": 940}},
    {"id": "CATALOG-1695", "title": "Catalog scenario 1695", "data": {"sku": "SKU1695", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1695@example.com", "threshold": 950}},
    {"id": "CATALOG-1696", "title": "Catalog scenario 1696", "data": {"sku": "SKU1696", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1696@example.com", "threshold": 960}},
    {"id": "CATALOG-1697", "title": "Catalog scenario 1697", "data": {"sku": "SKU1697", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1697@example.com", "threshold": 970}},
    {"id": "CATALOG-1698", "title": "Catalog scenario 1698", "data": {"sku": "SKU1698", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1698@example.com", "threshold": 980}},
    {"id": "CATALOG-1699", "title": "Catalog scenario 1699", "data": {"sku": "SKU1699", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1699@example.com", "threshold": 990}},
    {"id": "CATALOG-1700", "title": "Catalog scenario 1700", "data": {"sku": "SKU1700", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1700@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
