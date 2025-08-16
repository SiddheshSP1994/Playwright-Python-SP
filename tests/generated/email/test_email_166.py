import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-9941", "title": "Email scenario 9941", "data": {"sku": "SKU9941", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9941@example.com", "threshold": 410}},
    {"id": "EMAIL-9942", "title": "Email scenario 9942", "data": {"sku": "SKU9942", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9942@example.com", "threshold": 420}},
    {"id": "EMAIL-9943", "title": "Email scenario 9943", "data": {"sku": "SKU9943", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9943@example.com", "threshold": 430}},
    {"id": "EMAIL-9944", "title": "Email scenario 9944", "data": {"sku": "SKU9944", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9944@example.com", "threshold": 440}},
    {"id": "EMAIL-9945", "title": "Email scenario 9945", "data": {"sku": "SKU9945", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9945@example.com", "threshold": 450}},
    {"id": "EMAIL-9946", "title": "Email scenario 9946", "data": {"sku": "SKU9946", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9946@example.com", "threshold": 460}},
    {"id": "EMAIL-9947", "title": "Email scenario 9947", "data": {"sku": "SKU9947", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9947@example.com", "threshold": 470}},
    {"id": "EMAIL-9948", "title": "Email scenario 9948", "data": {"sku": "SKU9948", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9948@example.com", "threshold": 480}},
    {"id": "EMAIL-9949", "title": "Email scenario 9949", "data": {"sku": "SKU9949", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9949@example.com", "threshold": 490}},
    {"id": "EMAIL-9950", "title": "Email scenario 9950", "data": {"sku": "SKU9950", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9950@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
