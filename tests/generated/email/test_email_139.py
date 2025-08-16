import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-8321", "title": "Email scenario 8321", "data": {"sku": "SKU8321", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8321@example.com", "threshold": 210}},
    {"id": "EMAIL-8322", "title": "Email scenario 8322", "data": {"sku": "SKU8322", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8322@example.com", "threshold": 220}},
    {"id": "EMAIL-8323", "title": "Email scenario 8323", "data": {"sku": "SKU8323", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8323@example.com", "threshold": 230}},
    {"id": "EMAIL-8324", "title": "Email scenario 8324", "data": {"sku": "SKU8324", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8324@example.com", "threshold": 240}},
    {"id": "EMAIL-8325", "title": "Email scenario 8325", "data": {"sku": "SKU8325", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8325@example.com", "threshold": 250}},
    {"id": "EMAIL-8326", "title": "Email scenario 8326", "data": {"sku": "SKU8326", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8326@example.com", "threshold": 260}},
    {"id": "EMAIL-8327", "title": "Email scenario 8327", "data": {"sku": "SKU8327", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8327@example.com", "threshold": 270}},
    {"id": "EMAIL-8328", "title": "Email scenario 8328", "data": {"sku": "SKU8328", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8328@example.com", "threshold": 280}},
    {"id": "EMAIL-8329", "title": "Email scenario 8329", "data": {"sku": "SKU8329", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8329@example.com", "threshold": 290}},
    {"id": "EMAIL-8330", "title": "Email scenario 8330", "data": {"sku": "SKU8330", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8330@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
