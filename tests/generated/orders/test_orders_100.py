import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-5961", "title": "Orders scenario 5961", "data": {"sku": "SKU5961", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5961@example.com", "threshold": 610}},
    {"id": "ORDERS-5962", "title": "Orders scenario 5962", "data": {"sku": "SKU5962", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5962@example.com", "threshold": 620}},
    {"id": "ORDERS-5963", "title": "Orders scenario 5963", "data": {"sku": "SKU5963", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5963@example.com", "threshold": 630}},
    {"id": "ORDERS-5964", "title": "Orders scenario 5964", "data": {"sku": "SKU5964", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5964@example.com", "threshold": 640}},
    {"id": "ORDERS-5965", "title": "Orders scenario 5965", "data": {"sku": "SKU5965", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5965@example.com", "threshold": 650}},
    {"id": "ORDERS-5966", "title": "Orders scenario 5966", "data": {"sku": "SKU5966", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5966@example.com", "threshold": 660}},
    {"id": "ORDERS-5967", "title": "Orders scenario 5967", "data": {"sku": "SKU5967", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5967@example.com", "threshold": 670}},
    {"id": "ORDERS-5968", "title": "Orders scenario 5968", "data": {"sku": "SKU5968", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5968@example.com", "threshold": 680}},
    {"id": "ORDERS-5969", "title": "Orders scenario 5969", "data": {"sku": "SKU5969", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5969@example.com", "threshold": 690}},
    {"id": "ORDERS-5970", "title": "Orders scenario 5970", "data": {"sku": "SKU5970", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5970@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
