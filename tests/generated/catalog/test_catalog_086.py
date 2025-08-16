import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-5111", "title": "Catalog scenario 5111", "data": {"sku": "SKU5111", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5111@example.com", "threshold": 110}},
    {"id": "CATALOG-5112", "title": "Catalog scenario 5112", "data": {"sku": "SKU5112", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5112@example.com", "threshold": 120}},
    {"id": "CATALOG-5113", "title": "Catalog scenario 5113", "data": {"sku": "SKU5113", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5113@example.com", "threshold": 130}},
    {"id": "CATALOG-5114", "title": "Catalog scenario 5114", "data": {"sku": "SKU5114", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5114@example.com", "threshold": 140}},
    {"id": "CATALOG-5115", "title": "Catalog scenario 5115", "data": {"sku": "SKU5115", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5115@example.com", "threshold": 150}},
    {"id": "CATALOG-5116", "title": "Catalog scenario 5116", "data": {"sku": "SKU5116", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5116@example.com", "threshold": 160}},
    {"id": "CATALOG-5117", "title": "Catalog scenario 5117", "data": {"sku": "SKU5117", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5117@example.com", "threshold": 170}},
    {"id": "CATALOG-5118", "title": "Catalog scenario 5118", "data": {"sku": "SKU5118", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5118@example.com", "threshold": 180}},
    {"id": "CATALOG-5119", "title": "Catalog scenario 5119", "data": {"sku": "SKU5119", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5119@example.com", "threshold": 190}},
    {"id": "CATALOG-5120", "title": "Catalog scenario 5120", "data": {"sku": "SKU5120", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5120@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
