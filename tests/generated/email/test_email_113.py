import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-6761", "title": "Email scenario 6761", "data": {"sku": "SKU6761", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6761@example.com", "threshold": 610}},
    {"id": "EMAIL-6762", "title": "Email scenario 6762", "data": {"sku": "SKU6762", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6762@example.com", "threshold": 620}},
    {"id": "EMAIL-6763", "title": "Email scenario 6763", "data": {"sku": "SKU6763", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6763@example.com", "threshold": 630}},
    {"id": "EMAIL-6764", "title": "Email scenario 6764", "data": {"sku": "SKU6764", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6764@example.com", "threshold": 640}},
    {"id": "EMAIL-6765", "title": "Email scenario 6765", "data": {"sku": "SKU6765", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6765@example.com", "threshold": 650}},
    {"id": "EMAIL-6766", "title": "Email scenario 6766", "data": {"sku": "SKU6766", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6766@example.com", "threshold": 660}},
    {"id": "EMAIL-6767", "title": "Email scenario 6767", "data": {"sku": "SKU6767", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6767@example.com", "threshold": 670}},
    {"id": "EMAIL-6768", "title": "Email scenario 6768", "data": {"sku": "SKU6768", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6768@example.com", "threshold": 680}},
    {"id": "EMAIL-6769", "title": "Email scenario 6769", "data": {"sku": "SKU6769", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6769@example.com", "threshold": 690}},
    {"id": "EMAIL-6770", "title": "Email scenario 6770", "data": {"sku": "SKU6770", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6770@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
