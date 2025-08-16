import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-7451", "title": "Catalog scenario 7451", "data": {"sku": "SKU7451", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7451@example.com", "threshold": 510}},
    {"id": "CATALOG-7452", "title": "Catalog scenario 7452", "data": {"sku": "SKU7452", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7452@example.com", "threshold": 520}},
    {"id": "CATALOG-7453", "title": "Catalog scenario 7453", "data": {"sku": "SKU7453", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7453@example.com", "threshold": 530}},
    {"id": "CATALOG-7454", "title": "Catalog scenario 7454", "data": {"sku": "SKU7454", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7454@example.com", "threshold": 540}},
    {"id": "CATALOG-7455", "title": "Catalog scenario 7455", "data": {"sku": "SKU7455", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7455@example.com", "threshold": 550}},
    {"id": "CATALOG-7456", "title": "Catalog scenario 7456", "data": {"sku": "SKU7456", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7456@example.com", "threshold": 560}},
    {"id": "CATALOG-7457", "title": "Catalog scenario 7457", "data": {"sku": "SKU7457", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7457@example.com", "threshold": 570}},
    {"id": "CATALOG-7458", "title": "Catalog scenario 7458", "data": {"sku": "SKU7458", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7458@example.com", "threshold": 580}},
    {"id": "CATALOG-7459", "title": "Catalog scenario 7459", "data": {"sku": "SKU7459", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7459@example.com", "threshold": 590}},
    {"id": "CATALOG-7460", "title": "Catalog scenario 7460", "data": {"sku": "SKU7460", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7460@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
