import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-7121", "title": "Email scenario 7121", "data": {"sku": "SKU7121", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7121@example.com", "threshold": 210}},
    {"id": "EMAIL-7122", "title": "Email scenario 7122", "data": {"sku": "SKU7122", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7122@example.com", "threshold": 220}},
    {"id": "EMAIL-7123", "title": "Email scenario 7123", "data": {"sku": "SKU7123", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7123@example.com", "threshold": 230}},
    {"id": "EMAIL-7124", "title": "Email scenario 7124", "data": {"sku": "SKU7124", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7124@example.com", "threshold": 240}},
    {"id": "EMAIL-7125", "title": "Email scenario 7125", "data": {"sku": "SKU7125", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7125@example.com", "threshold": 250}},
    {"id": "EMAIL-7126", "title": "Email scenario 7126", "data": {"sku": "SKU7126", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7126@example.com", "threshold": 260}},
    {"id": "EMAIL-7127", "title": "Email scenario 7127", "data": {"sku": "SKU7127", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7127@example.com", "threshold": 270}},
    {"id": "EMAIL-7128", "title": "Email scenario 7128", "data": {"sku": "SKU7128", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7128@example.com", "threshold": 280}},
    {"id": "EMAIL-7129", "title": "Email scenario 7129", "data": {"sku": "SKU7129", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7129@example.com", "threshold": 290}},
    {"id": "EMAIL-7130", "title": "Email scenario 7130", "data": {"sku": "SKU7130", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7130@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
