import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-3941", "title": "Email scenario 3941", "data": {"sku": "SKU3941", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3941@example.com", "threshold": 410}},
    {"id": "EMAIL-3942", "title": "Email scenario 3942", "data": {"sku": "SKU3942", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3942@example.com", "threshold": 420}},
    {"id": "EMAIL-3943", "title": "Email scenario 3943", "data": {"sku": "SKU3943", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3943@example.com", "threshold": 430}},
    {"id": "EMAIL-3944", "title": "Email scenario 3944", "data": {"sku": "SKU3944", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3944@example.com", "threshold": 440}},
    {"id": "EMAIL-3945", "title": "Email scenario 3945", "data": {"sku": "SKU3945", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3945@example.com", "threshold": 450}},
    {"id": "EMAIL-3946", "title": "Email scenario 3946", "data": {"sku": "SKU3946", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3946@example.com", "threshold": 460}},
    {"id": "EMAIL-3947", "title": "Email scenario 3947", "data": {"sku": "SKU3947", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3947@example.com", "threshold": 470}},
    {"id": "EMAIL-3948", "title": "Email scenario 3948", "data": {"sku": "SKU3948", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3948@example.com", "threshold": 480}},
    {"id": "EMAIL-3949", "title": "Email scenario 3949", "data": {"sku": "SKU3949", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3949@example.com", "threshold": 490}},
    {"id": "EMAIL-3950", "title": "Email scenario 3950", "data": {"sku": "SKU3950", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3950@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
