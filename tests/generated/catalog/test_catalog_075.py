import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-4451", "title": "Catalog scenario 4451", "data": {"sku": "SKU4451", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4451@example.com", "threshold": 510}},
    {"id": "CATALOG-4452", "title": "Catalog scenario 4452", "data": {"sku": "SKU4452", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4452@example.com", "threshold": 520}},
    {"id": "CATALOG-4453", "title": "Catalog scenario 4453", "data": {"sku": "SKU4453", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4453@example.com", "threshold": 530}},
    {"id": "CATALOG-4454", "title": "Catalog scenario 4454", "data": {"sku": "SKU4454", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4454@example.com", "threshold": 540}},
    {"id": "CATALOG-4455", "title": "Catalog scenario 4455", "data": {"sku": "SKU4455", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4455@example.com", "threshold": 550}},
    {"id": "CATALOG-4456", "title": "Catalog scenario 4456", "data": {"sku": "SKU4456", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4456@example.com", "threshold": 560}},
    {"id": "CATALOG-4457", "title": "Catalog scenario 4457", "data": {"sku": "SKU4457", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4457@example.com", "threshold": 570}},
    {"id": "CATALOG-4458", "title": "Catalog scenario 4458", "data": {"sku": "SKU4458", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4458@example.com", "threshold": 580}},
    {"id": "CATALOG-4459", "title": "Catalog scenario 4459", "data": {"sku": "SKU4459", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4459@example.com", "threshold": 590}},
    {"id": "CATALOG-4460", "title": "Catalog scenario 4460", "data": {"sku": "SKU4460", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4460@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
