import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-0401", "title": "Email scenario 401", "data": {"sku": "SKU401", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user401@example.com", "threshold": 10}},
    {"id": "EMAIL-0402", "title": "Email scenario 402", "data": {"sku": "SKU402", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user402@example.com", "threshold": 20}},
    {"id": "EMAIL-0403", "title": "Email scenario 403", "data": {"sku": "SKU403", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user403@example.com", "threshold": 30}},
    {"id": "EMAIL-0404", "title": "Email scenario 404", "data": {"sku": "SKU404", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user404@example.com", "threshold": 40}},
    {"id": "EMAIL-0405", "title": "Email scenario 405", "data": {"sku": "SKU405", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user405@example.com", "threshold": 50}},
    {"id": "EMAIL-0406", "title": "Email scenario 406", "data": {"sku": "SKU406", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user406@example.com", "threshold": 60}},
    {"id": "EMAIL-0407", "title": "Email scenario 407", "data": {"sku": "SKU407", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user407@example.com", "threshold": 70}},
    {"id": "EMAIL-0408", "title": "Email scenario 408", "data": {"sku": "SKU408", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user408@example.com", "threshold": 80}},
    {"id": "EMAIL-0409", "title": "Email scenario 409", "data": {"sku": "SKU409", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user409@example.com", "threshold": 90}},
    {"id": "EMAIL-0410", "title": "Email scenario 410", "data": {"sku": "SKU410", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user410@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
