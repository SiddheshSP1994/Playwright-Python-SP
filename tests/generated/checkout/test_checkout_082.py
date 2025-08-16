import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-4861", "title": "Checkout scenario 4861", "data": {"sku": "SKU4861", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4861@example.com", "threshold": 610}},
    {"id": "CHECKOUT-4862", "title": "Checkout scenario 4862", "data": {"sku": "SKU4862", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4862@example.com", "threshold": 620}},
    {"id": "CHECKOUT-4863", "title": "Checkout scenario 4863", "data": {"sku": "SKU4863", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4863@example.com", "threshold": 630}},
    {"id": "CHECKOUT-4864", "title": "Checkout scenario 4864", "data": {"sku": "SKU4864", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4864@example.com", "threshold": 640}},
    {"id": "CHECKOUT-4865", "title": "Checkout scenario 4865", "data": {"sku": "SKU4865", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4865@example.com", "threshold": 650}},
    {"id": "CHECKOUT-4866", "title": "Checkout scenario 4866", "data": {"sku": "SKU4866", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4866@example.com", "threshold": 660}},
    {"id": "CHECKOUT-4867", "title": "Checkout scenario 4867", "data": {"sku": "SKU4867", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4867@example.com", "threshold": 670}},
    {"id": "CHECKOUT-4868", "title": "Checkout scenario 4868", "data": {"sku": "SKU4868", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4868@example.com", "threshold": 680}},
    {"id": "CHECKOUT-4869", "title": "Checkout scenario 4869", "data": {"sku": "SKU4869", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4869@example.com", "threshold": 690}},
    {"id": "CHECKOUT-4870", "title": "Checkout scenario 4870", "data": {"sku": "SKU4870", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4870@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
