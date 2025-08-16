import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-9761", "title": "Email scenario 9761", "data": {"sku": "SKU9761", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9761@example.com", "threshold": 610}},
    {"id": "EMAIL-9762", "title": "Email scenario 9762", "data": {"sku": "SKU9762", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9762@example.com", "threshold": 620}},
    {"id": "EMAIL-9763", "title": "Email scenario 9763", "data": {"sku": "SKU9763", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9763@example.com", "threshold": 630}},
    {"id": "EMAIL-9764", "title": "Email scenario 9764", "data": {"sku": "SKU9764", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9764@example.com", "threshold": 640}},
    {"id": "EMAIL-9765", "title": "Email scenario 9765", "data": {"sku": "SKU9765", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9765@example.com", "threshold": 650}},
    {"id": "EMAIL-9766", "title": "Email scenario 9766", "data": {"sku": "SKU9766", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9766@example.com", "threshold": 660}},
    {"id": "EMAIL-9767", "title": "Email scenario 9767", "data": {"sku": "SKU9767", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9767@example.com", "threshold": 670}},
    {"id": "EMAIL-9768", "title": "Email scenario 9768", "data": {"sku": "SKU9768", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9768@example.com", "threshold": 680}},
    {"id": "EMAIL-9769", "title": "Email scenario 9769", "data": {"sku": "SKU9769", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9769@example.com", "threshold": 690}},
    {"id": "EMAIL-9770", "title": "Email scenario 9770", "data": {"sku": "SKU9770", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9770@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
