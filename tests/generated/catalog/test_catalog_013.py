import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-0731", "title": "Catalog scenario 731", "data": {"sku": "SKU731", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user731@example.com", "threshold": 310}},
    {"id": "CATALOG-0732", "title": "Catalog scenario 732", "data": {"sku": "SKU732", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user732@example.com", "threshold": 320}},
    {"id": "CATALOG-0733", "title": "Catalog scenario 733", "data": {"sku": "SKU733", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user733@example.com", "threshold": 330}},
    {"id": "CATALOG-0734", "title": "Catalog scenario 734", "data": {"sku": "SKU734", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user734@example.com", "threshold": 340}},
    {"id": "CATALOG-0735", "title": "Catalog scenario 735", "data": {"sku": "SKU735", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user735@example.com", "threshold": 350}},
    {"id": "CATALOG-0736", "title": "Catalog scenario 736", "data": {"sku": "SKU736", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user736@example.com", "threshold": 360}},
    {"id": "CATALOG-0737", "title": "Catalog scenario 737", "data": {"sku": "SKU737", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user737@example.com", "threshold": 370}},
    {"id": "CATALOG-0738", "title": "Catalog scenario 738", "data": {"sku": "SKU738", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user738@example.com", "threshold": 380}},
    {"id": "CATALOG-0739", "title": "Catalog scenario 739", "data": {"sku": "SKU739", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user739@example.com", "threshold": 390}},
    {"id": "CATALOG-0740", "title": "Catalog scenario 740", "data": {"sku": "SKU740", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user740@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
