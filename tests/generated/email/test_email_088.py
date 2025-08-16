import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-5261", "title": "Email scenario 5261", "data": {"sku": "SKU5261", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5261@example.com", "threshold": 610}},
    {"id": "EMAIL-5262", "title": "Email scenario 5262", "data": {"sku": "SKU5262", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5262@example.com", "threshold": 620}},
    {"id": "EMAIL-5263", "title": "Email scenario 5263", "data": {"sku": "SKU5263", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5263@example.com", "threshold": 630}},
    {"id": "EMAIL-5264", "title": "Email scenario 5264", "data": {"sku": "SKU5264", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5264@example.com", "threshold": 640}},
    {"id": "EMAIL-5265", "title": "Email scenario 5265", "data": {"sku": "SKU5265", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5265@example.com", "threshold": 650}},
    {"id": "EMAIL-5266", "title": "Email scenario 5266", "data": {"sku": "SKU5266", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5266@example.com", "threshold": 660}},
    {"id": "EMAIL-5267", "title": "Email scenario 5267", "data": {"sku": "SKU5267", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5267@example.com", "threshold": 670}},
    {"id": "EMAIL-5268", "title": "Email scenario 5268", "data": {"sku": "SKU5268", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5268@example.com", "threshold": 680}},
    {"id": "EMAIL-5269", "title": "Email scenario 5269", "data": {"sku": "SKU5269", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5269@example.com", "threshold": 690}},
    {"id": "EMAIL-5270", "title": "Email scenario 5270", "data": {"sku": "SKU5270", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5270@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
