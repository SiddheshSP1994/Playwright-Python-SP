import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-6221", "title": "Email scenario 6221", "data": {"sku": "SKU6221", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6221@example.com", "threshold": 210}},
    {"id": "EMAIL-6222", "title": "Email scenario 6222", "data": {"sku": "SKU6222", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6222@example.com", "threshold": 220}},
    {"id": "EMAIL-6223", "title": "Email scenario 6223", "data": {"sku": "SKU6223", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6223@example.com", "threshold": 230}},
    {"id": "EMAIL-6224", "title": "Email scenario 6224", "data": {"sku": "SKU6224", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6224@example.com", "threshold": 240}},
    {"id": "EMAIL-6225", "title": "Email scenario 6225", "data": {"sku": "SKU6225", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6225@example.com", "threshold": 250}},
    {"id": "EMAIL-6226", "title": "Email scenario 6226", "data": {"sku": "SKU6226", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6226@example.com", "threshold": 260}},
    {"id": "EMAIL-6227", "title": "Email scenario 6227", "data": {"sku": "SKU6227", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6227@example.com", "threshold": 270}},
    {"id": "EMAIL-6228", "title": "Email scenario 6228", "data": {"sku": "SKU6228", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6228@example.com", "threshold": 280}},
    {"id": "EMAIL-6229", "title": "Email scenario 6229", "data": {"sku": "SKU6229", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6229@example.com", "threshold": 290}},
    {"id": "EMAIL-6230", "title": "Email scenario 6230", "data": {"sku": "SKU6230", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6230@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
