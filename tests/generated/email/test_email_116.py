import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-6941", "title": "Email scenario 6941", "data": {"sku": "SKU6941", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6941@example.com", "threshold": 410}},
    {"id": "EMAIL-6942", "title": "Email scenario 6942", "data": {"sku": "SKU6942", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6942@example.com", "threshold": 420}},
    {"id": "EMAIL-6943", "title": "Email scenario 6943", "data": {"sku": "SKU6943", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6943@example.com", "threshold": 430}},
    {"id": "EMAIL-6944", "title": "Email scenario 6944", "data": {"sku": "SKU6944", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6944@example.com", "threshold": 440}},
    {"id": "EMAIL-6945", "title": "Email scenario 6945", "data": {"sku": "SKU6945", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6945@example.com", "threshold": 450}},
    {"id": "EMAIL-6946", "title": "Email scenario 6946", "data": {"sku": "SKU6946", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6946@example.com", "threshold": 460}},
    {"id": "EMAIL-6947", "title": "Email scenario 6947", "data": {"sku": "SKU6947", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6947@example.com", "threshold": 470}},
    {"id": "EMAIL-6948", "title": "Email scenario 6948", "data": {"sku": "SKU6948", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6948@example.com", "threshold": 480}},
    {"id": "EMAIL-6949", "title": "Email scenario 6949", "data": {"sku": "SKU6949", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6949@example.com", "threshold": 490}},
    {"id": "EMAIL-6950", "title": "Email scenario 6950", "data": {"sku": "SKU6950", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6950@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
