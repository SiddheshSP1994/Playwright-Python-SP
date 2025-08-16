import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-0341", "title": "Email scenario 341", "data": {"sku": "SKU341", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user341@example.com", "threshold": 410}},
    {"id": "EMAIL-0342", "title": "Email scenario 342", "data": {"sku": "SKU342", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user342@example.com", "threshold": 420}},
    {"id": "EMAIL-0343", "title": "Email scenario 343", "data": {"sku": "SKU343", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user343@example.com", "threshold": 430}},
    {"id": "EMAIL-0344", "title": "Email scenario 344", "data": {"sku": "SKU344", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user344@example.com", "threshold": 440}},
    {"id": "EMAIL-0345", "title": "Email scenario 345", "data": {"sku": "SKU345", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user345@example.com", "threshold": 450}},
    {"id": "EMAIL-0346", "title": "Email scenario 346", "data": {"sku": "SKU346", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user346@example.com", "threshold": 460}},
    {"id": "EMAIL-0347", "title": "Email scenario 347", "data": {"sku": "SKU347", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user347@example.com", "threshold": 470}},
    {"id": "EMAIL-0348", "title": "Email scenario 348", "data": {"sku": "SKU348", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user348@example.com", "threshold": 480}},
    {"id": "EMAIL-0349", "title": "Email scenario 349", "data": {"sku": "SKU349", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user349@example.com", "threshold": 490}},
    {"id": "EMAIL-0350", "title": "Email scenario 350", "data": {"sku": "SKU350", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user350@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
