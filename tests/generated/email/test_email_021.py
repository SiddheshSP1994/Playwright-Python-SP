import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-1241", "title": "Email scenario 1241", "data": {"sku": "SKU1241", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1241@example.com", "threshold": 410}},
    {"id": "EMAIL-1242", "title": "Email scenario 1242", "data": {"sku": "SKU1242", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1242@example.com", "threshold": 420}},
    {"id": "EMAIL-1243", "title": "Email scenario 1243", "data": {"sku": "SKU1243", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1243@example.com", "threshold": 430}},
    {"id": "EMAIL-1244", "title": "Email scenario 1244", "data": {"sku": "SKU1244", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1244@example.com", "threshold": 440}},
    {"id": "EMAIL-1245", "title": "Email scenario 1245", "data": {"sku": "SKU1245", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1245@example.com", "threshold": 450}},
    {"id": "EMAIL-1246", "title": "Email scenario 1246", "data": {"sku": "SKU1246", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1246@example.com", "threshold": 460}},
    {"id": "EMAIL-1247", "title": "Email scenario 1247", "data": {"sku": "SKU1247", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1247@example.com", "threshold": 470}},
    {"id": "EMAIL-1248", "title": "Email scenario 1248", "data": {"sku": "SKU1248", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1248@example.com", "threshold": 480}},
    {"id": "EMAIL-1249", "title": "Email scenario 1249", "data": {"sku": "SKU1249", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1249@example.com", "threshold": 490}},
    {"id": "EMAIL-1250", "title": "Email scenario 1250", "data": {"sku": "SKU1250", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1250@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
