import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-8261", "title": "Email scenario 8261", "data": {"sku": "SKU8261", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8261@example.com", "threshold": 610}},
    {"id": "EMAIL-8262", "title": "Email scenario 8262", "data": {"sku": "SKU8262", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8262@example.com", "threshold": 620}},
    {"id": "EMAIL-8263", "title": "Email scenario 8263", "data": {"sku": "SKU8263", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8263@example.com", "threshold": 630}},
    {"id": "EMAIL-8264", "title": "Email scenario 8264", "data": {"sku": "SKU8264", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8264@example.com", "threshold": 640}},
    {"id": "EMAIL-8265", "title": "Email scenario 8265", "data": {"sku": "SKU8265", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8265@example.com", "threshold": 650}},
    {"id": "EMAIL-8266", "title": "Email scenario 8266", "data": {"sku": "SKU8266", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8266@example.com", "threshold": 660}},
    {"id": "EMAIL-8267", "title": "Email scenario 8267", "data": {"sku": "SKU8267", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8267@example.com", "threshold": 670}},
    {"id": "EMAIL-8268", "title": "Email scenario 8268", "data": {"sku": "SKU8268", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8268@example.com", "threshold": 680}},
    {"id": "EMAIL-8269", "title": "Email scenario 8269", "data": {"sku": "SKU8269", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8269@example.com", "threshold": 690}},
    {"id": "EMAIL-8270", "title": "Email scenario 8270", "data": {"sku": "SKU8270", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8270@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
